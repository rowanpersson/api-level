from flask import Flask, render_template
import pyodbc

app = Flask(__name__)

def connection():
    s = 'A-PF1F43HN\SQLEXPRESS'
    d = 'App_Data' 
    u = 'sa'
    p = 'password123!'
    cstr = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+s+';DATABASE='+d+';UID='+u+';PWD='+p
    conn = pyodbc.connect(cstr)
    return conn

@app.route('/')
def main():
    customers = []
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM dbo.customers")
    for row in cursor.fetchall():
        customers.append({"customer_id": row[0], "customer_name": row[1]})
    conn.close()
    return render_template("base.html", customers = customers)

if(__name__ == "__main__"):
    app.run()
