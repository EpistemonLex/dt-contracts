"""Contracts for Chemistry and Emergent Physics (Sandboxels)."""

from pydantic import ConfigDict, Field
from .base import DeepthoughtBaseModel

class SandboxelsReaction(DeepthoughtBaseModel):
    """An emergent reaction detected in the Sandboxels grid."""
    model_config = ConfigDict(slots=True)
    
    element1: str
    element2: str
    result: str
    pos_x: int
    pos_y: int

class SandboxelsState(DeepthoughtBaseModel):
    """The granular state of the Sandboxels cellular automata grid."""
    model_config = ConfigDict(slots=True)
    
    element_counts: dict[str, int] = Field(..., description="Count of each element type currently in the grid")
    active_reactions: list[SandboxelsReaction] = Field(default_factory=list)
    timestamp: str

class ChemistryState(DeepthoughtBaseModel):
    """Standard chemistry lab state (e.g. ChemCollective)."""
    model_config = ConfigDict(slots=True)
    
    beakers: list[dict[str, object]] = Field(default_factory=list)
    total_volume_ml: float = 0.0
