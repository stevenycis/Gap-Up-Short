from ib_insync import *

account_size = 10000
percentage_of_account_risked_each_trade = 0.05

ticker_to_short = input("What ticker do you want to short?\n")

custom_stop_loss = float(input("Which level (2 decimal points) do you want your stop loss to be? Enter 0 if you want your stop loss to be at the current daily high.\n"))

ib = IB()
ib.connect('127.0.0.1', 7497, clientId=13)

contract = Stock(ticker_to_short, 'SMART', 'USD')
ib.qualifyContracts(contract)

ticker = ib.reqMktData(contract)

ib.sleep(2)

current_price = ticker.last

if custom_stop_loss = float(0):
    stop_loss_price = ticker.high
else 
    stop_loss_price = custom_stop_loss


number_of_shares_to_short = (account_size * percentage_of_account_risked_each_trade) / (stop_loss_price - current_price)
number_of_shares_to_short = int(number_of_shares_to_short)



order = MarketOrder('SELL', number_of_shares_to_short)    # Short 

# Define stop loss and take profit orders
stopLossOrder = StopOrder('BUY', number_of_shares_to_short, stop_loss_price)  # Stop loss
takeProfitOrder = LimitOrder('BUY', number_of_shares_to_short, current_price - (stop_loss_price - current_price))  # Take profit

# Create the bracket order
bracketOrder = BracketOrder(order, takeProfitOrder, stopLossOrder)

trade = ib.placeOrder(contract, order)

ib.disconnect()

