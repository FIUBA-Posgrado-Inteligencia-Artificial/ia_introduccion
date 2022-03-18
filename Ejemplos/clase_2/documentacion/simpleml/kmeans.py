import numpy as np
from typing import Any, Dict, List, Tuple, Union


class KMeans:
    """
    Class for the NumPy simplified implementation of K-means.

    :param n_clusters: Number of clusters used to segment the data.
    :type n_clusters: int
    :param iterations: Maximum number of iterations for the model.
    :type iterations: int, optional
    :param data: Input data to cluster.
    :type data: np.ndarray
    :param centroids: Final centroids locations
    :type centroids: np.ndarray
    """

    def __init__(self, n_clusters: int, iterations: int = 1000) -> None:
        """
        Constructor method
        """

        self.n_clusters = n_clusters
        self.iterations = iterations
        self.centroids = np.zeros((3, 3))

    def k_means_loop(self, data: np.ndarray, centroids: np.ndarray) -> np.ndarray:
        """

        :param data: Input data to cluster
        :type data: np.ndarray
        :param centroids: Current centroids locations
        :type centroids: np.ndarray
        :return: cluster id for each point
        :rtype: np.ndarray
        """

        expanded_centroids = centroids[:, None]
        distances = np.sqrt(np.sum((expanded_centroids - data) ** 2, axis=2))
        arg_min = np.argmin(distances, axis=0)
        return arg_min

    def fit(self, data: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        """
        Returns the locations of the centroids and the cluster identity of each point
        of the input data.

        :param data: Input data to cluster
        :type data: np.ndarray
        :return: location of the centroids and the cluster ids.
        :rtype: tuple with the centroids (NumPy array) and cluster ids (NumPy array)
        """

        centroids = np.eye(self.n_clusters, data.shape[1])
        for i in range(self.iterations):
            centroids, cluster_ids = self.k_means_loop(data, centroids)

        self.centroids = centroids

        if cluster_ids:
            return centroids, cluster_ids
        else:
            print("There was a problem establishing the clusters")
            raise ValueError

    def predict(self, data: np.ndarray) -> np.ndarray:
        """
        Returns the cluster identity of each of the points from the input data, using
        the centroids previously obtained by fitting the training data.

        :param data: Input data to cluster
        :type data: np.ndarray
        :return: Cluster identity of each point of the input data.
        :rtype: np.ndarray
        """

        expanded_centroids = self.centroids[:, None]
        distances = np.sqrt(np.sum((expanded_centroids - X) ** 2, axis=2))
        arg_min = np.argmin(distances, axis=0)
        return arg_min
