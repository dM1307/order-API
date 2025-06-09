from lib.src.services.job_service import JobService
from lib.src.adapters.job_repository import JobRepository


def get_job_service():
    return JobService(repository=JobRepository())
