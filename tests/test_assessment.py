"""Tests for the Deepthought assessment and RAG schemas."""

import pytest
from pydantic import ValidationError

from dt_contracts.assessment import CognitiveMetric, PedagogicalContext


def test_pedagogical_context_creation() -> None:
    """Test standard creation of a PedagogicalContext container."""
    context = PedagogicalContext(
        source_id="kolibri-node-1",
        transcript_chunks=[
            "The lift equation is L = 1/2 * rho * v^2 * S * Cl.",
            "Rho represents air density at a given altitude.",
        ],
        key_terms={"rho": "Air density", "v": "Velocity"},
    )
    assert context.source_id == "kolibri-node-1"
    assert len(context.transcript_chunks) == 2
    assert context.key_terms["rho"] == "Air density"


def test_cognitive_metric_creation() -> None:
    """Test creation of a student struggle metric."""
    metric = CognitiveMetric(
        student_id="stu-123",
        topic_id="physics-lift",
        struggle_score=0.75,
        struggle_reason="Repeated syntax errors in lift coefficient assignment.",
        mastery_level="intermediate",
    )
    assert metric.struggle_score == 0.75
    assert metric.mastery_level == "intermediate"


def test_assessment_memory_sovereignty() -> None:
    """Verify that assessment models are frozen."""
    metric = CognitiveMetric(
        student_id="stu-1",
        topic_id="top-1",
        struggle_score=0.1,
        struggle_reason="none",
        mastery_level="beginner",
    )

    assert metric.model_config.get("frozen") is True

    with pytest.raises(ValidationError):
        metric.__setattr__("struggle_score", 0.9)
