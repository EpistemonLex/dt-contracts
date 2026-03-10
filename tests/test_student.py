"""Tests for the Student contracts."""

from __future__ import annotations

from dt_contracts.student import (
    CognitiveProfile,
    MasteryLevel,
    SkillMastery,
    StudentProfile,
)


def test_student_profile_creation() -> None:
    skill = SkillMastery(
        topic_id="math-1",
        level=MasteryLevel.EXPLORER,
        last_accessed="2026-03-09",
    )
    profile = StudentProfile(
        id="stu-1",
        name="Alice",
        cognitive_state=CognitiveProfile(attention_span=0.8),
        skill_map={"math-1": skill},
    )
    assert profile.name == "Alice"
    assert profile.skill_map["math-1"].level == MasteryLevel.EXPLORER
