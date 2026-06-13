"""
app/auth — Canonical Authentication Module.

[Refactoring Note]: 
This module has been refactored using a Domain-Driven Design (Vertical Slicing) approach. 
All authentication logic (Routes, Services, Schemas, Repositories, Security) has been 
consolidated here to prevent cross-team merge conflicts and establish a single source of truth.

Public API (Other services MUST import only from here, never from internal sub-packages):
  auth_router       — FastAPI router, mounted in app/main.py
  get_current_user  — Dependency for any protected endpoint
  get_current_admin — Dependency for admin-only endpoints
"""
from app.auth.api.auth_routes import router as auth_router
from app.auth.security.dependencies import get_current_user, get_current_admin

__all__ = ["auth_router", "get_current_user", "get_current_admin"]
