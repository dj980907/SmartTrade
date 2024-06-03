# SmartTrade

## how i design the database
i will ahve relational data base.

this is what stock data looks like:

| key | Description |
| :---: | :---: |
| ID | primary |
| Symbol | text |
| Company | text |

for example,

| key | Description |
| :---: | :---: |
| ID | 1 |
| Symbol | APPL |
| Company | APPLE INC |

this is what stock price data looks like:

| key | Description |
| :---: | :---: |
| ID | Primary |
| Stock_ID | Foreign Key |
| Date | text |
| Open | text |
| High | text |
| Low | text |
| Close | text |

the stock price will be pointing to the stock data table, which means that stockID will have a foreign key of stock data