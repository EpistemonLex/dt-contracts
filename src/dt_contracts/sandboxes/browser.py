"""Contracts for the Chrome Pedagogical Nanny (Digital Curiosity)."""

from __future__ import annotations

from pydantic import Field

from dt_contracts.base import DeepthoughtBaseModel


class BrowserCuriosity(DeepthoughtBaseModel):
    """Telemetry captured when a student explores the 'Wild' web."""

    type: str = Field(..., description="e.g. 'PAGE_VISIT', 'SEARCH_QUERY'")
    title: str = Field(..., description="The title of the page or the query string")
    url: str = Field(..., description="The full URL of the visited resource")
    timestamp: str = Field(..., description="ISO 8601 timestamp from the browser")

    # Enrichment
    derived_keywords: list[str] = Field(default_factory=list, description="NLP-extracted topics of interest")
