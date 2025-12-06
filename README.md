# GDG Hackathon - FastAPI Health Endpoint

A simple FastAPI application with a health check endpoint, containerized with Docker and managed with `uv`.

## 🚀 Features

- ✅ FastAPI web framework
- ✅ Health check endpoint
- ✅ Docker containerization
- ✅ Docker Compose orchestration
- ✅ Dependency management with `uv`
- ✅ Automatic health monitoring

## 📋 Prerequisites

- Python 3.12+
- [uv](https://github.com/astral-sh/uv) package manager
- Docker and Docker Compose (for containerized deployment)

## 🛠️ Installation

### Local Development

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd GDG
   ```

2. **Install dependencies with uv:**
   ```bash
   uv sync
   ```

3. **Run the application:**
   ```bash
   uv run python main.py
   ```
   
   Or use uvicorn directly:
   ```bash
   uv run uvicorn main:app --reload
   ```

4. **Access the application:**
   - API: http://localhost:8000
   - Health endpoint: http://localhost:8000/health
   - Swagger UI: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

### Docker Deployment

1. **Build and start the container:**
   ```bash
   docker compose up -d
   ```

2. **View logs:**
   ```bash
   docker compose logs -f api
   ```

3. **Stop the container:**
   ```bash
   docker compose down
   ```

4. **Rebuild after changes:**
   ```bash
   docker compose up -d --build
   ```

## 📡 API Endpoints

### Health Check

**GET** `/health`

Returns the health status of the API.

**Response:**
```json
{
    "status": "healthy",
    "timestamp": "2025-12-06T07:27:53.530067",
    "service": "gdg-api"
}
```

**Example:**
```bash
curl http://localhost:8000/health
```

## 🐳 Docker Configuration

### Dockerfile

The application uses a multi-stage Docker build with:
- Base image: `python:3.12-slim`
- Package manager: `uv` (copied from official image)
- Exposed port: `8000`

### Docker Compose

Features include:
- Automatic restart policy
- Health check monitoring (every 30s)
- Port mapping: `8000:8000`
- Environment variables for Python

### Health Check

The container includes an automatic health check:
- **Interval:** 30 seconds
- **Timeout:** 10 seconds
- **Retries:** 3
- **Start period:** 40 seconds

## 📦 Project Structure

```
GDG/
├── main.py              # FastAPI application
├── pyproject.toml       # Project dependencies
├── Dockerfile           # Docker build configuration
├── docker-compose.yml   # Docker Compose configuration
├── .dockerignore        # Docker build exclusions
├── .gitignore           # Git exclusions
└── README.md            # This file
```

## 🔧 Development

### Adding Dependencies

```bash
# Add a new dependency
uv add <package-name>

# Add a development dependency
uv add --dev <package-name>

# Update dependencies
uv sync
```

### Running Tests

```bash
# Add your test commands here
uv run pytest
```

## 📝 Environment Variables

Currently, no environment variables are required. Future configurations can be added to `docker-compose.yml` under the `environment` section.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is part of the GDG Hackathon.

## 🆘 Troubleshooting

### Container won't start
```bash
# Check logs
docker compose logs api

# Restart the container
docker compose restart api
```

### Port already in use
```bash
# Find process using port 8000
lsof -i :8000

# Kill the process or change the port in docker-compose.yml
```

### Dependencies not installing
```bash
# Clear uv cache
uv cache clean

# Reinstall dependencies
uv sync --reinstall
```

## 📚 Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [uv Documentation](https://github.com/astral-sh/uv)
- [Docker Documentation](https://docs.docker.com/)
