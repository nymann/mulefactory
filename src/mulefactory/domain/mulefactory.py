import requests

class Mulefactory(object):
    session_id: str = ""
    cfduid: str = ""

    def login(self, username: str, password: str):
        """
        curl 'http://supply.mulefactory.com/' 
        
        -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0' 
        -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' 
        -H 'Accept-Language: en-US,en;q=0.5' --compressed 
        -H 'Content-Type: application/x-www-form-urlencoded' 
        -H 'Origin: http://supply.mulefactory.com' 
        -H 'Connection: keep-alive' 
        -H 'Referer: http://supply.mulefactory.com/' 
        -H 'Cookie: __cfduid=dab170aa372b23e24571bc58f20aa34d91619558519; PHPSESSID=0acc05dcb5e148e637768feac2da1181' 
        -H 'Upgrade-Insecure-Requests: 1' 
        -H 'Pragma: no-cache' 
        -H 'Cache-Control: no-cache'
        --data-raw 'postid=login&admin_name=USERNAME&admin_pass=PASS'
        """
        data = "postid=login&adin_name={username}&admin_pass={password}".format(username=username, password=password)
        url="http://supply.mulefactory.com/"
        headers={
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'http://supply.mulefactory.com',
            'Connection': 'keep-alive',
            'Referer': 'http://supply.mulefactory.com/',
            'Upgrade-Insecure-Requests': '1',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache'
        }
        with requests.Session() as session:
            response = session.post(url=url, data=data, headers=headers)
            cookies = dict(response.cookies)
            self.session_id = cookies["PHPSESSID"]
            self.cfduid = cookies["__cfduid"]
            return response


    def game_data(self):
        pass
