"""Contracts for Pedagogical Content and Kolibri Mappings."""

from __future__ import annotations

from enum import StrEnum

from pydantic import Field

from .base import DeepthoughtBaseModel


class KolibriLevel(StrEnum):
    """Developmental tiers for Kolibri content."""

    ELEMENTARY = "elementary"
    MIDDLE = "middle"
    HIGH_SCHOOL = "high_school"


class TopicMapping(DeepthoughtBaseModel):
    """Mapping of a Kolibri topic to Ed-OS S.T.E.A.M. parameters."""

    kolibri_topic_id: str
    target_tier: KolibriLevel
    suggested_sandboxes: list[str] = Field(default_factory=list)
    analogy_prompt: str = Field(..., description="The high-70B precomputed analogy for this topic")


class ContentRequirement(DeepthoughtBaseModel):
    """Explicit requirement for completing a lesson."""

    node_id: str
    min_score: float = 0.0
    required_time_seconds: int = 0
