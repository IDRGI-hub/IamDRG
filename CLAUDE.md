# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a FastAPI-based personal resume/portfolio website (IamDRG) with the following architecture:
- **FastAPI backend** serving HTML templates with Jinja2
- **PostgreSQL database** for data persistence
- **Nginx reverse proxy** with SSL/TLS termination
- **Docker containerization** with multi-service setup
- **Static assets** (images, icons) served through FastAPI

The site features dark/light theme toggle and uses Tailwind CSS with JetBrains Mono font.

## Development Commands

### Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Run FastAPI development server
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### Docker Development
```bash
# Build and run all services (app, database, nginx, certbot)
docker-compose up --build

# Run in background
docker-compose up -d

# View logs
docker-compose logs -f app

# Stop services
docker-compose down

# Rebuild specific service
docker-compose build app
docker-compose up app
```

### Database Operations
```bash
# Access PostgreSQL container
docker exec -it resume_db psql -U resume_user -d resume_db

# View database logs
docker-compose logs -f db
```

## Architecture Details

### File Structure
- `/app/main.py` - FastAPI application entry point
- `/app/templates/` - Jinja2 HTML templates
- `/app/static/` - Static assets (images, icons)
- `/nginx/default.conf` - Nginx configuration with SSL
- `/docker-compose.yml` - Multi-service container orchestration
- `/requirements.txt` - Python dependencies (FastAPI, Jinja2, uvicorn, SQLAlchemy, asyncpg)

### Services Architecture
1. **App Container** (port 8000) - FastAPI application
2. **Database Container** - PostgreSQL 16 with persistent volume
3. **Nginx Container** (ports 80/443) - Reverse proxy with SSL termination
4. **Certbot Container** - SSL certificate management

### Theme System
The site implements a JavaScript-based theme switcher with CSS custom properties for dark/light modes. Theme state is managed through the `data-theme` attribute on the HTML element.

### Domain Configuration
Production domain: `ruvpnservice.ru` (configured in nginx)
SSL certificates managed via Let's Encrypt/Certbot

## Database Schema
Uses SQLAlchemy ORM with asyncpg driver for PostgreSQL connectivity. Database credentials are configured in docker-compose environment variables.