"""Prediction service primitives for AT-MORT-001.

No bundled model is represented as biologically or operationally validated.
"""
from __future__ import annotations
from dataclasses import dataclass
import hashlib, json
import numpy as np

@dataclass(frozen=True)
class Prediction:
    risk_score: float
    confidence: float | None
    data_quality_score: float
    model_id: str
    model_version: str
    feature_version: str
    input_hash: str
    limitations: tuple[str,...]

def hash_features(features: dict[str,float]) -> str:
    payload=json.dumps(features,sort_keys=True,separators=(",",":"))
    return hashlib.sha256(payload.encode()).hexdigest()

def predict_with_model(model, features: dict[str,float], ordered_features: list[str], *, data_quality_score: float, model_version: str="experimental") -> Prediction:
    missing=[f for f in ordered_features if f not in features]
    if missing: raise ValueError(f"missing features: {missing}")
    x=np.array([[features[f] for f in ordered_features]],dtype=float)
    risk=float(model.predict_proba(x)[0,1])
    limitations=("EXPERIMENTAL_NOT_OPERATIONALLY_VALIDATED","NOT_A_VETERINARY_INDICATION")
    return Prediction(risk,None,float(data_quality_score),"AT-MORT-001",model_version,"features-v1",hash_features(features),limitations)
