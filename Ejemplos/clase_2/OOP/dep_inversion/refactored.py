from abc import ABC, abstractmethod


# Abstract Based Class
class Models(ABC):
    @abstractmethod
    def train(self):
        pass

    @abstractmethod
    def predict(self):
        pass

    @abstractmethod
    def log_metrics(self):
        pass

    @abstractmethod
    def print_model(self):
        pass


# Implements the interface defined by Models
class RandomForest(Models):
    def train(self):
        pass

    def predict(self):
        pass

    def log_metrics(self):
        print("Printing training metrics")

    def print_model(self):
        print("Random Forest model parameters")


class AdaBoost(Models):
    def train(self):
        pass

    def predict(self):
        pass

    def log_metrics(self):
        print("Printing training metrics")

    def print_model(self):
        print("AdaBoost model parameters")

# We removed the dependency between the Logger and the models
# using dependency inversion

# Type hint--> arg1: str, arg2: int = 3, Tuple, List, Any, obj


class ModelLogger(object):

    def __init__(self, ml: Models, verbose=True):
        self.model = ml
        self.verbose = verbose

    def logging(self):
        if self.verbose:
            self.model.train()
            self.model.log_metrics()
            self.model.print_model()
        else:
            self.model.train()


if __name__ == "__main__":
    rf = RandomForest()
    logger_1 = ModelLogger(rf, verbose=True)
    logger_1.logging()
    ab = AdaBoost()
    logger_2 = ModelLogger(ab, verbose=True)
    logger_2.logging()
