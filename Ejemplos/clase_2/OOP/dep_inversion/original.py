class RandomForest(object):

    def train(self):
        pass

    def predict(self):
        pass

    def log_metrics(self):
        print("Printing training metrics")

    def print_model(self):
        print("Random Forest model parameters")


class ModelLogger(object):

    def __init__(self, ml: RandomForest, verbose=True):
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
    logger = ModelLogger(rf, verbose=True)
    logger.logging()
