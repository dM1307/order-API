# app/controllers/job_controller.py

from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.dependencies import get_current_user
from chronos_lib.services import JobService, JobNotFound
from chronos_lib.schemas import JobCreate, JobRead

router = APIRouter()


def get_job_service():
    return JobService()


@router.post("/", response_model=List[JobRead])
def create_jobs(
    body: List[JobCreate],
    user=Depends(get_current_user),
    svc: JobService = Depends(get_job_service)
):
    client_id = user["sub"]  # or user["client_id"]
    created = [svc.create_job(**job.dict(), client_id=client_id) for job in body]
    return [JobRead(**j.to_dict()).dict() for j in created]


@router.get("/", response_model=List[JobRead])
def list_jobs(
    user=Depends(get_current_user),
    svc: JobService = Depends(get_job_service)
):
    client_id = user["sub"]
    jobs = svc.list_jobs(client_id=client_id)
    return [JobRead(**j.to_dict()).dict() for j in jobs]


@router.get("/{job_id}", response_model=JobRead)
def get_job(
    job_id: str,
    user=Depends(get_current_user),
    svc: JobService = Depends(get_job_service)
):
    client_id = user["sub"]
    try:
        job = svc.get_job(job_id, client_id=client_id)
        return JobRead(**job.to_dict()).dict()
    except JobNotFound:
        raise HTTPException(status_code=404, detail="Job not found")
