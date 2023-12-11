import numpy as np

from openalerts.core.simple_indicators import moving_average


def test_moving_average():
    test_data = np.arange(1, 10)
    test_window = 3
    
    expected_result = np.arange(2, 9)
    test_result = moving_average(test_data, test_window)
    assert np.allclose(expected_result, test_result)