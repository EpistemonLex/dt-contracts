"""Contracts for Student Identity, Mastery, and Cognitive State."""

from enum import StrEnum

from pydantic import ConfigDict, Field

from .base import DeepthoughtBaseModel


class MasteryLevel(StrEnum):
    """The student's proficiency in a specific skill node."""

    UNSEEN = "unseen"
    STRUGGLING = "struggling"
    FAMILIAR = "familiar"
    PROFICIENT = "proficient"
    MASTERED = "mastered"

class SkillMastery(DeepthoughtBaseModel):
    """The current proficiency level for a single knowledge node."""

    model_config = ConfigDict(slots=True)

    node_id: str
    level: MasteryLevel
    confidence: float = Field(..., ge=0.0, le=1.0)
    last_practiced: str | None = None

class CognitiveProfile(DeepthoughtBaseModel):
    """A high-level model of the student's current learning state."""

    model_config = ConfigDict(slots=True)

    student_id: str
    focus_score: float = Field(0.5, description="1.0 = High focus, 0.0 = Distracted")
    struggle_index: float = Field(0.0, description="1.0 = Significant friction, 0.0 = Flow")
    preferred_avatar: str = "Sprocket"
    mastered_nodes: list[str] = Field(default_factory=list)
    recent_telemetry_summary: str | None = None

class StudentProfile(DeepthoughtBaseModel):
    """The authoritative identity and aggregate state of a learner."""

    model_config = ConfigDict(slots=True)

    id: str
    name: str
    grade_level: int | None = None
    cognitive_state: CognitiveProfile
    skill_map: dict[str, SkillMastery] = Field(default_factory=dict)
