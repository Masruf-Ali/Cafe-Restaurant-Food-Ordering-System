from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def db():
    return sqlite3.connect("cafe.db")

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    if data["username"] == "admin" and data["password"] == "admin123":
        return jsonify({"role":"admin"})
    elif data["username"] == "user" and data["password"] == "user123":
        return jsonify({"role":"user"})
    return jsonify({"error":"Invalid credentials"}), 401

@app.route("/admin/orders")
def admin_orders():
    con = db()
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS orders(item TEXT, price INT)")
    cur.execute("SELECT * FROM orders")
    orders = cur.fetchall()
    con.close()
    return jsonify(orders)

@app.route("/order/add", methods=["POST"])
def add_order():
    item = request.json["item"]
    price = request.json["price"]
    con = db()
    cur = con.cursor()
    cur.execute("INSERT INTO orders VALUES (?,?)",(item,price))
    con.commit()
    con.close()
    return jsonify({"msg":"added"})

if __name__ == "__main__":
     app.run(host="0.0.0.0", port=8080)
