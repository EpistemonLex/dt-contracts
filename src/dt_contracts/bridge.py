"""Contracts for Ecosystem Bridge and Store-and-Forward Sync."""

from enum import StrEnum

from pydantic import ConfigDict

from .base import DeepthoughtBaseModel


class SyncDirection(StrEnum):
    """Direction of data flow during a bridge session."""

    UPLOAD = "upload"      # Backpack -> Core
    DOWNLOAD = "download"  # Core -> Backpack

class SyncResource(StrEnum):
    """Types of resources that can be synchronized."""

    LESSON_PLAN = "lesson_plan"
    TELEMETRY = "telemetry"
    STUDENT_PROFILE = "student_profile"
    KNOWLEDGE_GRAPH = "knowledge_graph"
    MEDIA_ASSET = "media_asset"

class SyncManifest(DeepthoughtBaseModel):
    """The batch manifest representing a collection of resources to sync."""

    model_config = ConfigDict(slots=True)

    session_id: str
    direction: SyncDirection
    resources: list[SyncResource]
    total_size_bytes: int
    checksum: str

class Handshake(DeepthoughtBaseModel):
    """Initial protocol exchange between Backpack and Core Server."""

    model_config = ConfigDict(slots=True)

    backpack_id: str
    firmware_version: str
    current_time: str
    is_authorized: bool = False
