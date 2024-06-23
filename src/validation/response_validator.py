class ResponseValidator:

    def validate_user_response(self, response, expected_user):
        assert response["id"] == expected_user["id"]
        assert response["name"] == expected_user["name"]
        assert response["username"] == expected_user["username"]
        assert response["email"] == expected_user["email"]
        assert response["phone"] == expected_user["phone"]
        assert response["website"] == expected_user["website"]
        assert response["address"]["street"] == expected_user["address"]["street"]
        assert response["address"]["suite"] == expected_user["address"]["suite"]
        assert response["address"]["city"] == expected_user["address"]["city"]
        assert response["address"]["zipcode"] == expected_user["address"]["zipcode"]
        assert response["address"]["geo"]["lat"] == expected_user["address"]["geo"]["lat"]
        assert response["address"]["geo"]["lng"] == expected_user["address"]["geo"]["lng"]
        assert response["company"]["name"] == expected_user["company"]["name"]
        assert response["company"]["catchPhrase"] == expected_user["company"]["catchPhrase"]
        assert response["company"]["bs"] == expected_user["company"]["bs"]
