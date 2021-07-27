#integrate API using API key

import os
import requests
import json

# from twilio.rest import api

API_KEY=os.environ.get('MARKETSTACK_KEY')
BASE_URL = 'http://api.marketstack.com/v1/'

def get_stock_price(stock_symbol):
    params = {
        'access_key' : API_KEY
        

    }
    elements=(BASE_URL,"tickers/",stock_symbol,"/intraday/latest")
    end_point = ''.join(elements)
    
    api_result = requests.get(end_point,params)
    
    json_result = json.loads(api_result.text)
    
    return {
        "lowest_price": json_result["low"]
    }



