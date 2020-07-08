"""This file contains custom classes that will be imported in script.py
"""

from alfred3.page import Page
from alfred3 import element as elm
from thesmuggler import smuggle

inst = smuggle("instructions.py")


class Welcome(Page):
    def on_showing(self):

        welcome_text = elm.TextElement("Welcome to alfred!")
        self.append(welcome_text)


class Instructions(Page):
    def on_showing(self):

        general_inst = elm.TextElement(inst.text1)
        additional_inst = elm.TextElement(inst.text2)
        other_files = elm.TextElement(inst.text_dict.get("other_files"))

        self.append(general_inst, additional_inst, other_files)
