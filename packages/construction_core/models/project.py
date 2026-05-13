"""Project-level domain models."""
from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field


class ProjectInfo(BaseModel):
    """Basic project information for an export package."""

    project_id: str
    project_name: str
    location: str
    contractor: str
    work_type: str
    created_at: datetime
    metadata: dict[str, Any] = Field(default_factory=dict)
