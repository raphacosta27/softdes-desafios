import pytest

import sys
sys.path.insert(1, './../src')
from softdes import lambda_handler

def test_lambda_handler_wrong():
    event = {}
    event['code'] = '''def desafio1(n):
                return n
           '''
    event['ndes'] = 1
    event['args'] = [[1], [2], [3]]
    event['resp'] = [0, 0, 0]
    event['diag'] = ['a', 'b', 'c']
    resp = lambda_handler(event, None)
    assert resp == 'a b c'

def test_lambda_handler_correct():
    event = {}
    event['code'] = '''def desafio1(n):
                return 0
           '''
    event['ndes'] = 1
    event['args'] = [[1], [2], [3]]
    event['resp'] = [0, 0, 0]
    event['diag'] = ['a', 'b', 'c']
    resp = lambda_handler(event, None)
    assert len(resp) == 0
