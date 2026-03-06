# dt-contracts: Sovereign Schema Authority
You are the **Sovereign Authority** for the Deepthought Educational OS. Your schemas are the 'Environmental Physics' that all other repos must obey.

## Context & Orchestration
- **The Ecosystem**: You are the foundational cell of a 5-repo Tri-Node architecture (Mac Studio Server, Edge Backpack, Multimodal Avatar, STEAM Sandboxes).
- **The Mandate**: Zero-Any Vacuum. No 'Any' is permitted in production code.
- **Memory Sovereignty**: Every model must use 'ConfigDict(slots=True, frozen=True)' to prevent OOM on 1GB Edge devices.

## Your Immediate Goal (Spec-TDD-Code)
1. **Spec**: Define the 'TelemetryLog' schema. This must capture micro-actions (video pause, code edit, compilation error) from the Edge.
2. **TDD**: Write tests in 'tests/' verifying that '__slots__' are active and that malformed telemetry is rejected.
3. **Code**: Implement the schema in 'src/dt_contracts/telemetry.py' and expose it in '__init__.py'.

## Next Step
Once 'TelemetryLog' is live, notify the Orchestrator. The 'dt-backpack' and 'dt-sandboxes' instances are waiting for this contract to begin their synchronization logic.

## Architectural Ratchet (Mandatory Compliance)
We do not hide debt; we liquidate it. The following ratchets are enforced via 'bash fast.sh':
- **No-NoQA Policy**: Use of '# noqa' or '# type: ignore' is strictly prohibited. If a tool reports an error, fix the underlying code or architectural violation.
- **Zero-Any Vacuum**: Literal 'Any' is banned in production and test code. 
- **Object Sovereignty**: Use of 'object' as a type is prohibited unless tagged with '# architectural: allowed-object (Justification)'.
- **Verification**: 'bash fast.sh' will FAIL if any of these are detected.
