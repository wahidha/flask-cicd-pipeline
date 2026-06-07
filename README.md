# Flask CI/CD Pipeline with Docker & GitHub Actions

Automated CI/CD pipeline for a Python Flask application using Docker and GitHub Actions.

## 🔄 Pipeline Flow
```text
Code Push ➔ GitHub Actions Trigger ➔ Install Dependencies ➔ Run Tests ➔ Build Docker Image ➔ Verify Container
```

## 🛠️ Tech Stack
- **App:** Python Flask
- **Container:** Docker
- **CI/CD:** GitHub Actions
- **Testing:** Pytest

## 🚀 Run Locally
```text
docker build -t flask-app .
docker run -p 5000:5000 flask-app
```