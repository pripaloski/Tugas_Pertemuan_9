from locust import HttpUser, task, between
import re

class WebsiteUser(HttpUser):
    wait_time = between(1, 2)
    
    def on_start(self):
        """Setup session with login"""
        # Get the login page first to get the CSRF token
        with self.client.get("/admin/login/", catch_response=True) as response:
            if response.status_code == 200:
                # Extract CSRF token from the response content
                csrf_token_pattern = r'name="csrfmiddlewaretoken" value="(.+?)"'
                match = re.search(csrf_token_pattern, response.text)
                if match:
                    csrf_token = match.group(1)
                    # Perform login with the CSRF token
                    login_response = self.client.post(
                        "/admin/login/",
                        data={
                            "username": "qwe",  # Username Anda
                            "password": "qwe",  # Password Anda
                            "csrfmiddlewaretoken": csrf_token,
                            "next": "/admin/"
                        },
                        headers={
                            "Referer": "http://localhost:8000/admin/login/",
                            "X-CSRFToken": csrf_token
                        },
                        allow_redirects=True
                    )
                    
                    if login_response.status_code == 200 or login_response.status_code == 302:
                        response.success()
                    else:
                        response.failure(f"Login failed with status code: {login_response.status_code}")
                else:
                    response.failure("Could not find CSRF token")
            else:
                response.failure(f"Could not get login page, status code: {response.status_code}")

    @task(3)
    def view_home(self):
        """Access home page"""
        with self.client.get("/", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Got status code {response.status_code}")

    @task(2)
    def view_courses(self):
        """Access courses page"""
        with self.client.get("/courses/", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Got status code {response.status_code}")

    @task(1)
    def view_admin(self):
        """Access admin page"""
        with self.client.get("/admin/", catch_response=True) as response:
            if response.status_code == 200 or response.status_code == 302:
                response.success()
            else:
                response.failure(f"Got status code {response.status_code}") 