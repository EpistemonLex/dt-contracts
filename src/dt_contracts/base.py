from pydantic import BaseModel, ConfigDict

class DeepthoughtBaseModel(BaseModel):
    """Base model enforcing memory efficiency via __slots__."""
    model_config = ConfigDict(
        slots=True,
        frozen=True,
        extra="forbid",
        validate_assignment=True
    )
