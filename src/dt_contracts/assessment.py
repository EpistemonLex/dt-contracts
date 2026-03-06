"""The Assessment and RAG contracts for pedagogical grounding."""

from pydantic import Field

from .base import DeepthoughtBaseModel


class PedagogicalContext(DeepthoughtBaseModel):
    """Container for vector-retrieved Kolibri context to ground the AI Tutor."""

    source_id: str = Field(..., description="The ContentNode_ID of the source material")
    transcript_chunks: list[str] = Field(
        ..., description="Semantically cohesive blocks of video transcript text",
    )
    key_terms: dict[str, str] = Field(
        default_factory=dict, description="A mapping of vocabulary terms to their definitions",
    )
    metadata: dict[str, str] = Field(
        default_factory=dict, description="Additional context for the RAG process",
    )


class CognitiveMetric(DeepthoughtBaseModel):
    """Summary of student struggle points and mastery levels."""

    student_id: str = Field(..., description="UUID of the student")
    topic_id: str = Field(..., description="The ID of the educational topic being assessed")
    struggle_score: float = Field(
        ...,
        description="A value between 0 and 1 representing the student's level of difficulty",
    )
    struggle_reason: str = Field(
        ..., description="An LLM-generated rationale for the struggle points",
    )
    mastery_level: str = Field(
        ..., description="The determined skill level: e.g. beginner, intermediate, advanced",
    )
