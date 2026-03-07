"""Reproduction script."""
import sys

from pydantic import BaseModel, ConfigDict


class StrictModel(BaseModel):
    model_config = ConfigDict(
        slots=True,
        frozen=True,
        extra="forbid",
    )
    x: int

def check_strict():
    m = StrictModel(x=1)
    print(f"Python version: {sys.version}")

    # Check if __dict__ exists
    try:
        m.__dict__
        print("HAS __dict__")
    except AttributeError:
        print("NO __dict__")

    # Check if __slots__ exists on the class
    if hasattr(StrictModel, "__slots__"):
        print(f"HAS __slots__: {StrictModel.__slots__}")
    else:
        print("NO __slots__ on class")

    # Try setting an extra attribute
    try:
        m.y = 2
        print("Managed to set extra attribute 'y'")
    except Exception as e:
        print(f"FAILED to set extra attribute 'y' ({type(e).__name__}: {e})")

if __name__ == "__main__":
    check_strict()
