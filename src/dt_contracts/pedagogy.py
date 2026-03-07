"""Contracts for Pedagogical Content and Kolibri Mappings."""

from enum import StrEnum

from pydantic import ConfigDict, Field

from .base import DeepthoughtBaseModel


class ContentKind(StrEnum):
    """Types of educational content."""

    TOPIC = "topic"
    VIDEO = "video"
    EXERCISE = "exercise"
    DOCUMENT = "document"
    HTML5 = "html5"

class KnowledgeNode(DeepthoughtBaseModel):
    """A single node in the pedagogical knowledge graph."""

    model_config = ConfigDict(slots=True)

    id: str = Field(..., description="The unique Kolibri ContentNode ID")
    title: str
    description: str | None = None
    kind: ContentKind
    channel_id: str
    tags: list[str] = Field(default_factory=list)
    metadata: dict[str, object] = Field(default_factory=dict) # architectural: allowed-object (Engine-specific meta)

class TranscriptChunk(DeepthoughtBaseModel):
    """A semantically cohesive block of text from a video transcript."""

    model_config = ConfigDict(slots=True)

    node_id: str
    content: str = Field(..., description="The raw transcript text")
    start_time: float | None = None
    end_time: float | None = None
    vector_id: str | None = Field(None, description="The ID in the LanceDB vector store")

class Prerequisite(DeepthoughtBaseModel):
    """A directed edge in the knowledge graph representing dependency."""

    model_config = ConfigDict(slots=True)

    target_id: str = Field(..., description="The node that requires completion")
    required_id: str = Field(..., description="The dependency node")
    priority: int = 1  # 1 = hard prerequisite, 2 = recommended
