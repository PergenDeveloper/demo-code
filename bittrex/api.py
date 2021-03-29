import requests


class APIClient:
    API_ENDPOINT = 'https://api.bittrex.com/v3/markets/BTC-USDT/summary'

    def get_btc_summary(self):
        response = requests.get(self.API_ENDPOINT)
        try:
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return None
