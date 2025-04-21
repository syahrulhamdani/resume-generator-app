# resume-generator-app

[![Build and Deploy to Cloud Run](https://github.com/syahrulhamdani/resume-generator-app/actions/workflows/cloudrun.yml/badge.svg?branch=main&event=push)](https://github.com/syahrulhamdani/resume-generator-app/actions/workflows/cloudrun.yml)

A FastAPI-based service for generating PDF resumes from structured JSON data.

## Prerequisites

To set up the development environment, you need:

- Python 3.12 or higher
- [pyenv](https://github.com/pyenv/pyenv) (for Python version management)
- [Poetry](https://python-poetry.org/) (for dependency management)

## Repository Structure

```bash
resume-generator-app/
├── .github/            # GitHub Actions workflows
│ └── workflows/        # CI/CD pipeline configurations
├── app/                # Main application code
│ ├── api/              # API routes and endpoints
│ │ ├── v1/             # API version 1
│ │ │ └── endpoints/    # API endpoint implementations
│ ├── core/             # Core functionality (config, logging)
│ ├── models/           # Data models and schemas
│ └── services/         # Business logic services
├── tests/              # Test suite
├── Dockerfile          # Container definition
├── pyproject.toml      # Project dependencies and configuration
└── README.md           # Project documentation
```

## API Endpoints

- `/`: API information
- `/health`: Health check endpoint
- `/resume/generate`: Generate a PDF resume (POST)

## Deployment

The application is set up for deployment to Google Cloud Run via GitHub Actions.
Pushes to the main branch will trigger automatic builds and deployments.
