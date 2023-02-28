from foo import utils
import requests
import pytest


def test_json_load():
    assert type(utils.load.json()) == list
    assert len((utils.load_json())) > 0
