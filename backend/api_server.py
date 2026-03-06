from flask import Flask, jsonify, render_template
import sqlite3
import os

app = Flask(__name__, template_folder="templates")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db_path = os.path.join(BASE_DIR, "database", "traffic.db")


def get_db_connection():
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


# -----------------------------
# Dashboard Route
# -----------------------------
@app.route("/")
def dashboard():
    return render_template("index.html")


# -----------------------------
# Latest Traffic
# -----------------------------
@app.route("/api/traffic")
def get_traffic():

    conn = get_db_connection()

    rows = conn.execute(
        "SELECT * FROM traffic ORDER BY time DESC LIMIT 20"
    ).fetchall()

    conn.close()

    data = [dict(row) for row in rows]

    return jsonify(data)


# -----------------------------
# Protocol Statistics
# -----------------------------
@app.route("/api/protocols")
def protocol_stats():

    conn = get_db_connection()

    rows = conn.execute("""
        SELECT protocol, COUNT(*) as count
        FROM traffic
        GROUP BY protocol
    """).fetchall()

    conn.close()

    data = [dict(row) for row in rows]

    return jsonify(data)


# -----------------------------
# Top Source IPs
# -----------------------------
@app.route("/api/top_ips")
def top_ips():

    conn = get_db_connection()

    rows = conn.execute("""
        SELECT src_ip, COUNT(*) as count
        FROM traffic
        GROUP BY src_ip
        ORDER BY count DESC
        LIMIT 10
    """).fetchall()

    conn.close()

    data = [dict(row) for row in rows]

    return jsonify(data)


# -----------------------------
# Security Alerts API
# -----------------------------
@app.route("/api/alerts")
def get_alerts():

    conn = get_db_connection()

    rows = conn.execute("""
        SELECT * FROM alerts
        ORDER BY time DESC
        LIMIT 10
    """).fetchall()

    conn.close()

    data = [dict(row) for row in rows]

    return jsonify(data)


# -----------------------------
# Start Server
# -----------------------------
if __name__ == "__main__":
    print("Starting API server...\n")
    app.run(debug=True)