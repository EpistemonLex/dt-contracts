"""Contracts for Student Identity, Mastery, and Cognitive State."""

from __future__ import annotations

from enum import StrEnum

from pydantic import Field

from .base import DeepthoughtBaseModel


class MasteryLevel(StrEnum):
    """The student's level of understanding for a specific concept."""

    NOVICE = "novice"
    EXPLORER = "explorer"
    ARCHITECT = "architect"
    MASTER = "master"


class SkillMastery(DeepthoughtBaseModel):
    """The student's mastery of a specific skill or topic."""

    topic_id: str
    level: MasteryLevel
    last_accessed: str
    confidence_score: float = 0.0


class CognitiveProfile(DeepthoughtBaseModel):
    """Current mental and emotional state of a learner."""

    attention_span: float = 1.0
    frustration_level: float = 0.0
    active_sandbox_id: str | None = None


class StudentProfile(DeepthoughtBaseModel):
    """The authoritative state of a learner."""

    id: str
    name: str
    grade_level: int | None = None
    cognitive_state: CognitiveProfile
    skill_map: dict[str, SkillMastery] = Field(default_factory=dict)
