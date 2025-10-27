from locust import HttpUser, task, between

class WordPressUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def view_post(self):
        self.client.get("/?p=1")  # artigo com imagem 1MB

    @task
    def view_post2(self):
        self.client.get("/?p=2")
    
    @task
    def view_post3(self):
        self.client.get("/?p=3")
