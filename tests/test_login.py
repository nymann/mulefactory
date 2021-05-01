import os
from mulefactory.domain.mulefactory import Mulefactory

def test_login():
    m = Mulefactory()
    username = os.environ["MULEFACTORY_USER"]
    password = os.environ["MULEFACTORY_PASS"]
    response = m.login(username=username, password=password)
    c = dict(response.cookies)
    assert "PHPSESSID" in c
    assert "__cfduid" in c
    assert m.session_id != ""
    assert m.cfduid != ""

