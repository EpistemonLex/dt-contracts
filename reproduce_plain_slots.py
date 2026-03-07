"""Reproduction script."""
import sys


class PlainSlotted:
    __slots__ = ("x",)
    def __init__(self, x):
        self.x = x

def check_plain():
    m = PlainSlotted(x=1)
    print(f"Python version: {sys.version}")

    # Check if __dict__ exists
    try:
        m.__dict__
        print("HAS __dict__")
    except AttributeError:
        print("NO __dict__")

    # Check if __slots__ exists on the class
    if hasattr(PlainSlotted, "__slots__"):
        print(f"HAS __slots__: {PlainSlotted.__slots__}")
    else:
        print("NO __slots__ on class")

    # Try setting an extra attribute
    try:
        m.y = 2
        print("Managed to set extra attribute 'y'")
    except AttributeError:
        print("FAILED to set extra attribute 'y' (Slots are working)")

if __name__ == "__main__":
    check_plain()
