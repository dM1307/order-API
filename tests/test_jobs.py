def test_job_creation(client):
    resp = client.post(
        "/jobs/", 
        json={"name": "Backup", "schedule": "*/5 * * * *"}
    )
    assert resp.status_code == 201
