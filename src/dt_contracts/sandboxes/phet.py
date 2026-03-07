"""PhET Interactive Simulation contracts."""

from pydantic import ConfigDict, Field

from dt_contracts.base import DeepthoughtBaseModel


class PhETVariable(DeepthoughtBaseModel):
    """A single observable variable in a PhET simulation."""

    model_config = ConfigDict(slots=True)

    name: str = Field(..., description="e.g. 'gravity', 'mass', 'voltage'")
    value: float | str | bool
    unit: str | None = None

class PhETState(DeepthoughtBaseModel):
    """The full state of a PhET HTML5 simulation."""

    model_config = ConfigDict(slots=True)

    sim_name: str = Field(..., description="Internal PhET ID (e.g. 'gravity-force-lab')")
    variables: list[PhETVariable]
    is_paused: bool = False
