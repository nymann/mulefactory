import enum
class Server(str, enum.Enum):
    standard_sc = "standard_sc" 
    standard_hc = "standard_hc" 
    ultimatum_sc = "ultimatum_sc" 
    ultimatum_hc = "ultimatum_hc" 

    def get_id(self) -> int:
        server_map = {
            "standard_sc" : 1047,
            "standard_hc": 1048,
            "ultimatum_sc" : 1742,
            "ultimatum_hc" : 1743,
        }
        return server_map[self.value]
