
from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

START = datetime.utcnow()

def uptime():
    delta = datetime.utcnow() - START
    s = int(delta.total_seconds())
    d, s = divmod(s, 86400)
    h, s = divmod(s, 3600)
    m, s = divmod(s, 60)
    return f"{d}d {h}h {m}m"

@app.get("/health")
def health():
    return jsonify({"status": "ok", "time": datetime.utcnow().isoformat()+"Z"})

@app.get("/status")
def status():
    data = {
        "status": "running",
        "uptime": uptime(),
        "processed_today": 482,
        "ai_accuracy": 82,
        "telegram_delivery": 99.1,
        "avg_latency": "1.7s",
        "total_liquidations": 1203,
        "last_update": datetime.utcnow().isoformat()+"Z",
    }
    return jsonify(data)

@app.get("/liquidations")
def liquidations():
    now = datetime.utcnow()
    data = [
        {"id": 1, "symbol": "XRPUSDT", "side": "SELL", "price": 0.5234, "quantity": 15000,
         "timestamp": (now).isoformat()+"Z", "ai_recommendation": "BUY", "confidence": 78, "risk_level": "MEDIUM"},
        {"id": 2, "symbol": "DOGEUSDT", "side": "BUY", "price": 0.118, "quantity": 32000,
         "timestamp": (now).isoformat()+"Z", "ai_recommendation": "HOLD", "confidence": 61, "risk_level": "LOW"},
        {"id": 3, "symbol": "PEPEUSDT", "side": "SELL", "price": 0.0000071, "quantity": 120000000,
         "timestamp": (now).isoformat()+"Z", "ai_recommendation": "SELL", "confidence": 72, "risk_level": "HIGH"},
    ]
    return jsonify(data)

@app.get("/symbols")
def symbols():
    now = datetime.utcnow().isoformat()+"Z"
    data = [
        {"symbol": "XRPUSDT", "status": "active", "websocket_status": "connected", "last_event": now, "today_count": 89},
        {"symbol": "DOGEUSDT", "status": "active", "websocket_status": "connected", "last_event": now, "today_count": 75},
        {"symbol": "PEPEUSDT", "status": "active", "websocket_status": "connected", "last_event": now, "today_count": 56},
    ]
    return jsonify(data)

if __name__ == "__main__":
    # Default to 0.0.0.0:8080 for Docker friendliness
    app.run(host="0.0.0.0", port=8080, debug=True)
