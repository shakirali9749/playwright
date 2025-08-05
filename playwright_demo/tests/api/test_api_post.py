from playwright.sync_api import sync_playwright


def test_post_api():
   with sync_playwright() as p:
       request_context = p.request.new_context()
       response = request_context.post(
           "https://reqres.in/api/users",
           json={"name": "Alice", "job": "Engineer"}
       )
       assert response.status == 201
       print(response.json())
       request_context.dispose()
