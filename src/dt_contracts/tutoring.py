"""The Tutoring Orchestration contracts for real-time AI teacher responses."""

from pydantic import ConfigDict, Field

from .base import DeepthoughtBaseModel


class SocraticScript(DeepthoughtBaseModel):
    """A pre-computed pedagogical blueprint for a specific topic (The Script)."""

    model_config = ConfigDict(slots=True)

    topic_id: str = Field(..., description="Kolibri ContentNode_ID")
    concept_name: str
    primary_analogy: str = Field(..., description="e.g. The Wonderland analogy")
    key_points: list[str] = Field(default_factory=list)
    suggested_questions: list[str] = Field(default_factory=list)
    rag_context: str = Field(..., description="Ground truth transcript text")


class TeacherAction(DeepthoughtBaseModel):
    """The primary response contract for the AI Tutor."""

    action_id: str = Field(..., description="A unique UUID for the tutoring event")
    response_text: str = Field(
        ..., description="The main spoken/displayed response to the student",
    )
    socratic_question: str | None = Field(
        default=None, description="A targeted question to prompt student inquiry",
    )
    code_hint: str | None = Field(
        default=None, description="Specific debugging guidance for S.T.E.A.M. challenges",
    )
    ui_trigger: str | None = Field(
        default=None, description="A specific frontend event identifier",
    )
    confidence_score: float = Field(
        ..., description="The model's self-assessed confidence in the pedagogical response",
    )


class ModelRetry(DeepthoughtBaseModel):
    """Feedback payload for the self-healing AI validation loop."""

    error_message: str = Field(..., description="The Pydantic ValidationError text")
    malformed_output: str = Field(..., description="The raw string that failed validation")
    fix_instruction: str = Field(
        ..., description="Specific system instructions for correcting the output",
    )
