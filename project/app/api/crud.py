# project/app/api/crud.py


from app.models.pydantic import RecommendationloadSchema
from app.models.tortoise import Recommendation

from typing import Union
from typing import Union, List

async def post(payload: RecommendationPayloadSchema) -> int:
    recommendation = Recommendation(
        url=payload.url,
        song="good song",
    )
    await recommendation.save()
    return recommendation.id


async def get(id: int) -> Union[dict, None]:
    recommendation = await Recommendation.filter(id=id).first().values()
    if recommendation:
        return recommendation[0]
    return None


async def get_all() -> List:
    recommendation = await Recommendation.all().values()
    return recommendation