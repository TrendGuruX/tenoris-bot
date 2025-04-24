from flask import Flask, request, jsonify
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()

    symbol = data.get('symbol')
    side = data.get('side')
    entry = float(data.get('entry'))
    tp = float(data.get('tp'))
    sl = float(data.get('sl'))

    logging.info(f"Alert received: {side.upper()} {symbol} | Entry: {entry} | TP: {tp} | SL: {sl}")
    print(f"Trade: {side.upper()} {symbol} | Entry {entry} | TP {tp} | SL {sl}")

    return jsonify({"status": "received"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
