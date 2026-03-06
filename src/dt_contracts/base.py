"""Base model configurations for the Deepthought contract ecosystem."""

from pydantic import BaseModel, ConfigDict


class DeepthoughtBaseModel(BaseModel):
    """Base model enforcing memory sovereignty and data integrity."""

    model_config = ConfigDict(
        slots=True,  # type: ignore[typeddict-unknown-key]
        frozen=True,
        extra="forbid",
        validate_assignment=True,
    )
