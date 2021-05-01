import enum

from pydantic import BaseModel
from pydantic import utils


class Server(str, enum.Enum):  # noqa: WPS600
    standard_sc = "standard_sc"
    standard_hc = "standard_hc"
    ultimatum_sc = "ultimatum_sc"
    ultimatum_hc = "ultimatum_hc"

    def get_id(self) -> int:
        server_map = {
            "standard_sc": 1047,
            "standard_hc": 1048,
            "ultimatum_sc": 1742,
            "ultimatum_hc": 1743,
        }
        return server_map[self.value]


class PoeItem(BaseModel):
    identifier: int
    limit: str
    price: str
    update: bool
    exchange_rate: float

    class Config(object):
        """Pydantic configurator."""

        alias_generator = utils.to_camel
