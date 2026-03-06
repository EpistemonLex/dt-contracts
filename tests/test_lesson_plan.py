"""Tests for the Deepthought lesson plan schemas."""

import pytest
from pydantic import ValidationError

from dt_contracts.lesson_plan import HybridLessonPlan, KolibriStep, SandboxEngine, SandboxStep, StepKind


def test_kolibri_step_creation() -> None:
    """Test creation of a KolibriStep."""
    step = KolibriStep(
        content_node_id="uuid-1",
        channel_id="channel-1",
        title="Test Lesson",
        transcript="Test transcript",
        key_vocabulary=["test"],
    )
    assert step.kind == StepKind.KOLIBRI_CONSUMPTION
    assert step.title == "Test Lesson"

def test_sandbox_step_creation() -> None:
    """Test creation of a SandboxStep."""
    step = SandboxStep(
        engine=SandboxEngine.KAPLAY,
        challenge_prompt="Code something",
        validation_logic="true",
    )
    assert step.kind == StepKind.STEAM_SANDBOX
    assert step.engine == SandboxEngine.KAPLAY

def test_hybrid_lesson_plan_creation() -> None:
    """Test creation of a HybridLessonPlan."""
    kolibri_step = KolibriStep(
        content_node_id="uuid-1",
        channel_id="channel-1",
        title="Lesson 1",
        transcript="Transcript 1",
    )
    sandbox_step = SandboxStep(
        engine=SandboxEngine.KAPLAY,
        challenge_prompt="Challenge 1",
        validation_logic="logic 1",
    )
    plan = HybridLessonPlan(
        plan_id="plan-1",
        student_id="student-1",
        title="My Plan",
        steps=[kolibri_step, sandbox_step],
    )
    assert len(plan.steps) == 2
    assert plan.steps[0].kind == StepKind.KOLIBRI_CONSUMPTION
    assert plan.steps[1].kind == StepKind.STEAM_SANDBOX

def test_memory_sovereignty() -> None:
    """Verify that models use slots and are frozen."""
    kolibri_step = KolibriStep(
        content_node_id="uuid-1",
        channel_id="channel-1",
        title="Test Lesson",
        transcript="Test transcript",
    )

    # Check frozen
    with pytest.raises(ValidationError):
        kolibri_step.title = "New Title"  # type: ignore[misc]

    # Check memory sovereignty configuration
    assert kolibri_step.model_config.get("slots") is True
    assert kolibri_step.model_config.get("frozen") is True
    assert hasattr(kolibri_step, "__slots__")
