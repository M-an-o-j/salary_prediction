from configuration.config import APIRouter, Depends, get_model
from .prediction_controller import prediction_controller

router = APIRouter()

@router.get("/prediction", summary="Prediction Router",tags=["Prediction"])
def prediction_router(age:int,exp:int,model = Depends(get_model)):
    return prediction_controller(age,exp,model)