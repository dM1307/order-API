from flask import Blueprint, request, jsonify
from app.services.job_service import JobService

job_bp = Blueprint("jobs", __name__, url_prefix="/jobs")


@job_bp.route("/", methods=["POST"])
def create_job():
    job = JobService.create(request.json)
    return jsonify(job.to_dict()), 201


@job_bp.route("/<job_id>", methods=["GET"])
def get_job(job_id):
    job = JobService.get(job_id)
    if job:
        return jsonify(job.to_dict())
    return jsonify({"error": "Not found"}), 404


@job_bp.route("/", methods=["GET"])
def list_jobs():
    jobs = JobService.list()
    return jsonify([j.to_dict() for j in jobs])


@job_bp.route("/<job_id>", methods=["PUT"])
def update_job(job_id):
    updated = JobService.update(job_id, request.json)
    if updated:
        return jsonify(updated.to_dict())
    return jsonify({"error": "Not found"}), 404


@job_bp.route("/<job_id>", methods=["DELETE"])
def delete_job(job_id):
    success = JobService.delete(job_id)
    return (jsonify({}), 204) if success else \
           (jsonify({"error": "Not found"}), 404)
