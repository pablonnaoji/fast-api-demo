# project/tests/test_recommendations.py


import json

import pytest


def test_create_recommendation(test_app_with_db):
    response = test_app_with_db.post("/recommendations/", data=json.dumps({"url": "https://foo.bar"}))

    assert response.status_code == 201
    assert response.json()["url"] == "https://foo.bar"


def test_create_summaries_invalid_json(test_app):
    response = test_app.post("/recommendations/", data=json.dumps({}))
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "url"],
                "msg": "field required",
                "type": "value_error.missing"
            }
        ]
    }

def test_read_recommendation(test_app_with_db):
    response = test_app_with_db.post("/recommendations/", data=json.dumps({"url": "https://foo.bar"}))
    recommendation_id = response.json()["id"]

    response = test_app_with_db.get(f"/recommendations/{recommendation_id}/")
    assert response.status_code == 200

    response_dict = response.json()
    assert response_dict["id"] == recommendation_id
    assert response_dict["url"] == "https://foo.bar"
    assert response_dict["recommendation"]
    assert response_dict["created_at"]


def test_read_recommendation_incorrect_id(test_app_with_db):
    response = test_app_with_db.get("/recommendations/999/")
    assert response.status_code == 404
    assert response.json()["detail"] == "Summary not found"


def test_read_all_recommendations(test_app_with_db):
    response = test_app_with_db.post("/recommendations/", data=json.dumps({"url": "https://foo.bar"}))
    recommendation_id = response.json()["id"]

    response = test_app_with_db.get("/recommendations/")
    assert response.status_code == 200

    response_list = response.json()
    assert len(list(filter(lambda d: d["id"] == recommendation_id, response_list))) == 1