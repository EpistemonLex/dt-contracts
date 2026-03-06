"""The Telemetry schema for logging micro-actions on the Edge."""

from enum import StrEnum

from pydantic import Field

from .base import DeepthoughtBaseModel
from .lesson_plan import JsonValue


class ActionType(StrEnum):
    """Designation for the type of logged action."""

    VIDEO_PAUSE = "video_pause"
    CODE_EDIT = "code_edit"
    COMPILATION_ERROR = "compilation_error"
    UI_INTERACTION = "ui_interaction"


class TelemetryLog(DeepthoughtBaseModel):
    """Schema for micro-actions logged on the Edge."""

    student_id: str = Field(..., description="UUID of the student")
    action_type: ActionType
    timestamp: str = Field(..., description="ISO 8601 timestamp of the action")
    details: dict[str, JsonValue] | None = Field(
        default=None, description="Structured payload details",
    )
