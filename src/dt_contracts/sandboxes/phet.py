"""Contracts for PhET Interactive Simulations."""

from pydantic import ConfigDict, Field
from .base import DeepthoughtBaseModel

class PhetVariable(DeepthoughtBaseModel):
    """A granular variable from a PhET simulation state."""
    model_config = ConfigDict(slots=True)
    
    name: str = Field(..., description="The internal name of the PhET property")
    value: float | str | bool
    units: str | None = None

class PhetState(DeepthoughtBaseModel):
    """The high-fidelity state of a PhET simulation."""
    model_config = ConfigDict(slots=True)
    
    sim_id: str = Field(..., description="The unique PhET simulation identifier")
    variables: list[PhetVariable] = Field(default_factory=list)
    timestamp: str
