"""Tests for the Deepthought assessment and RAG schemas."""

from __future__ import annotations

import pytest
from pydantic import ValidationError

from dt_contracts.assessment import CognitiveMetric, PedagogicalContext


def test_pedagogical_context_creation() -> None:
    """Test standard creation of a PedagogicalContext container."""
    context = PedagogicalContext(
        node_id="kolibri-node-1",
        transcript_segment="The lift equation is L = 1/2 * rho * v^2 * S * Cl.",
        source_channel="physics-101",
        relevance_score=0.95,
    )
    assert context.node_id == "kolibri-node-1"
    assert "lift equation" in context.transcript_segment


def test_cognitive_metric_creation() -> None:
    """Test creation of a student cognitive metric."""
    metric = CognitiveMetric(
        metric_id="m-123",
        value=0.75,
        timestamp="2026-03-09T10:00:00Z",
        metadata={"topic": "physics-lift"},
    )
    assert metric.value == 0.75
    assert metric.metadata["topic"] == "physics-lift"


def test_assessment_memory_sovereignty() -> None:
    """Verify that assessment models are frozen."""
    metric = CognitiveMetric(
        metric_id="m-1",
        value=0.1,
        timestamp="2026-03-09T10:00:00Z",
    )

    assert metric.model_config.get("frozen") is True

    with pytest.raises(ValidationError):
        metric.__setattr__("value", 0.9)
