import sqlite3, config
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
def index(request: Request):
    print(dir(request))
    # connect to the database
    connection = sqlite3.connect(config.DB_FILE)
    connection.row_factory = sqlite3.Row

    # create a cursor
    cursor = connection.cursor()

    # get all the companies that we have in the database
    cursor.execute("""
        SELECT id, symbol, name FROM stock ORDER BY symbol
    """)

    # fetch all the datas and store them in rows
    rows = cursor.fetchall()


    return templates.TemplateResponse("index.html", {"request": request, "stocks": rows})


@app.get("/stock/{symbol}")
def stock_detail(request: Request, symbol):

    # connect to the database
    connection = sqlite3.connect(config.DB_FILE)
    connection.row_factory = sqlite3.Row

    # create a cursor
    cursor = connection.cursor()

    # get all the companies that we have in the database
    cursor.execute("""
        SELECT id, symbol, name FROM stock WHERE symbol = ?
    """, (symbol,))

    # fetch all the datas and store them in rows
    row = cursor.fetchone()

    cursor.execute("""
        SELECT * FROM stock_price WHERE stock_id = ? ORDER BY date DESC
    """, (row['id'],))

    prices = cursor.fetchall()

    return templates.TemplateResponse("stock_detail.html", {"request": request, "stock": row, "bars": prices})