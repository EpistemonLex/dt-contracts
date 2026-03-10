"""The Assessment and RAG contracts for pedagogical grounding."""

from __future__ import annotations

from pydantic import Field

from .base import DeepthoughtBaseModel


class PedagogicalContext(DeepthoughtBaseModel):
    """Container for vector-retrieved Kolibri context."""

    node_id: str
    transcript_segment: str
    source_channel: str
    relevance_score: float


class CognitiveMetric(DeepthoughtBaseModel):
    """A granular metric tracking student performance or affect."""

    metric_id: str
    value: float
    timestamp: str
    metadata: dict[str, str] = Field(default_factory=dict)


class AssessmentResult(DeepthoughtBaseModel):
    """The result of a cognitive assessment pass."""

    student_id: str
    struggle_detected: bool
    reason: str = Field(
        ..., description="An LLM-generated rationale for the struggle points",
    )
    mastery_level: str = Field(
        ..., description="The determined skill level: e.g. beginner, intermediate, advanced",
    )
