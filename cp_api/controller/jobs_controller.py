from flask import Blueprint, request, jsonify
from cp_api.dependencies import get_current_user
from cp_api.auth import token_required
from cp_lib.services.jobs_service import JobService, JobNotFound
from flask import abort
from cp_lib.models.schemas import JobRead
# app/controllers/job_controller.py


job_bp = Blueprint('job_bp', __name__)


def get_job_service():
    return JobService()


@job_bp.route("/jobs", methods=["POST"])
@token_required
def create_jobs():
    body = request.get_json()
    user = get_current_user()
    svc = get_job_service()

    client_id = user["sub"]  # or user["client_id"]
    created = [svc.create_job(**job, client_id=client_id) for job in body]
    return jsonify([JobRead(**j.to_dict()).dict() for j in created])


@job_bp.route("/jobs", methods=["GET"])
@token_required
def list_jobs():
    user = get_current_user()
    svc = get_job_service()

    client_id = user["sub"]
    jobs = svc.list_jobs(client_id=client_id)
    return jsonify([JobRead(**j.to_dict()).dict() for j in jobs])


@job_bp.route("/jobs/<string:job_id>", methods=["GET"])
@token_required
def get_job(job_id: str):
    user = get_current_user()
    svc = get_job_service()

    client_id = user["sub"]
    try:
        job = svc.get_job(job_id, client_id=client_id)
        return jsonify(JobRead(**job.to_dict()).dict())
    except JobNotFound:
        abort(404, description="Job not found")
