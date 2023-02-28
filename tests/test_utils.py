from foo import utils


import requests
import pytest


def test_json_load():
    assert type(utils.json_load()) == list
    assert len((utils.json_load())) > 0
