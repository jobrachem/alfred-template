"""This file contains custom classes that will be imported in script.py
"""

from alfred3.page import Page
from alfred3.section import SegmentedSection
from alfred3 import element as elm
from thesmuggler import smuggle

inst = smuggle("instructions.py")


class Welcome(Page):
    title = "Welcome to the experiment!"
    uid = "welcome_page"

    def on_exp_access(self):
        self += elm.TextElement("Welcome to alfred!")
        self += elm.TextEntryElement("Enter", name="text1")


class Instructions(Page):
    title = "Instructions (please read carefully)"
    uid = "instructions_page"

    def on_exp_access(self):
        self += elm.TextElement(inst.text1)
        self += elm.TextElement(inst.text2)
        self += elm.TextElement(inst.text_dict.get("other_files"))

    def on_first_show(self):
        d = self.get_page_data(page_uid="welcome_page")
        text = f"This text was entered on the previous page: {d['text1']}"

        self += elm.TextElement(text)


class MainSection(SegmentedSection):
    def on_exp_access(self):
        self += Welcome()
        self += Instructions()

