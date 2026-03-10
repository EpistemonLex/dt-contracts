"""The Telemetry schema for logging micro-actions and semantically dense summaries."""

from __future__ import annotations

from enum import StrEnum
from typing import Any

from pydantic import Field

from dt_contracts.sandboxes.base import SandboxType, TelemetryLevel

from .base import DeepthoughtBaseModel


class CompetencyLevel(StrEnum):
    """Pedagogical mastery levels for a given topic."""

    NONE = "none"
    FAILED = "failed"
    ATTEMPTED = "attempted"
    MASTERED = "mastered"


class LogEntryType(StrEnum):
    """The source or nature of a raw log entry."""

    SANDBOX = "sandbox"
    TUTOR_SPEECH = "tutor_speech"
    STUDENT_UTTERANCE = "student_utterance"
    SYSTEM_ERROR = "system_error"


class SandboxRawPayload(DeepthoughtBaseModel):
    """Standardized payload for raw sandbox events in the ledger."""

    sandbox_type: SandboxType
    event_name: str
    payload: dict[str, Any] = Field(default_factory=dict) # architectural: allowed-any (Engine Payload)
    level: TelemetryLevel = TelemetryLevel.INFO


class RawLogEntry(DeepthoughtBaseModel):
    """A single 'thin' event recorded in the local hot-table."""

    timestamp: str
    entry_type: LogEntryType
    payload: dict[str, Any] = Field(default_factory=dict) # architectural: allowed-any (Heterogeneous Payload)


class CognitiveAssessment(DeepthoughtBaseModel):
    """AI enrichment explaining the student's logic and struggle."""

    frustration_index: float = Field(0.0, ge=0.0, le=1.0)
    intervention_held: bool = False
    socratic_summary: str = Field(..., description="Teacher-readable note on the outcome")


class MasterySignal(DeepthoughtBaseModel):
    """Mapping of the interaction back to the Kolibri Topic Tree."""

    kolibri_topic_id: str
    competency: CompetencyLevel = CompetencyLevel.NONE
    next_logical_unlock: str | None = None


class SemanticallyDenseSummary(DeepthoughtBaseModel):
    """A 5-minute flight recorder snapshot of the student's learning arc."""

    summary_id: str
    start_time: str
    end_time: str

    # Enrichment
    assessment: CognitiveAssessment
    mastery: MasterySignal

    # Compressed context (Optional: sample of crucial raw logs for human auditing)
    context_samples: list[RawLogEntry] = Field(default_factory=list)


# Legacy Support (Keep until all refactors complete)
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
    details: dict[str, Any] | None = Field( # architectural: allowed-any
        default=None, description="Structured payload details",
    ) # architectural: allowed-any (Legacy Support)
