import cloudscraper


class Mulefactory(object):
    scraper = cloudscraper.create_scraper(debug=True)

    def __init__(self, server_id: int):
        self.server_id = server_id

    def login(self, username: str, password: str):
        """Logs a user in to mulefactory.

        Args:
            username: supply.mulefactory username
            password: supply.mulefactory password

        Returns:
            Response
        """
        request_data = {"postid": "login", "admin_name": username, "admin_pass": password}
        url = "http://supply.mulefactory.com/"
        return self.scraper.post(url=url, data=request_data)

    def game_data(self):
        raise NotImplementedError()
