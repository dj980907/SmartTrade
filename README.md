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

to insert datas,

use the following: 

INSERT INTO {{table_name}} ({{column_names}}) VALUES ({{actual_values_of_columns}})

for example,

```
INSERT INTO stock (symbol, company) VALUES ('AAPL', 'Apple');
```



to read the datas from sql database, use this:


SELECT {{what_you_want_to_read}} from {{table}}


for example,

```
SELECT * from stock;
```

to update the data, use this:

UPDATE {{table_name}} SET {{column_you_want_to_update}} = '{value}' WHERE {{condition}};

```
UPDATE stock SET company = 'Apple INC.' WHERE id = 1;
```

to de3lete the data, use this:

DELETE FROM {{table_name}} where {{condition}};

```
DELETE FROM stock where id = 3;
```




### API
i am going to use Alpaca API.


to check the stock prices are populated well, 
```
SELECT symbol,date,open,high,low,close
FROM stock_price
JOIN stock on stock.id = stock_price.stock_id
WHERE symbol='AAPL'
ORDER BY date;
```


to run the main.py
```
uvicorn main:app --reload
```

I am using Fast API and Semantic UI

DOne with part 6