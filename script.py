from alfred3 import Experiment
from alfred3.section import SegmentedSection

from thesmuggler import smuggle

exp_classes = smuggle("files/exp_classes.py")


def generate_experiment(self, config=None):
    exp = Experiment(config=config)

    main = SegmentedSection()

    pg_welcome = exp_classes.Welcome(title="Welcome Page")
    pg_instructions = exp_classes.Instructions(title="Instructions")

    main.append(pg_welcome, pg_instructions)

    exp.append(main)

    return exp

