
def test_create_job_success(client):
    payload = {
        "name": "New Job",
        "schedule": "*/5 * * * *",
        "retries": 2,
        "priority": 3
    }
    resp = client.post("/jobs", json=payload)
    assert resp.status_code == 201
    data = resp.get_json()
    assert data["name"] == "New Job"
    assert data["schedule"] == "*/5 * * * *"
    assert data["retries"] == 2
    assert data["priority"] == 3
    assert "id" in data
    assert data["status"] == "PENDING"


def test_get_job_success(client):
    # DummyService pre-populates job-123
    resp = client.get("/jobs/job-123")
    assert resp.status_code == 200
    data = resp.get_json()
    assert data["id"] == "job-123"
    assert data["name"] == "Test Job"
    assert data["schedule"] == "* * * * *"
    assert data["status"] == "PENDING"


def test_get_job_not_found(client):
    resp = client.get("/jobs/nonexistent")
    assert resp.status_code == 404
    data = resp.get_json()
    assert data["error"] == "Job not found"


def test_list_jobs(client):
    resp = client.get("/jobs")
    assert resp.status_code == 200
    jobs = resp.get_json()
    assert isinstance(jobs, list)
    # At least the dummy job
    assert any(j["id"] == "job-123" for j in jobs)
