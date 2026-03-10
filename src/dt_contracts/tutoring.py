"""The Tutoring Orchestration contracts for real-time AI teacher responses."""

from __future__ import annotations

from pydantic import Field

from .base import DeepthoughtBaseModel


class SocraticScript(DeepthoughtBaseModel):
    """A pre-computed pedagogical script from the 70B Core."""

    topic_id: str
    concept_name: str
    primary_analogy: str
    key_points: list[str] = Field(default_factory=list)
    suggested_questions: list[str] = Field(default_factory=list)
    rag_context: str = Field(..., description="Targeted grounding text for the local 0.8B")


class TeacherAction(DeepthoughtBaseModel):
    """A structured response from the local AI Tutor."""

    action_id: str
    response_text: str = Field(..., description="The student-facing message")
    socratic_question: str | None = Field(
        None, description="The pedagogical 'hook' to keep them thinking",
    )
    confidence_score: float = 1.0


class ModelRetry(DeepthoughtBaseModel):
    """Internal contract for correcting malformed local LLM output."""

    validation_error: str = Field(..., description="The Pydantic ValidationError text")
    malformed_output: str = Field(..., description="The raw string that failed validation")
    fix_instruction: str = Field(
        ..., description="Specific system instructions for correcting the output",
    )
