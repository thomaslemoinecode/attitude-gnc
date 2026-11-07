import numpy as np

from attitude_gnc.kalman_scalar import predict, update


def test_variance_of_constant_estimation():
    # parameters: constant state (a = 1, q = 0), direct measurement (h = 1)
    P_0 = 4.0
    r = 0.25
    n = 100
    a = 1.0
    q = 0.0
    h = 1.0

    x_hat, P = 0.0, P_0
    for _ in range(n):
        x_prior, P_prior = predict(x_hat, P, a, q)
        x_hat, P, _ = update(x_prior, P_prior, z=0.0, h=h, r=r)

    P_exact = (1 / P_0 + n / r) ** (-1)
    np.testing.assert_allclose(P, P_exact)
