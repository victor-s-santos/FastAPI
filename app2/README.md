# Stock Screener
>This application is a Stock Screener dashboard where are listed many informations about the stocks.

# Content
- I am using sqlalchemy to create my models and my database schema;
- yfinance to get stocks informations;
- pydantic to use Basemodel;
- jinja2 to render the html templates;
- BackgroundTasks to execute the background action after the post has submitted;

# BackgroundTasks
> Everytime a stock has submitted, the fetch_stock_data is added to background tasks. Therefore, the information about the submitted stock will be fetched in background action.

