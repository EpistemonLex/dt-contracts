"""Contracts for Mathematical and Geometrical sandboxes."""

from __future__ import annotations

from pydantic import Field

from dt_contracts.base import DeepthoughtBaseModel


class MathEquation(DeepthoughtBaseModel):
    """An equation or expression being manipulated (Mathigon)."""

    id: str
    latex: str
    is_solved: bool = False


class GeometryState(DeepthoughtBaseModel):
    """The state of a geometry simulation (GeoGebra)."""

    points: list[dict[str, float]] = Field(default_factory=list)
    lines: list[dict[str, str]] = Field(default_factory=list)
    active_tool: str = "select"
