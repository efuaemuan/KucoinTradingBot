# KuCoin Trading Bot
This is a python program designed to buy and sell coins on the cryptocurrency exchange platform, KuCoin. The program uses KuCoin's API to get the user's secret key and passphrase. The bot will buy a predetermined coin at its best market price, it will then wait for the buy price to increase by a predetermined percentage (1.2% by default). The user would have to set their API restriction to 'General' and 'Trade' for this operation to be possible.

No stoplosss feature is implemented, the bot will not make any trade until the price of the coin reaches its predetermined 'take_profit' percentage.

## Disclaimer
This is a personal experimental project, I am not responsible for how this program is used.
