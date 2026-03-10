"""The Hybrid Lesson Plan contracts for offline AI orchestration."""

from __future__ import annotations

from enum import StrEnum

from pydantic import Field

from dt_contracts.sandboxes.base import SandboxType

from .base import DeepthoughtBaseModel

# Deepthought recursive JSON type for initial states
# Literal ANY is strictly forbidden.
type JsonValue = str | int | float | bool | None | list[JsonValue] | dict[str, JsonValue]


class StepKind(StrEnum):
    """Designation for the type of lesson step."""

    KOLIBRI_CONSUMPTION = "kolibri_consumption"
    STEAM_SANDBOX = "steam_sandbox"


class KolibriStep(DeepthoughtBaseModel):
    """Step requiring interaction with Kolibri content."""

    kind: StepKind = StepKind.KOLIBRI_CONSUMPTION
    content_node_id: str = Field(..., description="UUID of the Kolibri content node")
    channel_id: str = Field(..., description="UUID of the Kolibri channel")
    title: str
    transcript: str = Field(..., description="Full text transcript for AI grounding")
    key_vocabulary: list[str] = Field(default_factory=list)


class SandboxStep(DeepthoughtBaseModel):
    """Step requiring active creation in a STEAM sandbox."""

    kind: StepKind = StepKind.STEAM_SANDBOX
    engine: SandboxType
    challenge_prompt: str = Field(..., description="The Socratic prompt for the student")
    initial_state: dict[str, JsonValue] | None = None
    validation_logic: str = Field(..., description="RestrictedPython or JSON logic for success")


class HybridLessonPlan(DeepthoughtBaseModel):
    """The authoritative daily workload contract."""

    plan_id: str
    student_id: str
    title: str
    steps: list[KolibriStep | SandboxStep]
    metadata: dict[str, str] = Field(default_factory=dict)
