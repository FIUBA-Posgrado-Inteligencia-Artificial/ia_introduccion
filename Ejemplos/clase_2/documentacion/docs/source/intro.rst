Introduction
============

``SimpleML`` is a high-level OO Python package which aims to provide an easy and intuitive way implementation
of simple machine learning models. In essence, this package is a simplification of existing packages like
``Scikit-learn``.


Motivation
**********

As a newbie experimenter in the field of machine learning, it's easy to forget about the mathematical and statistical
foundations behind the principal models, especially due to the vast amount of high-level packages available with a
plug-and-play philosophy. This package is implemented purely in NumPy and completely vectorized to explain the model's
functionalities for educational purposes.

Limitations
***********

Right now, only a couple of models are implemented, such as :py:class:`simpleml.kmeans.KMeans` for unsupervised learning
and regression models like :py:class:`simpleml.linear_regression.LinearRegression` for supervised learning. Under no
circumstances should this package be used for production environments, only for educational purposes.