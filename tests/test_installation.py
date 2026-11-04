"""Smoke tests: check that the toolchain works (pytest, NumPy, src layout)."""

import numpy as np

import attitude_gnc


def test_package_is_importable():
    # assert that the package exposes a callable named `main`
    assert callable(attitude_gnc.main)


def test_inverse_times_matrix_is_identity():

    # check that inv(A) @ A equals the 3x3 identity,
    # using np.testing.assert_allclose with an absolute tolerance
    # create a random generator with a fixed seed (e.g. 42)
    rng = np.random.default_rng(seed=42)
    # draw a 3x3 matrix A with standard normal entries
    A = rng.standard_normal(size=(3, 3))
    A_inv = np.linalg.inv(A)
    np.testing.assert_allclose(A_inv @ A, np.eye(3), atol=1e-12)
