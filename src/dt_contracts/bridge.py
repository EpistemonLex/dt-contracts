"""Contracts for Ecosystem Bridge and Store-and-Forward Sync."""

from __future__ import annotations

from enum import StrEnum

from .base import DeepthoughtBaseModel


class SyncDirection(StrEnum):
    """Direction of telemetry synchronization."""

    EDGE_TO_CLOUD = "edge_to_cloud"
    CLOUD_TO_EDGE = "cloud_to_edge"


class SyncManifest(DeepthoughtBaseModel):
    """A manifest describing a batch of telemetry being synced."""

    batch_id: str
    direction: SyncDirection
    count: int
    checksum: str


class Handshake(DeepthoughtBaseModel):
    """Initial protocol exchange between Backpack and Core Server."""

    backpack_id: str
    firmware_version: str
    current_time: str
    is_authorized: bool = False
