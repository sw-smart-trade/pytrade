import json
from fastapi import APIRouter, Request
from service.recommendation import stock_recommendations

#APIRouter creates path operations for recommendation module
router = APIRouter(
    prefix="/recommendations",
    tags=["Recommendations"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
def read_recommendations(req: Request):
    try:
        print(req.query_params)
        return json.loads(stock_recommendations(int(req.query_params["top"])))
    except:
        return json.loads(stock_recommendations(10))
    
