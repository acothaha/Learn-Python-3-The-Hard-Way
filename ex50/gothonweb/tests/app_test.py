from nose.tools import *
import pytest
from app import app


app.config['TESTING'] = True
web = app.test_client()

def test_index():
    rv = web.get('/', follow_redirects=True)
    assert rv.status_code == 404

    rv = web.get('/hello', follow_redirects=True)
    assert b"Fill Out This Form" in rv.data

    data = {'name': 'asping', 'greet': 'guten morgen'}
    rv = web.post('/hello', follow_redirects=True, data=data)
    assert b"asping" in rv.data
    assert b"guten morgen" in rv.data
