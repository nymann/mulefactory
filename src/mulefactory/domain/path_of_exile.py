from typing import Dict, Any
import requests
import datetime

from mulefactory.domain import mulefactory

class POEMulefactory(mulefactory.Mulefactory):
    b = datetime.datetime.utcfromtimestamp(0)
    def game_data(self):
        """curl 'https://supply.mulefactory.com/ajax.php?
        module=supply&
        target=ajax&
        command=check&
        gameid=14&
        serverid=1047&
        _=1619558804510'
        -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0' 
        -H 'Accept: application/json, text/javascript, */*; q=0.01' 
        -H 'Accept-Language: en-US,en;q=0.5' --compressed 
        -H 'X-Requested-With: XMLHttpRequest' 
        -H 'Connection: keep-alive' 
        -H 'Referer: https://supply.mulefactory.com/supply/?gameid=14&serverid=1047' 
        -H 'Cookie: __cfduid=dab170aa372b23e24571bc58f20aa34d91619558519; PHPSESSID=55c6400fcab994bee9d1624b5427fd8165b47635; appHeadReferer_v01=YToyOntzOjY6IlN1cHBseSI7czo2MjoiaHR0cHM6Ly9zdXBwbHkubXVsZWZhY3RvcnkuY29tL3N1cHBseS8%2FZ2FtZWlkPTE0JnNlcnZlcmlkPTEwNDciO3M6MDoiIjtzOjMxOiJodHRwczovL3N1cHBseS5tdWxlZmFjdG9yeS5jb20vIjt9' 
        -H 'Pragma: no-cache' 
        -H 'Cache-Control: no-cache' 
        -H 'TE: Trailers'"
        """
        url: str = "https://supply.mulefactory.com/ajax.php"
        parameters: Dict[str,Any] = {
            "module": "supply",
            "target":"ajax",
            "command":"check",
            "gameid":14,
            "serverid":1047,
            "_":self.get_time()
        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'en-US,en;q=0.5', 
            'X-Requested-With': 'XMLHttpRequest',
            'Connection': 'keep-alive',
            'Referer': 'https://supply.mulefactory.com/supply/?gameid=14&serverid=1047',
            'Cookie': f'__cfduid={self.cfduid}; PHPSESSID={self.session_id};',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'TE': 'Trailers'
        }
        return requests.get(url=url, params=parameters, headers=headers)

    def get_time(self):
        return int((datetime.datetime.utcnow() - self.b).total_seconds())
