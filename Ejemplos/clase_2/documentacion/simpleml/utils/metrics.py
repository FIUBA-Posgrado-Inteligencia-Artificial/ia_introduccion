import numpy as np
from abc import ABC


class Metric(ABC):
    """
    Abstract Metric Class used as interface of all metrics.

    """

    def __call__(self, target: np.ndarray, prediction: np.ndarray):
        pass


class MSE(Metric):
    """
    MSE metric class. It uses the call method to calculate the metric.

    """

    def __init__(self):
        """
        MSE class constructor.

        """

        Metric.__init__(self)

    def __call__(self, target: np.ndarray, prediction: np.ndarray) -> float:
        """
        Call method that calculates the MSE metric.

        :param target: target values or ground truth
        :type target: np.ndarray
        :param prediction: predicted values
        :type prediction: np.ndarray
        :return: metric value
        :rtype: float
        """

        n = target.size
        return np.sum((target - prediction) ** 2) / n
