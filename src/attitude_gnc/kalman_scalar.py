"""Scalar Kalman filter (one state, one measurement)."""


def predict(x_hat: float, P: float, a: float, q: float) -> tuple[float, float]:
    """Propagate the estimate and its variance through x_k = a x_{k-1} + w."""
    x_prior = a * x_hat
    P_prior = a**2 * P + q
    return x_prior, P_prior


def update(
    x_prior: float, P_prior: float, z: float, h: float, r: float
) -> tuple[float, float, float]:
    """Correct the a priori estimate with the measurement z_k = h x_k + v.

    Returns (x_hat, P, K).
    """
    S = h**2 * P_prior + r
    K = P_prior * h / S
    P = (1 - K * h) * P_prior
    innovation = z - h * x_prior
    x_hat = x_prior + K * innovation
    return x_hat, P, K
