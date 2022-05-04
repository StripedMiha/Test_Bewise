import requests

url = "https://jservice.io/api/random?count="


async def get_questions(count: int = 1) -> list[dict]:
    ans = requests.get(f"{url}{count}").json()
    return ans
