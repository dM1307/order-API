# 📦 Order API

**Order API** is a modular, scalable, and secure REST API service built using **Flask**, designed with a clean architecture (Hexagonal/Ports & Adapters) for maintainability and extensibility. It supports both synchronous and asynchronous job scheduling and is part of the larger **Chronos** distributed job scheduling system.

---

## ✨ Features

* 🔐 OAuth2-based Authentication using Keycloak
* ♻️ Sync & Async Job Scheduling
* ⏳ Cron-like scheduling support
* 📊 Swagger UI for API exploration
* 🧪 Pytest-based testing with CI/CD
* 📦 Clean separation of interface and business logic (API + LIB split)
* 🌍 Production-ready Docker setup

---

## 📁 Repository Structure

```
order-API/
├── app/                     # Flask Application
│   ├── main.py              # Entry point
│   ├── api/                 # Routes/Controllers
│   └── dependencies/        # Dependency injection & integration
│
├── tests/                   # Pytest test cases
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## 📊 Architecture Overview

```mermaid
graph TD
    A["🌐 NGINX Reverse Proxy"] --> B["🧩 Flask API (order-API)"]
    B --> C["🧠 Order LIB (Business Logic Layer)"]
    C --> D["🗃️ PostgreSQL Database"]
    B --> E["🔐 Keycloak (OAuth2 Provider)"]
    B --> F["📘 Swagger UI (API Docs)"]
```

---

## ⚙️ Tech Stack

| Layer      | Tool / Tech            |
| ---------- | ---------------------- |
| Web Server | NGINX                  |
| API Layer  | Flask                  |
| Auth       | Keycloak (OAuth2)      |
| DB         | PostgreSQL             |
| Doc        | Swagger/OpenAPI        |
| Tests      | Pytest                 |
| CI/CD      | GitHub Actions         |
| Container  | Docker, Docker Compose |

---

## 🪰 Local Development Setup

### 🔧 Prerequisites

* Python 3.10+
* Docker + Docker Compose
* Poetry or pip
* Keycloak running locally or remotely

---

### 📦 Step 1: Clone & Install

```bash
git clone https://github.com/dM1307/order-API.git
cd order-API
pip install -r requirements.txt
```

---

### 🔐 Step 2: Configure Environment

Create a `.env` file:

```dotenv
DATABASE_URL=postgresql://user:pass@localhost:5432/orderdb
KEYCLOAK_URL=http://localhost:8080
KEYCLOAK_REALM=chronos
KEYCLOAK_CLIENT_ID=order-api
KEYCLOAK_CLIENT_SECRET=your_client_secret
```

---

### ▶️ Step 3: Run the App

```bash
docker-compose up --build
```

Swagger UI will be available at:
👉 [http://localhost:5000/docs](http://localhost:5000/docs)

---

## 🔐 Authentication Flow

1. Users authenticate via Keycloak
2. Access tokens are passed to protected endpoints
3. API decodes token and extracts `client_id` for filtering jobs

---

## 🧪 Running Tests

```bash
pytest tests/
```

---

## 🎯 Sample API Endpoints

| Endpoint            | Method | Description          |
| ------------------- | ------ | -------------------- |
| `/jobs`             | GET    | List jobs for client |
| `/jobs`             | POST   | Create a new job     |
| `/jobs/<id>`        | GET    | Get job details      |
| `/jobs/<id>/status` | PATCH  | Update job status    |

Use Swagger UI or Postman with a valid access token.

---

## 💡 Design Principles

* **Hexagonal Architecture**: decouples domain from frameworks
* **Separation of Concerns**: API, Logic, and Persistence split
* **Token-Based Context**: Jobs filtered via `client_id` from token
* **Async Ready**: Support for non-blocking jobs

---

## ↺ CI/CD & Quality

* ✅ Auto lint with Flake8
* ✅ Unit & integration tests via Pytest
* ✅ GitHub Actions for build/test on push

---

## 📘 License

MIT License © 2025 [Dinesh Maharana](https://github.com/dM1307)

---

## 🙌 Contributions

* Fork the repo
* Create a feature branch
* Open a PR with clear title/description

---

## 🔗 Related Projects

* [Chronos LIB](https://github.com/dM1307/Order-lib)
* [Chronos Orchestrator](https://github.com/dM1307/Orchestrator)

---

Built with 💙 by [Dinesh Maharana](https://github.com/dM1307)
