from flask import Flask,request
from twilio.rest import Client
from marketstack import get_stock_price
import os

from werkzeug.wrappers import response
app = Flask(__name__)




ACCOUNT_ID=os.environ.get('ACCOUNT_TWILIO')
TWILIO_TOKEN=os.environ.get('TOKEN_TWILIO')

client = Client(ACCOUNT_ID, TWILIO_TOKEN)
TWILIO_NUMBER= 'whatsapp:+14155238886'

def send_msg(msg, receipient):
    client.messages.create(
        from_=TWILIO_NUMBER,
        body=msg,
        to=receipient
    )

def process_msg(msg):
    response=""
    if msg=="hi" or msg=="hello" or msg=="Hello" or msg=="Hi":
        response="Hello, welcome to the stock market bot!!"
        response += "\nEnter the symbol of stock for wich you want info as : sym: <symbol>"

    
    elif 'sym:' in msg:
        x=msg.split(":")
        stock_symbol=x[1]
        stock_price= get_stock_price(stock_symbol)
        price=str(stock_price['lowest_price'])
        response = "The lowest price of the given stock is " + price
            
    else:
        response="Please type hi to get started."
    
    return response    


@app.route("/")
def hello():
    return {
        "Result" : "You successed!"
    }

@app.route("/webhook", methods=["POST"]) 
def webhook():
    f = request.form
    msg = f['Body']
    sender = f['From']
    response = process_msg(msg)
    send_msg(response, sender) 
    return "OK", 200

#Steps
 #Get Twilio Account and Token from Twilio and set it in base env.
 # TWILIO_ACCOUNT, TWILIO_TOKEN
 # from twilio.rest import Client
 #

