"""Smoke tests: check that the toolchain works (pytest, NumPy, src layout)."""

import numpy as np

import attitude_gnc


def test_package_is_importable():
    # assert that the package exposes a callable named `main`
    assert attitude_gnc.__name__ == "attitude_gnc"


def test_inverse_times_matrix_is_identity():
    # create a random generator with a fixed seed
    rng = np.random.default_rng(seed=42)
    # draw a 3x3 matrix A with standard normal entries
    A = rng.standard_normal(size=(3, 3))
    A_inv = np.linalg.inv(A)
    # inv(A) @ A must equal the identity. Absolute tolerance because the
    # expected off-diagonal values are 0; measured error is about 4e-14.
    np.testing.assert_allclose(A_inv @ A, np.eye(3), atol=1e-12)
