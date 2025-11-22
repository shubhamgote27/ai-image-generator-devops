# 🎨 AI Image Generator - DevOps Edition

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Docker](https://img.shields.io/badge/docker-ready-blue)
![Kubernetes](https://img.shields.io/badge/kubernetes-deployed-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## 📖 Overview

This project demonstrates a complete **DevOps lifecycle** for an AI-powered Image Generation application. The application uses a Python backend (Flask/Streamlit) to generate images based on user prompts (using OpenAI DALL-E, Stable Diffusion, or similar APIs).

The core focus of this repository is not just the AI application, but the **DevOps pipeline** implementation, including containerization, orchestration, and automated deployment.

## 🚀 Features

* **AI Image Generation**: Web interface to accept text prompts and generate images.
* **Containerization**: Fully dockerized application for consistent environments.
* **Orchestration**: Kubernetes manifests for scalable deployment.
* **CI/CD Pipeline**: Automated build and deploy pipelines (Jenkins/GitHub Actions).
* **Infrastructure as Code**: (Optional) Terraform scripts for provisioning cloud resources.

## 🛠️ Tech Stack

* **Application**: Python, Flask / Streamlit
* **Containerization**: Docker
* **Orchestration**: Kubernetes (Minikube / EKS / AKS)
* **CI/CD**: Jenkins / GitHub Actions
* **Version Control**: Git
* **Registry**: Docker Hub / AWS ECR

---

## ⚙️ Prerequisites

Before running the project, ensure you have the following installed:

* [Docker](https://docs.docker.com/get-docker/)
* [Kubernetes CLI (kubectl)](https://kubernetes.io/docs/tasks/tools/)
* [Minikube](https://minikube.sigs.k8s.io/docs/start/) (for local K8s testing)
* Python 3.9+
* An API Key (OpenAI/HuggingFace) if required by the app code.

---

## 🖥️ Local Setup (Without Docker)

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/shubhamgote27/ai-image-generator-devops.git](https://github.com/shubhamgote27/ai-image-generator-devops.git)
    cd ai-image-generator-devops
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set Environment Variables:**
    ```bash
    export OPENAI_API_KEY="your_api_key_here"
    ```

4.  **Run the application:**
    ```bash
    python app.py
    # or if using streamlit
    # streamlit run app.py
    ```
    Access the app at `http://localhost:5000` (or the port specified).

---

## 🐳 Docker Setup

1.  **Build the Docker Image:**
    ```bash
    docker build -t ai-image-generator:v1 .
    ```

2.  **Run the Container:**
    ```bash
    docker run -d -p 5000:5000 --env OPENAI_API_KEY="your_key" --name ai-generator ai-image-generator:v1
    ```

3.  **Verify:**
    Open your browser and visit `http://localhost:5000`.

---

## ☸️ Kubernetes Deployment

This project includes K8s manifests to deploy the application on a cluster.

1.  **Start Minikube (if testing locally):**
    ```bash
    minikube start
    ```

2.  **Apply Deployment and Service:**
    ```bash
    kubectl apply -f k8s/deployment.yaml
    kubectl apply -f k8s/service.yaml
    ```

3.  **Access the App:**
    ```bash
    # For Minikube users to get the URL
    minikube service ai-generator-service --url
    ```

---

## 🔄 CI/CD Pipeline

The project uses a pipeline to automate deployments.

**Workflow:**
1.  **Code Commit**: Developer pushes code to GitHub.
2.  **Build**: CI server builds the Docker image.
3.  **Test**: Runs unit tests (if available).
4.  **Push**: Pushes the image to Docker Hub/ECR.
5.  **Deploy**: Updates the Kubernetes deployment with the new image tag.

*(Note: Check the `Jenkinsfile` or `.github/workflows` directory for the specific pipeline configuration.)*

---

## 📂 Project Structure

```bash
ai-image-generator-devops/
├── app.py              # Main Application Source Code
├── requirements.txt    # Python Dependencies
├── Dockerfile          # Docker Configuration
├── k8s/                # Kubernetes Manifests
│   ├── deployment.yaml
│   └── service.yaml
├── templates/          # HTML Templates (if Flask)
├── static/             # CSS/JS files
├── Jenkinsfile         # CI/CD Pipeline Script
└── README.md           # Documentation
