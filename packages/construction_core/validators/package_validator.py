"""Package validator helpers."""
from __future__ import annotations

from packages.construction_core.models.export_package import ExportPackage


def validate_export_package(package: ExportPackage) -> bool:
    """Basic placeholder validator for package object shape."""
    return bool(package.package_id and package.project_info.project_id)
