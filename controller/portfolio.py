import json
from fastapi import APIRouter, Request
from service.portfolio import portfolio_builder

#APIRouter creates path operations for portfolio module
router = APIRouter(
    prefix="/portfolio",
    tags=["Portfolio"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
def read_portfolio_builder(req: Request):
    try:
        return json.loads(portfolio_builder(int(req.query_params["profile"])))
    except:
        return json.loads(portfolio_builder(2))