"""Contracts for Data Science and Relational sandboxes."""

from __future__ import annotations

from pydantic import Field

from dt_contracts.base import DeepthoughtBaseModel


class NotebookCell(DeepthoughtBaseModel):
    """A single cell in a literate notebook (Starboard)."""

    cell_id: str
    cell_type: str = Field(..., description="e.g. 'code', 'markdown'")
    content: str
    execution_count: int = 0


class DataState(DeepthoughtBaseModel):
    """Snapshot of a data science environment."""

    cells: list[NotebookCell]
    active_dataset: str | None = None
    variables: dict[str, str] = Field(default_factory=dict)
