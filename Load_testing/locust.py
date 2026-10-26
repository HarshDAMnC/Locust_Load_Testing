from locust import HttpUser, task, between
import random

sentences=["hi, how are you?","I love python","I am a nice guy"]

class AppUser(HttpUser):
    wait_time=between(2,5)
    @task
    def index_page(self):
        self.client.get('/')
        
    @task
    def sentiment_page(self):
        text=random.choice(sentences)
        self.client.get("/senti/"+str(text))