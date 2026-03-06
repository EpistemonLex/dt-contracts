# Deepthought OS: Sovereign Contracts Blueprint (V1.0)

## 1. Vision: The Immutable Ground Truth
The `dt-contracts` repository (internally referred to as the **Sovereign Schema Repository**) serves as the mathematical and structural backbone of the Deepthought Educational OS. In an environment defined by broadband asymmetry and edge-first execution, data integrity is not a preference—it is a survival mandate. 

This repository centralizes all Pydantic V2 models that define how data flows between the **Principal** (Core Server), the **Foreman** (Factory Forge), and the **Backpack** (Edge Teacher). By decoupling schemas from implementation, we ensure that a 0.8B parameter model on a Chromebook speaks the exact same "language" as a Mac Studio in the district office.

## 2. The Three Pillars of Data Sovereignty

### I. Zero-Any Vacuum
To prevent runtime type-confusion and "silent failures" in the AI orchestration loop, the use of `Any` is strictly forbidden. All dynamic payloads must be modeled using recursive type aliases (e.g., `JsonValue`) or explicit `Union` types.

### II. Memory Sovereignty (__slots__)
Edge devices (Chromebooks/Tablets) operate in a "RAM-starved" state. 
- All models must enforce `ConfigDict(slots=True, frozen=True)`.
- This micro-optimization reduces object memory overhead by ~2.5x, preventing the local FastAPI daemon from triggering OOM (Out-of-Memory) events during high-frequency telemetry logging.

### III. Self-Healing Orchestration
Small LLMs (Qwen 0.8B) are prone to syntax errors. These contracts provide the "Prompted Output" schemas for `pydantic-ai`, allowing the system to automatically trap validation errors and force model retries with specific error feedback.

---

## 3. Contract Domains

### Domain A: Provisioning (Server -> Backpack)
*The instructions sent to the edge to dictate the day's pedagogy.*
- **`HybridLessonPlan`**: The authoritative daily workload connecting Kolibri `ContentNodes` to STEAM sandboxes.
- **`PedagogicalContext`**: Vector-retrieved transcript chunks and vocabulary grounding for the local RAG loop.

### Domain B: Telemetry (Backpack -> Server)
*The granular micro-actions logged on the edge for future assessment.*
- **`StudentAction`**: High-frequency logs of video progress, code compilation attempts, and UI interactions.
- **`CognitiveMetric`**: Compressed summaries of student "struggle points" used by the LangGraph Assessor.

### Domain C: Tutoring Orchestration (LLM Loop)
*The real-time handshake between the AI Tutor and the User Interface.*
- **`TeacherAction`**: Socratic prompts, debugging guidance, and audio-visual cues for the "Dumb UI."
- **`ModelRetry`**: Automated feedback payloads when the LLM fails to match a JSON schema.

---

## 4. Implementation Mandates

1. **Schema-First Development**: No feature is implemented in the Backpack or Server until its corresponding Pydantic model is merged into `dt-contracts`.
2. **Recursive Integrity**: Use PEP 695 `type` aliases for all recursive structures (JSON trees, nested steps).
3. **Ritual Verification**: All changes must pass `bash fast.sh` with 100% test coverage and 0% `Any` detection.

## 5. Roadmap: Phase 1 & 2
- [x] Initial `HybridLessonPlan` and `BaseModel` setup.
- [ ] Define `TelemetryPayload` for asynchronous SQLite-to-LanceDB syncing.
- [ ] Implement `TeacherAction` schema for Pydantic-AI "Prompted Output" loops.
- [ ] Authorize `KolibriMapping` schemas for Topic Tree graph traversals.
