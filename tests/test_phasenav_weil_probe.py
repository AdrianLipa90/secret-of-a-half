from __future__ import annotations

from secret_of_a_half.phasenav_weil_probe import (
    WeilProbeProgram,
    centered_involution,
    default_program_path,
    feature_vector,
    run_probe,
)


def load_program() -> WeilProbeProgram:
    return WeilProbeProgram.load(default_program_path())


def test_native_profile_parses() -> None:
    program = load_program()
    assert program.channel_count == 2
    assert program.zero_ordinate_count == 10
    assert len(program.ordinates) == 10


def test_centered_involution_is_an_involution() -> None:
    z = 0.17 + 14.2j
    assert centered_involution(centered_involution(z)) == z


def test_channels_encode_opposite_radial_gain() -> None:
    program = load_program()
    minus, plus = feature_vector(0.1 + 1j * program.target_ordinate, program)
    assert abs(plus) > abs(minus)


def test_on_axis_control_is_psd() -> None:
    receipt = run_probe(load_program())
    assert receipt["on_axis_control"]["pass"] is True
    assert receipt["on_axis_control"]["lambda_min"] >= -1e-10


def test_synthetic_off_axis_quartet_has_negative_witness() -> None:
    receipt = run_probe(load_program())
    assert receipt["synthetic_off_axis"]["pass"] is True
    assert receipt["synthetic_off_axis"]["lambda_min"] < -1e-6
