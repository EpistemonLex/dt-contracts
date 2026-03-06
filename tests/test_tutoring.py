"""Tests for the Deepthought tutoring orchestration schemas."""

import pytest
from pydantic import ValidationError

from dt_contracts.tutoring import ModelRetry, TeacherAction


def test_teacher_action_creation() -> None:
    """Test standard creation of a TeacherAction."""
    action = TeacherAction(
        action_id="act-123",
        response_text="Great work on the lift equation! What happens if we double the velocity?",
        socratic_question="What happens if we double the velocity?",
        confidence_score=0.95,
    )
    assert action.action_id == "act-123"
    assert action.confidence_score == 0.95


def test_teacher_action_with_ui_trigger() -> None:
    """Test creation with UI triggers and code hints."""
    action = TeacherAction(
        action_id="act-456",
        response_text="Look at the wind tunnel visualization.",
        ui_trigger="start_smoke_animation",
        code_hint="Check your lift_coefficient variable assignment.",
        confidence_score=0.88,
    )
    assert action.ui_trigger == "start_smoke_animation"
    assert "lift_coefficient" in str(action.code_hint)


def test_model_retry_creation() -> None:
    """Test creation of a ModelRetry feedback payload."""
    retry = ModelRetry(
        error_message="Field 'action_id' is missing",
        malformed_output='{"response_text": "hello"}',
        fix_instruction="Please include the required 'action_id' UUID.",
    )
    assert "missing" in retry.error_message
    assert "UUID" in retry.fix_instruction


def test_tutoring_memory_sovereignty() -> None:
    """Verify that tutoring models are frozen and adhere to DeepthoughtBaseModel."""
    action = TeacherAction(
        action_id="act-123",
        response_text="Test",
        confidence_score=1.0,
    )

    # Check memory sovereignty configuration
    assert action.model_config.get("frozen") is True

    # Check frozen mutation rejection
    with pytest.raises(ValidationError):
        action.__setattr__("confidence_score", 0.0)
