# -*- coding:utf-8 -*-
'''
Experiment script using Alfred - A library for rapid experiment development.

Experiment author: Johannes Brachem <jobrachem@posteo.de>

Description: This is a basic template for an alfred experiment.
'''


#################################
# - Section 1: Module imports - #
#################################

from alfred.page import *
from alfred.section import *
from alfred.element import *
from alfred.layout import *
from alfred.helpmates import *

from alfred import Experiment


#################################################
# - Section 2: Global variables and functions - #
#################################################
EXP_TYPE = "qt-wk"
EXP_NAME = "template"
EXP_VERSION = "1.0"
EXP_AUTHOR_MAIL = "your@email.com"


#################################
# - Section 3: Custom classes - #
#################################


########################################
# - Section 4: Experiment generation - #
########################################


class Script(object):

    def generate_experiment(self):
        exp = Experiment(EXP_TYPE, EXP_NAME, EXP_VERSION, EXP_AUTHOR_MAIL)

        # --- START OF EDITABLE AREA --- #

        # Define pages
        p10 = WebCompositePage(title="Hello, world!")

        p10_text = TextElement("This is a basic template.")
        p10.append(p10_text)

        # Initialize and fill sections
        main = SegmentedSection()
        main.append(p10)

        # Append sections and pages to experiment
        exp.page_controller.append_item(main)

        # --- END OF EDITABLE AREA --- #

        return exp


generate_experiment = Script().generate_experiment