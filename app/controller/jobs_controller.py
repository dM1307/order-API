from flask import Blueprint, request, jsonify
from chronos_lib.services import JobService, JobNotFound
from chronos_lib.schemas import JobCreate, JobRead

job_bp = Blueprint("job_api", __name__)

service = JobService()


@job_bp.route("", methods=["POST"])
def create_job():
    payload = JobCreate(**request.json)
    job = service.create_job(**payload.dict())
    return jsonify(JobRead(**job.to_dict()).dict()), 201


@job_bp.route("/<job_id>", methods=["GET"])
def get_job(job_id):
    try:
        job = service.get_job(job_id)
        return jsonify(JobRead(**job.to_dict()).dict()), 200
    except JobNotFound:
        return jsonify({"error": "Job not found"}), 404


@job_bp.route("", methods=["GET"])
def list_jobs():
    jobs = service.list_jobs()
    return jsonify([JobRead(**j.to_dict()).dict() for j in jobs]), 200
