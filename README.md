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

run the command:

```
sqlite3 app.db
```

```
CREATE TABLE IF NOT EXISTS stock (
    id INTEGER PRIMARY KEY,
    symbol TEXT NOT NULL UNIQUE,
    company TEXT NOT NULL
);
```

if you want to see that you actually created the table, enter this:

```
.schema
```

add stock price data:

```
CREATE TABLE IF NOT EXISTS stock_price (
    id INTEGER PRIMARY KEY,
    stock_id INTEGER,
    date NOT NULL,
    open NOT NULL,
    high NOT NULL,
    low NOT NULL,
    close NOT NULL,
    adjusted_close NOT NULL,
    volume NOT NULL,
    FOREIGN KEY (stock_id) REFERENCES stock (id)
);
```