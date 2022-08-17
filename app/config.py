import os
from flask import current_app as app

def get_db_credentials():
    try:
        username = os.environ["DB_USERNAME"]
        password = os.environ["DB_PASSWORD"]
        host = os.environ["DB_HOST"]
        port = os.environ["DB_PORT"]
        database = os.environ["DB_DATABASE"]
    except KeyError as err:
        app.logger.error(f"""You need to set the following environment variables for the server to work properly:
DB_USERNAME
DB_PASSWORD
DB_HOST
DB_PORT
DB_DATABASE     
""")
        raise err
    return username, password, host, port, database
