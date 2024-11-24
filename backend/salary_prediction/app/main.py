from configuration.config import *
from api.prediction.prediction_router import *
import uvicorn

# router.mount('/api/v1', router )

app.include_router(router)

if __name__ == '__main__':
    uvicorn.run("main:app", host="localhost",port=5001, reload=True)