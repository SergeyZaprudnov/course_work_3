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

def test_sort_date():
    """тест сортировки даты"""
    assert isinstance(utils.sort_date(), list)
    assert utils.sort_date() != utils.sort_date()

def test_last_five():
    """тест получения операций"""
    assert isinstance(utils.last_five()[:5], list)
    assert len(utils.last_five()[:5]) == 5

def test_disquise_card():
    """тест маскировки карты"""
    for i in utils.last_five()[:5]:
        assert isinstance(i, dict)
    last_five_transactions = utils.last_five()[:5]
    assert isinstance(utils.disguise_card(last_five_transactions), list)

