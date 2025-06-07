from app.db import db
from enum import Enum
import uuid


class JobStatus(Enum):
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class Job(db.Model):

    __tablename__ = 'jobs'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(255), nullable=False)
    schedule = db.Column(db.String, nullable=False)  # cron or interval
    status = db.Column(db.Enum(JobStatus), default=JobStatus.PENDING, nullable=False)
    retries = db.Column(db.Integer, default=0)
    priority = db.Column(db.Integer, default=5)
    created_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now(), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "schedule": self.schedule,
            "status": self.status.value,  # status of the job
            "retries": self.retries,
            "priority": self.priority,
            "created_at": self.created_at.isoformat(),  # creation timestamp
            "updated_at": self.updated_at.isoformat()  # update timestamp
        }
