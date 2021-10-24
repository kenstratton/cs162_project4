from gui_prototype import *
import pytest


# Objects from classes in the application
app = Prototype()
projector = app.projector
finder = app.finder


# Tests for Text Projector
def test_projecter():
    lbl_txt = projector.lbl_txt
    txt_box = projector.txt_box
    sbmt_btn = projector.sbmt_btn

    # Tests for Label
    assert lbl_txt["text"] == ""
    assert lbl_txt["font"] == "{} 14"
    # Tests for Text Box
    assert txt_box["width"] == 20
    assert txt_box.get_txt() == ""
    # Tests for Button
    assert sbmt_btn["text"] == "Submit"
    assert sbmt_btn["width"] == 6
    assert sbmt_btn["font"] == "{} 12"
    # Test for output
    txt_box.insert(0, "Hello World.")
    projector.txt_project()
    assert lbl_txt["text"] == "Hello World."


# Tests for Minimum Finder
def test_init_finder():
    lbl_pos = finder.lbl_pos
    lbl_num = finder.lbl_num
    txt_box = finder.boxes[0]
    min_btn = finder.min_btn

    # Tests for Label
    assert lbl_pos["text"] == ""
    assert lbl_pos["font"] == "bold 16"
    # Tests for Text Box
    assert txt_box["width"] == 2
    assert txt_box.get_txt() == "0"
    # Tests for Button
    assert min_btn["text"] == "Pending"
    assert min_btn["width"] == 6
    assert min_btn["font"] == "{} 12"
    # Tests for output
    txt_box.insert(0, "-0.5")
    finder.process_request()
    assert lbl_pos["text"] == "The Minimum :"
    assert lbl_num["text"] == "-0.5"
    finder.display_sorted()
    assert lbl_pos["text"] == "The 2 nd :"
    assert lbl_num["text"] == "1"