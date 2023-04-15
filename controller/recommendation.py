import json
from fastapi import APIRouter, Request
from service.recommendation import recommendation


#APIRouter creates path operations for recommendation module
router = APIRouter(
    prefix="/recommendation",
    tags=["Recommendation"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
def read_recommendation(req: Request):
    try:
        return json.loads(recommendation(req.query_params["stock"]))
    except:
        return json.loads(recommendation("AAPL"))
    