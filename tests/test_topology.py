"""Tests for the Deepthought topological mapping schemas."""

import pytest
from pydantic import ValidationError

from dt_contracts.topology import ContentNodeRecord, KolibriHierarchy, NodeKind, PrerequisiteLink


def test_content_node_record_creation() -> None:
    """Test standard creation of a ContentNodeRecord."""
    node = ContentNodeRecord(
        node_id="kolibri-123",
        kind=NodeKind.VIDEO,
        title="Intro to Aerodynamics",
        channel_id="physics-channel",
    )
    assert node.node_id == "kolibri-123"
    assert node.kind == NodeKind.VIDEO


def test_prerequisite_link_creation() -> None:
    """Test creation of a prerequisite relationship."""
    link = PrerequisiteLink(
        required_node_id="math-101",
        target_node_id="physics-201",
    )
    assert link.required_node_id == "math-101"


def test_kolibri_hierarchy_recursion() -> None:
    """Test the recursive structure of the topic tree."""
    lesson = ContentNodeRecord(
        node_id="lesson-1",
        kind=NodeKind.EXERCISE,
        title="Practice Problems",
        channel_id="c1",
    )

    sub_topic = KolibriHierarchy(
        node_id="sub-1",
        title="Sub Topic",
        children=[lesson],
    )

    root = KolibriHierarchy(
        node_id="root-1",
        title="Root Topic",
        children=[sub_topic],
    )

    assert len(root.children) == 1
    # Check that children can be either further hierarchies or flat records
    assert isinstance(root.children[0], KolibriHierarchy)
    assert isinstance(sub_topic.children[0], ContentNodeRecord)


def test_topology_memory_sovereignty() -> None:
    """Verify that topology models are frozen."""
    node = ContentNodeRecord(
        node_id="id",
        kind=NodeKind.TOPIC,
        title="Title",
        channel_id="ch",
    )

    assert node.model_config.get("frozen") is True

    with pytest.raises(ValidationError):
        node.__setattr__("title", "New")
