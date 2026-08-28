"""Transparent baseline for AT-MORT-001.

This module deliberately avoids clinical/biological thresholds. It learns a simple
logistic model from labelled historical data and exists as a comparator for future
models. It is not validated for operational veterinary use.
"""

from dataclasses import dataclass

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import average_precision_score, brier_score_loss, roc_auc_score


@dataclass(frozen=True)
class BaselineMetrics:
    auroc: float
    auprc: float
    brier: float


def fit_baseline(X: np.ndarray, y: np.ndarray) -> LogisticRegression:
    if X.ndim != 2 or y.ndim != 1 or len(X) != len(y):
        raise ValueError("X/y shape mismatch")
    if len(np.unique(y)) < 2:
        raise ValueError("Training labels require both classes")
    model = LogisticRegression(max_iter=1000, class_weight="balanced", random_state=42)
    model.fit(X, y)
    return model


def evaluate(model: LogisticRegression, X: np.ndarray, y: np.ndarray) -> BaselineMetrics:
    probability = model.predict_proba(X)[:, 1]
    return BaselineMetrics(
        auroc=float(roc_auc_score(y, probability)),
        auprc=float(average_precision_score(y, probability)),
        brier=float(brier_score_loss(y, probability)),
    )
