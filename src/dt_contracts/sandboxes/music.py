"""Contracts for Music and Algorithmic Sound sandboxes."""

from __future__ import annotations

from pydantic import Field

from dt_contracts.base import DeepthoughtBaseModel


class MusicPattern(DeepthoughtBaseModel):
    """A musical sequence (Strudel/BeepBox)."""

    id: str
    notation: str = Field(..., description="e.g. TidalCycles or ABC notation")
    tempo_bpm: float = 120.0


class AudioState(DeepthoughtBaseModel):
    """State of an audio editing or synthesis session."""

    active_tracks: int = 1
    sample_rate: int = 44100
    is_playing: bool = False
