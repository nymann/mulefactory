import os

from mulefactory.domain.path_of_exile import POEMulefactory


def test_get_poe_data():
    poe = POEMulefactory()
    poe.login(username=os.environ["MULEFACTORY_USER"], password=os.environ["MULEFACTORY_PASS"])
    response = poe.game_data()
    assert response.status_code == 200
    assert response.json() is not None
