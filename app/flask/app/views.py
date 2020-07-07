from app import app
import os

@app.route("/")
def index():

    # Use os.getenv("key") to get environment variables
    app_name = os.getenv("APP_NAME")

    if app_name:
        return f"This is {app_name} microservice running inside a Docker container behind Nginx!"

    return "Container is not working!!!"