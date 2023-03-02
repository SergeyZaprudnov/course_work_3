from foo import utils
import requests
import pytest


def test_json_load():
    """тестирование получения данных"""
    assert type(utils.json_load()) == list
    assert len((utils.json_load())) > 0

def test_st_executed():
    """тестирование списка операций"""
    assert isinstance(utils.st_executed(), list)
    assert utils.st_executed() is not None

