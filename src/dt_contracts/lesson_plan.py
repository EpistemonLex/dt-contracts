from enum import Enum
from typing import List, Optional, Union, Dict, Any
from pydantic import Field
from .base import DeepthoughtBaseModel

class StepKind(str, Enum):
    KOLIBRI_CONSUMPTION = "kolibri_consumption"
    STEAM_SANDBOX = "steam_sandbox"

class SandboxEngine(str, Enum):
    KAPLAY = "kaplay"
    MINETEST = "minetest"
    TURBOWARP = "turbowarp"
    SONIC_PI = "sonic_pi"
    TLDRAW = "tldraw"

class KolibriStep(DeepthoughtBaseModel):
    """Step requiring interaction with Kolibri content."""
    kind: StepKind = StepKind.KOLIBRI_CONSUMPTION
    content_node_id: str = Field(..., description="UUID of the Kolibri content node")
    channel_id: str = Field(..., description="UUID of the Kolibri channel")
    title: str
    transcript: str = Field(..., description="Full text transcript for AI grounding")
    key_vocabulary: List[str] = Field(default_factory=list)

class SandboxStep(DeepthoughtBaseModel):
    """Step requiring active creation in a STEAM sandbox."""
    kind: StepKind = StepKind.STEAM_SANDBOX
    engine: SandboxEngine
    challenge_prompt: str = Field(..., description="The Socratic prompt for the student")
    initial_state: Optional[Dict[str, Any]] = None
    validation_logic: str = Field(..., description="RestrictedPython or JSON logic for success")

class HybridLessonPlan(DeepthoughtBaseModel):
    """The authoritative daily workload contract."""
    plan_id: str
    student_id: str
    title: str
    steps: List[Union[KolibriStep, SandboxStep]]
    metadata: Dict[str, str] = Field(default_factory=dict)
