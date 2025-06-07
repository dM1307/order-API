from flask import Flask, send_from_directory
from flask_swagger_ui import get_swaggerui_blueprint
from app.config import Config
from app.controllers.job_controller import job_bp

app = Flask(__name__)
app.config.from_object(Config)

# Swagger UI
SWAGGER_URL = "/docs"
API_URL = "/openapi.yaml"
swagger_bp = get_swaggerui_blueprint(SWAGGER_URL, API_URL)
app.register_blueprint(swagger_bp, url_prefix=SWAGGER_URL)

# Routes
app.register_blueprint(job_bp, url_prefix="/jobs")


@app.route("/openapi.yaml")
def spec():
    return send_from_directory("app", "openapi.yaml")


if __name__ == "__main__":
    app.run(port=5000)
