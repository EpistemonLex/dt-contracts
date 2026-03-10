"""Tests for the Bridge contracts."""

from __future__ import annotations

from dt_contracts.bridge import Handshake, SyncDirection, SyncManifest


def test_sync_manifest_creation() -> None:
    manifest = SyncManifest(
        batch_id="b1",
        direction=SyncDirection.EDGE_TO_CLOUD,
        count=10,
        checksum="c1",
    )
    assert manifest.batch_id == "b1"
    assert manifest.direction == SyncDirection.EDGE_TO_CLOUD


def test_handshake_creation() -> None:
    hs = Handshake(
        backpack_id="bp1",
        firmware_version="1.0.0",
        current_time="now",
        is_authorized=True,
    )
    assert hs.backpack_id == "bp1"
    assert hs.is_authorized is True
