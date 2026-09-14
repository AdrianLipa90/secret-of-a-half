# SOH 600-cell / binary-icosahedral candidate v0.1

Status: `CANDIDATE / ACTIVE_WORKING_VERSION / STRUCTURAL_SU2_BRIDGE / PHYSICAL_BINDING_OPEN`

Date: 2026-09-11

This candidate is executable working code, not a dormant note. It exposes the 120 unit quaternions given by the 600-cell vertices and verifies them as a closed finite subgroup under quaternion multiplication.

The working bridge provides:

- group order 120;
- identity and inverse operations;
- the central element `-1`;
- antipodal pairing `q <-> -q` into 60 pairs;
- identical SO(3) rotations for `q` and `-q`;
- fail-closed rejection of indices outside the verified carrier.

The full test iterates all 120 x 120 products and verifies closure numerically.

This is the finite structural bridge

`600-cell vertices -> unit quaternions -> 2I subset SU(2) -> antipodal quotient of order 60`.

It does not by itself promote a physical spin-1/2 interpretation, a particle assignment, or a proof of the SOH analytic claims. Those bindings remain separate gates.

Implementation:

`src/secret_of_a_half/binary_icosahedral_candidate_v01.py`

Tests:

`tests/test_binary_icosahedral_candidate_v01.py`
