# project/app/models/pydantic.py


from pydantic import BaseModel


class RecommendationPayloadSchema(BaseModel):
    url: str

class RecommendtionResponseSchema(RecommendationPayloadSchema):
    id: int
