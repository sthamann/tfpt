import { comparisonFor } from "@/lib/measurement-comparisons";
import { predictionById } from "@/lib/frozen-predictions";
import { SharedSeedMechanism,VacuumScaleMechanism,InflationRelationMechanism } from "./ReadoutMechanisms";

export function SharedSeedDerivation(){
 const observations=["LAMBDA_C","SIN2_THETA13","BETA_BIREFRINGENCE_DEG","OMEGA_B"].map(id=>{const r=comparisonFor(id);return {id,title:r.shortTitle,center:Number(r.central),minus:Number(r.uncertaintyMinus),plus:Number(r.uncertaintyPlus||r.uncertaintyMinus),measured:r.measured,date:r.date,href:r.href};});
 return <SharedSeedMechanism observations={observations}/>;
}
export function CosmologyDerivation(){return <><VacuumScaleMechanism inverseAlpha={Number(predictionById("ALPHA_INV").frozen_value)}/><InflationRelationMechanism center={.9752} uncertainty={.0030}/></>;}
