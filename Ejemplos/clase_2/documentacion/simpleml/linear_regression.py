import numpy as np
from abc import ABC


class BaseModel(ABC):
    """
    Abstract Model Class used as interface of all regression models.

    :param model: Stored model data (NumPy array in most cases)
    :type model: np.ndarray
    :param data: input data for training or testing
    :type data: np.ndarray
    :param labels: labels of the input data for training
    :type labels: np.ndarray
    """

    def __init__(self):
        self.model = None

    def fit(self, data: np.ndarray, labels: np.ndarray):
        """
        :param data: input data for training
        :type data: np.ndarray
        :param labels: labels of the input data for training
        :type labels: np.ndarray
        """

        pass

    def predict(self, data: np.ndarray):
        """
        :param data: input data for testing
        :type data: np.ndarray
        :return: predicted data
        :rtype: np.ndarray
        """

        pass


class ConstantModel(BaseModel):
    """
    Constant model class that uses the average of each feature as prediction.

    :param model: Stored model data (NumPy array in most cases)
    :type model: np.ndarray
    :param data: input data for training or testing
    :type data: np.ndarray
    :param labels: labels of the input data for training
    :type labels: np.ndarray
    """

    def fit(self, data: np.ndarray, labels: np.ndarray) -> None:
        """
        Method for fitting the training data and determining and storing the model parameters. In this case
        the model returns always the data average.

        :param data: input data for training
        :type data: np.ndarray
        :param labels: labels of the input data for training
        :type labels: np.ndarray
        :return: None
        """

        w = labels.mean()
        self.model = w

    def predict(self, data: np.ndarray) -> np.ndarray:
        """
        Given the input data it returns the predicted output for each input point using the model, in this case
        the average.

        :param data: input data for testing
        :type data: np.ndarray
        :return: predicted data
        :rtype: np.ndarray
        """

        return np.ones(len(data)) * self.model


class LinearRegression(BaseModel):
    """
    Linear regression model class that uses the following model for predictions:
    .. math::
        y = \\omega*X
    """

    def fit(self, data: np.ndarray, labels: np.ndarray) -> None:
        """
        Method for fitting the training data and determining and storing the model parameters :math:`\\omega`.

        :param data: input data for training
        :type data: np.ndarray
        :param labels: labels of the input data for training
        :type labels: np.ndarray
        :return: None
        """

        if len(data.shape) == 1:
            w = data.T.dot(labels) / data.T.dot(data)
        else:
            w = np.linalg.inv(data.T.dot(data)).dot(data.T).dot(labels)
        self.model = w

    def predict(self, data: np.ndarray) -> np.ndarray:
        """
        Given the input data it returns the predicted output for each input point using the model, in this case:

        .. math::
            y = \\omega*X

        :param data: input data for testing
        :type data: np.ndarray
        :return: predicted data
        :rtype: np.ndarray
        """

        return self.model * data


class LinearRegressionWithB(BaseModel):
    """
    Affine regression model class that uses the following model for predictions:

    .. math::
        y = \\omega*X + b
    """

    def fit(self, data: np.ndarray, labels: np.ndarray) -> None:
        """
        Method for fitting the training data and determining and storing the model parameters :math:`\\omega` and b.

        :param data: input data for training
        :type data: np.ndarray
        :param labels: labels of the input data for training
        :type labels: np.ndarray
        :return: None
        """

        x_expanded = np.vstack((data, np.ones(len(data)))).T
        w = np.linalg.inv(x_expanded.T.dot(x_expanded)).dot(x_expanded.T).dot(labels)
        self.model = w

    def predict(self, data: np.ndarray) -> np.ndarray:
        """
        Given the input data it returns the predicted output for each input point using the model, in this case:

        .. math::
            y = \\omega*X + b

        :param data: input data for testing
        :type data: np.ndarray
        :return: predicted data
        :rtype: np.ndarray
        """

        x_expanded = np.vstack((data, np.ones(len(data)))).T
        return x_expanded.dot(self.model)
