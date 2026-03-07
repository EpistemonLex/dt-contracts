"""Reproduction script."""
import sys

from pydantic import BaseModel, ConfigDict


class SlottedModel(BaseModel):
    model_config = ConfigDict(slots=True)
    x: int

def check_slots():
    m = SlottedModel(x=1)
    print(f"Python version: {sys.version}")

    # Check if __dict__ exists
    try:
        m.__dict__
        print("HAS __dict__")
    except AttributeError:
        print("NO __dict__")

    # Check if __slots__ exists on the class
    if hasattr(SlottedModel, "__slots__"):
        print(f"HAS __slots__: {SlottedModel.__slots__}")
    else:
        print("NO __slots__ on class")

    # Try setting an extra attribute
    try:
        m.y = 2
        print("Managed to set extra attribute 'y'")
    except AttributeError:
        print("FAILED to set extra attribute 'y' (Good for slots)")

if __name__ == "__main__":
    check_slots()
