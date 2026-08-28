from datetime import datetime
from typing import Literal
from uuid import UUID

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from .quality import assess_observation

app = FastAPI(title="AquaTwin AT-MORT-001 API", version="0.1.0")


class ObservationIn(BaseModel):
    cage_id: UUID
    cohort_id: UUID | None = None
    observed_at: datetime
    variable_code: str = Field(min_length=1, max_length=80)
    value: float
    unit: str = Field(min_length=1, max_length=40)
    source_id: str = Field(min_length=1, max_length=200)
    synthetic: bool = False


class ObservationAccepted(BaseModel):
    status: Literal["accepted", "accepted_for_review"]
    quality_flag: Literal["PASS", "REVIEW"]
    data_quality_score: float
    reasons: list[str]
    synthetic: bool


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "module": "AT-MORT-001"}


@app.post("/v1/observations", response_model=ObservationAccepted)
def ingest_observation(payload: ObservationIn) -> ObservationAccepted:
    quality = assess_observation(payload.variable_code, payload.value, payload.source_id)
    if not quality.valid:
        raise HTTPException(status_code=422, detail={"quality_flag": quality.quality_flag, "reasons": quality.reasons})

    return ObservationAccepted(
        status="accepted" if quality.quality_flag == "PASS" else "accepted_for_review",
        quality_flag=quality.quality_flag,
        data_quality_score=quality.score,
        reasons=list(quality.reasons),
        synthetic=payload.synthetic,
    )
