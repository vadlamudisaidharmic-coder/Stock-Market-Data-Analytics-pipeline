import base64
import json


def lambda_handler(event, context):
    for record in event.get("Records", []):
        try:
            data = base64.b64decode(
                record["kinesis"]["data"]
            ).decode("utf-8")

            stock = json.loads(data)
            symbol = stock.get("symbol")
            price = float(stock.get("price", 0))

            if not symbol or price <= 0:
                print("Invalid stock data")
                continue

            print({
                "symbol": symbol,
                "price": price,
                "anomaly": price > 1000
            })

        except (KeyError, ValueError, TypeError, json.JSONDecodeError) as error:
            print(f"Invalid record: {error}")

    return {"statusCode": 200}