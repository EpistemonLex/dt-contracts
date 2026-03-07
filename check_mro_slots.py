"""Reproduction script."""
from pydantic import BaseModel, ConfigDict


class SlottedModel(BaseModel):
    model_config = ConfigDict(slots=True)

print(f"MRO: {SlottedModel.__mro__}")
for cls in SlottedModel.__mro__:
    print(f"Class: {cls}, has __slots__: {hasattr(cls, '__slots__')}")
    if hasattr(cls, "__slots__"):
        print(f"  __slots__: {cls.__slots__}")
    print(f"  has __dict__: {hasattr(cls, '__dict__')}")
