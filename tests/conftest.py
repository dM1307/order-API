import pytest
from flask import Flask
from app.main import app as flask_app
from app.controllers.job_controller import JobNotFound


# Dummy in-memory job and service for controller tests
class DummyJob:
    def __init__(self, id, name, schedule, retries, priority, status):
        self.id = id
        self.name = name
        self.schedule = schedule
        self.retries = retries
        self.priority = priority
        self.status = status

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "schedule": self.schedule,
            "retries": self.retries,
            "priority": self.priority,
            "status": self.status
        }


class DummyService:
    def __init__(self):
        self.jobs = {
            "job-123": DummyJob("job-123", "Test Job", "* * * * *", 1, 5, "PENDING")
        }

    def create_job(self, name, schedule, retries, priority):
        job = DummyJob("job-456", name, schedule, retries, priority, "PENDING")
        self.jobs[job.id] = job
        return job

    def get_job(self, job_id):
        if job_id not in self.jobs:
            raise JobNotFound(job_id)
        return self.jobs[job_id]

    def list_jobs(self):
        return list(self.jobs.values())


@pytest.fixture(scope="session")
def app() -> Flask:
    """Create and configure a new app instance for each test session."""
    # Ensure blueprint is registered only once
    flask_app.register_blueprint(
        __import__("app.controllers.job_controller", fromlist=["job_bp"]).job_bp,
        url_prefix="/jobs"
    )
    return flask_app


@pytest.fixture
def client(app):
    """A test client for the Flask app."""
    return app.test_client()


@pytest.fixture(autouse=True)
def patch_service(monkeypatch):
    """Automatically replace real JobService with DummyService in controller."""
    dummy = DummyService()
    # Monkey-patch the service object in the controller module
    import app.controllers.job_controller as jc
    monkeypatch.setattr(jc, "service", dummy)
    return dummy
