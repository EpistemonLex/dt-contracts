"""Contracts for Design, Art, and Visual Thinking sandboxes."""

from __future__ import annotations

from pydantic import Field

from dt_contracts.base import DeepthoughtBaseModel


class CanvasShape(DeepthoughtBaseModel):
    """A shape or sketch on a canvas."""

    id: str
    type: str = Field(..., description="e.g. 'arrow', 'box', 'scribble'")
    bounds_x: float
    bounds_y: float
    text: str | None = None

class DesignState(DeepthoughtBaseModel):
    """The state of a visual thinking canvas (tldraw)."""

    shapes: list[CanvasShape]
    active_tool: str
    camera_zoom: float = 1.0
