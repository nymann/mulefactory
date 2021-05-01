import os

from mulefactory.domain.mulefactory import Mulefactory


def test_login():
    m = Mulefactory()
    username = os.environ["MULEFACTORY_USER"]
    password = os.environ["MULEFACTORY_PASS"]
    response = m.login(username=username, password=password)
    assert response.status_code == 200
    assert "PHPSESSID" in m.scraper.cookies
    assert "__cfduid" in m.scraper.cookies
