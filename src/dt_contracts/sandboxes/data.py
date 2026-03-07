"""Contracts for Data Science and Relational sandboxes."""

from pydantic import ConfigDict, Field

from dt_contracts.base import DeepthoughtBaseModel


class DataCell(DeepthoughtBaseModel):
    """A single cell in a data grid."""

    model_config = ConfigDict(slots=True)

    row: int
    col: str
    value: str | float | bool | None
    formula: str | None = None

class DataState(DeepthoughtBaseModel):
    """The state of a relational/data sandbox (Grist/Quadratic)."""

    model_config = ConfigDict(slots=True)

    active_table: str
    modified_cells: list[DataCell] = Field(default_factory=list)
    row_count: int
    col_count: int
