"""Tests for various Sandbox engine-specific contracts."""

from __future__ import annotations

from dt_contracts.sandboxes.actions import KaplayAction, MinetestAction, SnapAction
from dt_contracts.sandboxes.browser import BrowserCuriosity
from dt_contracts.sandboxes.chemistry import ChemistryLabState, SandboxelsReaction
from dt_contracts.sandboxes.data import DataState, NotebookCell
from dt_contracts.sandboxes.design import CanvasShape, DesignState
from dt_contracts.sandboxes.electronics import CircuitComponent, ElectronicsState
from dt_contracts.sandboxes.kaplay import KaplayEvent, KaplaySprite, KaplayState, Vector2
from dt_contracts.sandboxes.math import GeometryState, MathEquation
from dt_contracts.sandboxes.minetest import MinetestEvent, MinetestState, VoxelPosition
from dt_contracts.sandboxes.music import AudioState, MusicPattern
from dt_contracts.sandboxes.phet import PhetState, PhetVariable
from dt_contracts.sandboxes.snap import SnapBlock, SnapSprite, SnapState


def test_sandbox_actions() -> None:
    ka = KaplayAction(action_type="spawn", entity_id="e1")
    assert ka.action_type == "spawn"

    ma = MinetestAction(action_type="set_node", pos=[1, 2, 3])
    assert ma.pos == [1, 2, 3]

    sa = SnapAction(action_type="say", message="hello")
    assert sa.message == "hello"


def test_browser_curiosity() -> None:
    bc = BrowserCuriosity(type="visit", title="T1", url="http://u1", timestamp="now")
    assert bc.title == "T1"


def test_chemistry_models() -> None:
    sr = SandboxelsReaction(element_a="a", element_b="b", result_element="c", pos_x=1, pos_y=2)
    assert sr.result_element == "c"

    cl = ChemistryLabState(beakers=[{"id": "b1"}], total_volume_ml=100.0)
    assert len(cl.beakers) == 1


def test_data_models() -> None:
    nc = NotebookCell(cell_id="c1", cell_type="code", content="print(1)")
    assert nc.cell_id == "c1"

    ds = DataState(cells=[nc], variables={"x": "1"})
    assert len(ds.cells) == 1


def test_design_models() -> None:
    cs = CanvasShape(id="s1", type="box", bounds_x=10, bounds_y=20)
    assert cs.id == "s1"

    ds = DesignState(shapes=[cs], active_tool="draw")
    assert ds.active_tool == "draw"


def test_electronics_models() -> None:
    cc = CircuitComponent(id="c1", type="resistor", value=100)
    assert cc.value == 100

    es = ElectronicsState(components=[cc], is_simulating=True)
    assert es.is_simulating is True


def test_kaplay_models() -> None:
    v2 = Vector2(x=1, y=2)
    ks = KaplaySprite(id="s1", tags=["player"], pos=v2)
    state = KaplayState(sprites=[ks], score=10)
    assert state.score == 10

    ev = KaplayEvent(event_type="hit", actor_id="a1", payload={"damage": 10})
    assert ev.payload["damage"] == 10


def test_math_models() -> None:
    me = MathEquation(id="e1", latex="x+1=2", is_solved=True)
    assert me.is_solved is True

    gs = GeometryState(points=[{"x": 1.0, "y": 2.0}], active_tool="point")
    assert len(gs.points) == 1


def test_minetest_models() -> None:
    vp = VoxelPosition(x=1, y=2, z=3)
    ev = MinetestEvent(event_name="placed", player_name="alice", pos=vp)
    assert ev.player_name == "alice"

    ms = MinetestState(player_pos=vp, player_hp=20, inventory_count=5, active_mod_version="1.0")
    assert ms.player_hp == 20


def test_music_models() -> None:
    mp = MusicPattern(id="p1", notation="C D E")
    assert mp.notation == "C D E"

    as_ = AudioState(active_tracks=2, is_playing=True)
    assert as_.is_playing is True


def test_phet_models() -> None:
    pv = PhetVariable(name="v1", value=10.5)
    ps = PhetState(sim_id="s1", variables=[pv])
    assert ps.sim_id == "s1"


def test_snap_models() -> None:
    sb = SnapBlock(id="b1", selector="move", parameters=[10])
    assert sb.selector == "move"
    ss = SnapSprite(name="s1", scripts_count=1, costume_name="c1", pos_x=0, pos_y=0)
    state = SnapState(project_name="p1", sprites=[ss], variables={"v1": 1})
    assert state.project_name == "p1"
