import numpy as np

def moving_average(data: np.ndarray, window_size: int):
    """
    In statistics, a moving average (rolling average or running average) is a
    calculation to analyze data points by creating a series of averages of
    different selections of the full data set. It is also called a moving mean
    (MM) or rolling mean and is a type of finite impulse response filter.
    Variations include: simple, cumulative, or weighted forms.

    Parameters
    ----------
    data: np.ndarray
        Array on which moving average has to be implemented.
    window_size: int
        Values till which to include while averaging.

    Returns
    -------
    np.ndarray
        The averaged Array.

    References
    ----------
    .. [1] https://en.wikipedia.org/wiki/Moving_average

    """
    weights = np.ones(window_size) / window_size
    return np.convolve(data, weights, mode='valid')