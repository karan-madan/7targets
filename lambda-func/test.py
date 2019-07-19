# import lambda_handler
from handler import lambda_handler
import handler
import pytest


def test_lambda_handler():
    try:
     event = {'Number1': 10, 'Number2': 20}
    except null:
     assert lambda_handler(event, null) == 30

