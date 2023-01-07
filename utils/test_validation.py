import pytest
from utils.validation import Validation

def test_validation_register_1():
    test_register_1 = Validation.validation_register("Muhammad^&$%^&","asd")
    assert test_register_1 == False

def test_validation_register_2():
    test_register_2 = Validation.validation_register("Mas","asd")
    assert test_register_2 == False


def test_validation_register_3():
    test_register_3 = Validation.validation_register("Muhammad Rizky Mubarok","asdasd")
    assert test_register_3 == True


def test_validation_borrow_1():
    test_borrow_1 = Validation.validation_borrow("dada&^")
    assert test_borrow_1 == False

def test_validation_borrow_2():
    test_borrow_2 = Validation.validation_borrow("0000")
    assert test_borrow_2 == False

def test_validation_borrow_3():
    test_borrow_3 = Validation.validation_borrow("1000")
    assert test_borrow_3 == False

def test_validation_borrow_4():
    test_borrow_4 = Validation.validation_borrow("40000")
    assert test_borrow_4 == True

