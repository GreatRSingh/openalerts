from openalerts.core.simple_indicators import moving_average
import numpy as np


def macd(data: np.ndarray, p1: int = 12, p2: int = 26):
    assert p2>p1
    mov_1 = moving_average(data, p1)
    mov_2 = moving_average(data, p2)
    n_data = len(mov_2)
    return data[-n_data:], mov_1[-n_data:], mov_2[-n_data:]
