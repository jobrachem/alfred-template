from alfred3 import Experiment
from thesmuggler import smuggle

exp_classes = smuggle("files/exp_classes.py")


def generate_experiment(self, config=None):

    exp = Experiment(config=config)
    exp += exp_classes.MainSection()

    return exp
