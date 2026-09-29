"""Sufficient state for the existing charged E8 source action.

This is a stateful form of the lift calculation in :mod:`cartan_source`, not a
new dynamics.  An explicitly supplied native reflection label updates

* the naked E8 lattice action, and
* one eight-bit lattice-character carry.

The canonical quadratic lift phase is fixed by the current lattice action, so
the word that produced the state is unnecessary for every future charged-root
action.  Naked Cartan/C4 data see only the first component.  Charged vertex
operators also see the carry.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
import json
from typing import Any, Iterable

from .cartan_source import (
    PHASE_LIFT_SOURCE,
    V128_GLUE_SOURCE,
    V492_DECK_SOURCE,
    _apply_columns,
    _bitmask,
    _cocycle_exponent,
    _lattice_data,
    _parity,
    _quadratic_mask,
    _quadratic_value,
    _reflection_lift,
)


@lru_cache(maxsize=1)
def _lower() -> tuple[tuple[int, ...], ...]:
    return _lattice_data()["lower"]


@lru_cache(maxsize=1)
def _cocycle_table() -> tuple[tuple[int, ...], ...]:
    lower = _lower()
    return tuple(
        tuple(_cocycle_exponent(left, right, lower) for right in range(256))
        for left in range(256)
    )


@dataclass(frozen=True)
class SourceAction:
    """A sufficient future state for the charged lattice-VOA action.

    ``permutation`` is the exact action on the 240 E8 roots.
    ``action_columns_mod2`` is its action on ``L/2L`` in the original simple
    E8 basis.  ``character_carry`` is the remaining linear lift phase.  The
    canonical quadratic phase is recomputed from the action and is therefore
    not an independent state variable.
    """

    permutation: tuple[int, ...]
    action_columns_mod2: tuple[int, ...]
    character_carry: int

    def __post_init__(self) -> None:
        if len(self.permutation) != 240 or set(self.permutation) != set(range(240)):
            raise ValueError("permutation must act bijectively on all 240 E8 roots")
        if len(self.action_columns_mod2) != 8:
            raise ValueError("the L/2L action needs eight columns")
        if any(column < 0 or column > 255 for column in self.action_columns_mod2):
            raise ValueError("each L/2L action column must be an eight-bit word")
        if self.character_carry < 0 or self.character_carry > 255:
            raise ValueError("character carry must be an eight-bit word")

    @classmethod
    def identity(cls) -> "SourceAction":
        return cls(tuple(range(240)), tuple(1 << index for index in range(8)), 0)

    @property
    def canonical_quadratic_mask(self) -> int:
        return _quadratic_mask(self.action_columns_mod2, _lower())

    def phase_exponent(self, lattice_word: int) -> int:
        """Return ``phi_g(x)`` in ``(-1)^phi_g(x) E_{gx}``."""

        if lattice_word < 0 or lattice_word > 255:
            raise ValueError("lattice_word must represent L/2L")
        return (
            _quadratic_value(self.canonical_quadratic_mask, lattice_word)
            ^ _parity(self.character_carry & lattice_word)
        )

    def apply_native_reflection(self, label: int) -> "SourceAction":
        """Append one explicitly selected native reflection to the action."""

        if label < 0 or label >= 60:
            raise ValueError("native reflection label must be between 0 and 59")
        generator = _reflection_lift(label)
        gen_permutation = generator["permutation"]
        gen_columns = generator["action_columns_mod2"]
        new_permutation = tuple(
            self.permutation[gen_permutation[index]] for index in range(240)
        )
        new_carry = 0
        current_quadratic = self.canonical_quadratic_mask
        for index in range(8):
            exponent = (
                (generator["least_correction"] >> index) & 1
            ) ^ _quadratic_value(current_quadratic, gen_columns[index]) ^ _parity(
                self.character_carry & gen_columns[index]
            )
            new_carry |= exponent << index
        new_columns = tuple(
            _apply_columns(self.action_columns_mod2, gen_columns[index])
            for index in range(8)
        )
        return SourceAction(new_permutation, new_columns, new_carry)

    def apply_word(self, labels: Iterable[int]) -> "SourceAction":
        state = self
        for label in labels:
            state = state.apply_native_reflection(int(label))
        return state

    def effect_on_root(self, beta: tuple[int, ...]) -> dict[str, Any]:
        """Apply the lifted action to the charged vertex field ``E_beta``."""

        lattice = _lattice_data()
        try:
            root_index = lattice["roots"].index(tuple(beta))
        except ValueError as error:
            raise ValueError("beta must be one of the 240 native E8 roots") from error
        coordinates = lattice["root_coordinates"][root_index]
        exponent = self.phase_exponent(_bitmask(coordinates))
        target_index = self.permutation[root_index]
        return {
            "source_root": list(beta),
            "target_root": list(lattice["roots"][target_index]),
            "sign": -1 if exponent else 1,
            "phase_exponent_mod2": exponent,
        }

    def preserves_ordered_vertex_cocycle(self, exhaustive: bool = False) -> bool:
        """Check the exact lift identity on ``L/2L``.

        The two sides are bilinear after taking the coboundary of the quadratic
        phase, so the 64 basis pairs prove the identity for all lattice words.
        ``exhaustive=True`` additionally evaluates all 65,536 pairs.
        """

        words = range(256) if exhaustive else (1 << index for index in range(8))
        word_list = tuple(words)
        table = _cocycle_table()
        quadratic = self.canonical_quadratic_mask
        phases = tuple(
            _quadratic_value(quadratic, word)
            ^ _parity(self.character_carry & word)
            for word in range(256)
        )
        mapped = tuple(
            _apply_columns(self.action_columns_mod2, word) for word in range(256)
        )
        for left in word_list:
            for right in word_list:
                coboundary = (
                    phases[left]
                    ^ phases[right]
                    ^ phases[left ^ right]
                )
                cocycle_change = (
                    table[mapped[left]][mapped[right]]
                    ^ table[left][right]
                )
                if coboundary != cocycle_change:
                    return False
        return True

    def to_dict(self) -> dict[str, Any]:
        """Stable restart payload.  It intentionally contains no word history."""

        return {
            "schema": "tfpt.source-action.v1",
            "permutation": list(self.permutation),
            "action_columns_mod2": list(self.action_columns_mod2),
            "character_carry": self.character_carry,
        }

    @classmethod
    def from_dict(cls, payload: dict[str, Any]) -> "SourceAction":
        if payload.get("schema") != "tfpt.source-action.v1":
            raise ValueError("unsupported source-action schema")
        return cls(
            tuple(int(value) for value in payload["permutation"]),
            tuple(int(value) for value in payload["action_columns_mod2"]),
            int(payload["character_carry"]),
        )


def _check(name: str, actual: Any, expected: Any, method: str) -> dict[str, Any]:
    return {
        "name": name,
        "ok": actual == expected,
        "actual": actual,
        "expected": expected,
        "method": method,
    }


@lru_cache(maxsize=1)
def build_source_process_data() -> dict[str, Any]:
    left_word = (0, 1, 0)
    right_word = (2, 1, 2)
    left = SourceAction.identity().apply_word(left_word)
    right = SourceAction.identity().apply_word(right_word)
    same_bare_action = (
        left.permutation == right.permutation
        and left.action_columns_mod2 == right.action_columns_mod2
    )
    carry_difference = left.character_carry ^ right.character_carry

    lattice = _lattice_data()
    witness_index = next(
        index for index, coordinates in enumerate(lattice["root_coordinates"])
        if _parity(carry_difference & _bitmask(coordinates))
    )
    witness_beta = lattice["roots"][witness_index]
    left_effect = left.effect_on_root(witness_beta)
    right_effect = right.effect_on_root(witness_beta)
    # Diagnostic trajectories for the guided replay.  They are outputs, not
    # part of the sufficient state saved by SourceAction.to_dict().
    trajectories = []
    for word in (left_word, right_word):
        state = SourceAction.identity()
        steps = []
        for label in (None, *word):
            if label is not None:
                state = state.apply_native_reflection(label)
            steps.append({
                "event_label": label,
                "character_carry": state.character_carry,
                "carry_bits": format(state.character_carry, "08b"),
                "root_effect": state.effect_on_root(witness_beta),
            })
        trajectories.append(steps)

    # A restart after the two-event prefix must give the same future state as
    # uninterrupted composition.  No past labels are stored in the payload.
    prefix = SourceAction.identity().apply_word((0, 1))
    payload = json.loads(json.dumps(prefix.to_dict()))
    restarted = SourceAction.from_dict(payload)
    after_restart = restarted.apply_word((0, 13, 7))
    uninterrupted = SourceAction.identity().apply_word((0, 1, 0, 13, 7))

    generator_choice_counts = tuple(
        len(_reflection_lift(label)["corrections"]) for label in range(60)
    )
    generator_cocycle_passes = sum(
        SourceAction.identity().apply_native_reflection(label)
        .preserves_ordered_vertex_cocycle()
        for label in range(60)
    )
    path_cocycles = (
        left.preserves_ordered_vertex_cocycle(exhaustive=True),
        right.preserves_ordered_vertex_cocycle(exhaustive=True),
    )

    checks = [
        _check("all native reflection labels have involutive lift choices",
               [min(generator_choice_counts), max(generator_choice_counts)], [64, 64],
               "exact character enumeration for labels 0 through 59"),
        _check("all 60 source-event updates preserve the ordered vertex cocycle",
               generator_cocycle_passes, 60,
               "64 bilinear basis cells per generator"),
        _check("two original words have the same naked Cartan action",
               same_bare_action, True,
               "exact 240-root permutation and L/2L matrix equality"),
        _check("the retained carry difference is the D5+A3 deck character",
               carry_difference, 152,
               "exact least-section composition"),
        _check("the charged witness retains the relative path sign",
               [left_effect["target_root"] == right_effect["target_root"],
                left_effect["sign"] * right_effect["sign"]],
               [True, -1],
               "lifted action on one actual E8 root field"),
        _check("both composed path actions preserve the full cocycle table",
               list(path_cocycles), [True, True],
               "all 256 by 256 lattice-class pairs per path"),
        _check("restart state is sufficient for future event composition",
               after_restart == uninterrupted, True,
               "JSON round trip before three further native events"),
        _check("restart payload contains no dispensable word history",
               sorted(payload),
               ["action_columns_mod2", "character_carry", "permutation", "schema"],
               "serialized-state key census"),
    ]
    return {
        "data": {
            "state_schema": "tfpt.source-action.v1",
            "state_variables": [
                "exact permutation of 240 E8 roots",
                "eight columns of the induced L/2L action",
                "eight-bit character carry",
            ],
            "history_required_for_future_updates": False,
            "available_native_reflection_labels": 60,
            "involutive_lift_choices_per_label": 64,
            "path_comparison": {
                "left_word": list(left_word),
                "right_word": list(right_word),
                "same_naked_Cartan_action": same_bare_action,
                "character_carry_difference": carry_difference,
                "deck_character": 152,
                "charged_root_witness": list(witness_beta),
                "left_effect": left_effect,
                "right_effect": right_effect,
                "trajectories": trajectories,
            },
            "restart": {
                "payload": payload,
                "future_labels": [0, 13, 7],
                "matches_uninterrupted_composition": after_restart == uninterrupted,
            },
            "cocycle": {
                "generators_passed": generator_cocycle_passes,
                "generators_total": 60,
                "path_full_tables_passed": sum(path_cocycles),
                "path_full_tables_total": 2,
            },
        },
        "checks": checks,
        "sources": [
            "tfpt_explorer/cartan_source.py",
            PHASE_LIFT_SOURCE,
            V128_GLUE_SOURCE,
            V492_DECK_SOURCE,
        ],
        "scope": [
            "This is the exact finite update state of the existing E8 cocycle lift, not a newly selected dynamics.",
            "An external process must explicitly supply each reflection label; no yield rule, event probability, autonomous choice, state preparation, or CP completion is introduced.",
            "The naked C4/Cartan action cannot see the character carry.  Charged root fields and coherent comparisons of two paths can see its relative sign.",
            "A sign on one isolated charged basis field is not by itself an observable global phase; observability requires a coherent path reference or a charged correlator retaining both alternatives.",
        ],
    }


if __name__ == "__main__":
    print(json.dumps(build_source_process_data(), indent=2, sort_keys=True))
