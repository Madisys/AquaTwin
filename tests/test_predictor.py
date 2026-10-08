import numpy as np
from aquatwin.baseline import fit_baseline
from aquatwin.predictor import predict_with_model

def test_prediction_is_explicitly_experimental():
    X=np.array([[0.],[1.],[2.],[3.]])
    y=np.array([0,0,1,1])
    model=fit_baseline(X,y)
    p=predict_with_model(model,{"x":2.0},["x"],data_quality_score=1.0)
    assert 0 <= p.risk_score <= 1
    assert "EXPERIMENTAL_NOT_OPERATIONALLY_VALIDATED" in p.limitations
    assert len(p.input_hash)==64
