def test_api_get_request(playwright):
    request = playwright.request.new_context(
        extra_http_headers={"Authorization": "Bearer YOUR_API_KEY",
                            "Accept": "application/json",
                            "x-api-key": "reqres-free-v1"
        }
    )

    response = request.get("https://reqres.in/api/users?page=2")
    assert response.status == 200
    data  = response.json()
    print(f"response Data: {data}")
    assert data["data"][3]["first_name"] == "Byron"
    request.dispose()