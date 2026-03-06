"""The Topological Mapping contracts for the Kolibri Topic Tree."""

from enum import StrEnum

from pydantic import Field

from .base import DeepthoughtBaseModel


class NodeKind(StrEnum):
    """The type of a ContentNode in the Kolibri hierarchy."""

    TOPIC = "topic"
    VIDEO = "video"
    EXERCISE = "exercise"
    AUDIO = "audio"
    DOCUMENT = "document"
    HTML5 = "html5"


class ContentNodeRecord(DeepthoughtBaseModel):
    """A flattened record for a single educational node in the graph."""

    node_id: str = Field(..., description="The ContentNode_ID from Kolibri")
    kind: NodeKind
    title: str = Field(..., description="The human-readable title of the content")
    channel_id: str = Field(..., description="The ID of the source channel (e.g. Khan Academy)")
    metadata: dict[str, str] = Field(
        default_factory=dict, description="Additional context for the node",
    )


class PrerequisiteLink(DeepthoughtBaseModel):
    """A link defining a prerequisite relationship between two nodes."""

    required_node_id: str = Field(..., description="The node that must be completed")
    target_node_id: str = Field(..., description="The node that is unlocked")


class KolibriHierarchy(DeepthoughtBaseModel):
    """A recursive structure defining a portion of the curriculum graph."""

    node_id: str = Field(..., description="The ID of the parent topic node")
    title: str = Field(..., description="The title of the topic")
    children: list[KolibriHierarchy | ContentNodeRecord] = Field(
        default_factory=list, description="The nested children of this topic",
    )
    metadata: dict[str, str] = Field(
        default_factory=dict, description="Additional context for the hierarchy",
    )
