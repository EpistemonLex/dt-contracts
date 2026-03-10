"""Tests for the Pedagogy contracts."""

from __future__ import annotations

from dt_contracts.pedagogy import ContentRequirement, KolibriLevel, TopicMapping


def test_topic_mapping_creation() -> None:
    mapping = TopicMapping(
        kolibri_topic_id="gravity",
        target_tier=KolibriLevel.MIDDLE,
        suggested_sandboxes=["minetest"],
        analogy_prompt="Gravity is like a magnet.",
    )
    assert mapping.kolibri_topic_id == "gravity"
    assert mapping.target_tier == KolibriLevel.MIDDLE


def test_content_requirement_creation() -> None:
    req = ContentRequirement(
        node_id="n1",
        min_score=0.8,
        required_time_seconds=300,
    )
    assert req.node_id == "n1"
    assert req.min_score == 0.8
