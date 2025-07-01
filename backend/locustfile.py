from locust import HttpUser, task, between

class SwadhsutraUser(HttpUser):
    wait_time = between(1, 3)  # seconds delay between tasks

    @task(2)
    def get_recipes(self):
        self.client.get("/recipes")

    @task(3)
    def generate_recipe(self):
        self.client.post("/generate", json={"ingredients": "tomato,onion,garlic"})

    @task(1)
    def save_recipe(self):
        self.client.post("/save", json={
            "title": "Stress Test Dish",
            "ingredients": "Tomato, Onion, Garlic",
            "steps": "Mix and cook well."
        })
