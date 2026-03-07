"""Contracts for Music and Algorithmic Sound sandboxes."""

from pydantic import ConfigDict, Field

from dt_contracts.base import DeepthoughtBaseModel


class MusicalNote(DeepthoughtBaseModel):
    """A single note or event in a sequence."""

    model_config = ConfigDict(slots=True)

    pitch: str  # e.g. 'C4'
    duration: float
    velocity: float = 0.8

class MusicState(DeepthoughtBaseModel):
    """The overall state of a music composition (BeepBox/Strudel)."""

    model_config = ConfigDict(slots=True)

    bpm: float
    key: str
    tracks_count: int
    active_pattern: list[MusicalNote] = Field(default_factory=list)
