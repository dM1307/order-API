from app.models.job import Job, db


# app/services/job_services.py
class JobService:
    @staticmethod
    def create(data):
        job = Job(**data)
        db.session.add(job)
        db.session.commit()
        return job

    @staticmethod
    def get(job_id):
        return Job.query.get(job_id)

    @staticmethod
    def list():
        return Job.query.all()

    @staticmethod
    def update(job_id, updates):
        job = Job.query.get(job_id)
        if not job:
            return None
        for k, v in updates.items():
            setattr(job, k, v)
        db.session.commit()
        return job

    @staticmethod
    def delete(job_id):
        job = Job.query.get(job_id)
        if job:
            db.session.delete(job)
            db.session.commit()
            return True
        return False
