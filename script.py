# -*- coding:utf-8 -*-

#################################
# - Section 1: Module imports - #
#################################

from alfred.page import WebCompositePage
from alfred.section import Section
from alfred.element import TextElement
from alfred.helpmates import parse_xml_to_dict

from alfred import Experiment


#################################################
# - Section 2: Global variables and functions - #
#################################################
EXP_TYPE = "web"
EXP_NAME = "template"
EXP_VERSION = "1.0"
EXP_AUTHOR_MAIL = "your@email.com"

instr = parse_xml_to_dict("files/instructions.xml")

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
        welcome = WebCompositePage(title="Hello, world!", uid="welcome")

        text_a = TextElement("This is a basic template.")
        text_b = TextElement(instr["text01"])
        welcome.append(text_a, text_b)

        # Initialize and fill sections
        main = Section()
        main.append(welcome)

        # Append sections and pages to experiment
        exp.page_controller.append(main)

        # --- END OF EDITABLE AREA --- #

        return exp


generate_experiment = Script().generate_experiment
