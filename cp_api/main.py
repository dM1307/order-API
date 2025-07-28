# import os
from flask import Flask, send_from_directory, render_template
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from cp_api.config import Config
from cp_api.controller.jobs_controller import job_bp
from cp_api.auth import token_required


app = Flask(
    __name__,
    static_folder="specification/static",
    template_folder="specification/static"
)
app.config.from_object(Config)
CORS(app, resources={r"/specification/*": {"origins": "*"}})


@app.route("/v1/docs")
def swagger_ui():
    return render_template(
        "swagger.html",
        OAUTH2_REDIRECT_URI=app.config["OAUTH2_REDIRECT_URI"],
        OAUTH2_CLIENT_ID=app.config["OAUTH2_CLIENT_ID"],
        OAUTH2_CLIENT_SECRET=app.config["OAUTH2_CLIENT_SECRET"],
    )


# Swagger UI
SWAGGER_URL = "/v1/docs"
API_URL = "/specification/openapi.yaml"
swagger_ui_bp = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        "appName": "Chronos Scheduler UI",
        "oauth2RedirectUrl": "http://localhost:5000/v1/docs/oauth2-redirect.html",
    }
)
app.register_blueprint(swagger_ui_bp, url_prefix=SWAGGER_URL)

# --- API Routes -------------------------------------------------------------

# Protect all job routes by default
protected_job_bp = job_bp
# If you want some endpoints open, register twice or split controllers

app.register_blueprint(protected_job_bp, url_prefix="/jobs")

# Apply token_required to all /jobs endpoints
for rule in app.url_map.iter_rules():
    if rule.rule.startswith("/jobs"):
        view = app.view_functions[rule.endpoint]
        app.view_functions[rule.endpoint] = token_required(view)


@app.route("/specification/openapi.yaml")
def spec():
    return send_from_directory(
        "/Users/dineshmaharana/order-API/specification", "openapi.yaml")


if __name__ == "__main__":
    app.run(port=5000)
