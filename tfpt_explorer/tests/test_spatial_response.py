import numpy as np
import pytest

from tfpt_explorer.spatial_response import effective_response, build_spatial_data


def test_rate_response_requires_corrector_and_scales_with_physical_rates():
    r = np.ones(45)
    data = build_spatial_data()["data"]
    r[data["perturbation"]["edge"]] = 2
    a, b = effective_response(r), effective_response(3*r)
    assert np.allclose(b["tensor"], 3*a["tensor"])
    assert np.linalg.norm(a["tensor"] - a["uncorrected_tensor"]) > .05
    assert np.linalg.eigvalsh(a["tensor"]).min() > 0
    assert all(c["ok"] for c in build_spatial_data()["checks"])


def test_invalid_or_disconnected_rate_contract_is_rejected():
    for r in (np.ones(44), np.zeros(45), np.full(45, np.nan), -np.ones(45)):
        with pytest.raises(ValueError):
            effective_response(r)
