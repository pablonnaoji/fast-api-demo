# project/app/models/tortoise.py


from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator  # new

class Recommendation(models.Model):
    url = fields.TextField()
    name = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return self.url


RecommendationSchema = pydantic_model_creator(Recommendation)  # new


class User(models.Model):
    url = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return self.url


UserSchema = pydantic_model_creator(User)  # new