import datetime
from typing import Any, Dict

from mulefactory.domain import mfactory


class POEMulefactory(mfactory.Mulefactory):
    game_id: int = 14
    beginning_of_unix_time = datetime.datetime.utcfromtimestamp(0)

    def game_data(self):
        """Gets the item prices for a specific server_id and game.

        Returns:
            Response
        """
        url: str = "https://supply.mulefactory.com/ajax.php"
        request_parameters: Dict[str, Any] = {
            "module": "supply",
            "target": "ajax",
            "command": "check",
            "gameid": self.game_id,
            "serverid": self.server_id,
            "_": self.get_time(),
        }
        return self.scraper.get(url=url, params=request_parameters)

    def get_time(self):
        return int((datetime.datetime.utcnow() - self.beginning_of_unix_time).total_seconds())
