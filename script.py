# -*- coding:utf-8 -*-

#################################
# - Section 1: Module imports - #
#################################

import alfred
from alfred.page import WebCompositePage
from alfred.section import Section
from alfred.element import TextElement
from alfred.helpmates import parse_xml_to_dict



#################################################
# - Section 2: Global variables and functions - #
#################################################

instr = parse_xml_to_dict("files/instructions.xml")

#################################
# - Section 3: Custom classes - #
#################################


########################################
# - Section 4: Experiment generation - #
########################################


def generate_experiment(self):
    # Define pages
    welcome = WebCompositePage(title="Hello, world!", uid="welcome")

    text_a = TextElement("This is a basic template.", name="text_a")
    text_b = TextElement(instr["text01"], name="text_b")
    welcome.append(text_a, text_b)

    # Initialize and fill sections
    main = Section()
    main.append(welcome)

    # Append sections and pages to experiment
    exp = alfred.Experiment()
    exp.append(main)

    # --- END OF EDITABLE AREA --- #

    return exp


alfred.run(generate_experiment)
