# project/app/api/summaries.py


from fastapi import APIRouter, HTTPException

from app.api import crud
from app.models.pydantic import RecommendationPayloadSchema, RecommendationResponseSchema

from app.models.tortoise import RecommendationSchema
from typing import List

router = APIRouter()


@router.post("/", response_model=RecommendationResponseSchema, status_code=201)
async def create_recommendation(payload: RecommendationPayloadSchema) -> RecommendationResponseSchema:
    recommendation_id = await crud.post(payload)

    response_object = {
        "id": recommendation_id,
        "url": payload.url
    }
    return response_object



@router.get("/{id}/", response_model=RecommendationSchema)
async def read_recommendation(id: int) -> RecommendationSchema:
    recommendation = await crud.get(id)
    if not recommendation:
        raise HTTPException(status_code=404, detail="Recommendation not found")

    return recommendation


@router.get("/", response_model=List[RecommendationSchema])
async def read_all_recommendations() -> List[RecommendationSchema]:
    return await crud.get_all()

