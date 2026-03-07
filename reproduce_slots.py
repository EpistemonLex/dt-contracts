"""Reproduction script."""
import sys

from pydantic import BaseModel, ConfigDict


class SlottedModel(BaseModel):
    model_config = ConfigDict(slots=True)
    x: int

def check_slots():
    m = SlottedModel(x=1)
    print(f"Python version: {sys.version}")
    try:
        m.__dict__
        print("HAS __dict__ (NOT slotted)")
    except AttributeError:
        print("NO __dict__ (IS slotted)")

    print(f"Config: {m.model_config}")

if __name__ == "__main__":
    check_slots()
