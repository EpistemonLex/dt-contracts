"""Kaplay.js specific sandbox contracts."""

from pydantic import ConfigDict, Field

from dt_contracts.base import DeepthoughtBaseModel


class KaplayCodeSnapshot(DeepthoughtBaseModel):
    """The current state of the student's JavaScript code."""

    model_config = ConfigDict(slots=True)

    code: str = Field(..., description="The full source code text")
    cursor_line: int | None = None
    cursor_ch: int | None = None

class KaplayCompilationError(DeepthoughtBaseModel):
    """Details of a failed code execution."""

    model_config = ConfigDict(slots=True)

    message: str
    line: int | None = None
    column: int | None = None
    stack: str | None = None

class KaplayGameObject(DeepthoughtBaseModel):
    """Simplified state of an in-game entity."""

    model_config = ConfigDict(slots=True)

    id: int
    tags: list[str]
    pos_x: float
    pos_y: float
    is_paused: bool = False

class KaplayState(DeepthoughtBaseModel):
    """Full snapshot of the Kaplay engine state."""

    model_config = ConfigDict(slots=True)

    objects: list[KaplayGameObject]
    gravity: float
    is_game_over: bool = False
    score: int = 0
