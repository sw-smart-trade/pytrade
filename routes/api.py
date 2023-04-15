from fastapi import APIRouter
from controller import portfolio, recommendation, recommendations

router = APIRouter()
router.include_router(portfolio.router)
router.include_router(recommendation.router)
router.include_router(recommendations.router)