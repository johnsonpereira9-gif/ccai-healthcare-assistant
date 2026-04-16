from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    req = request.get_json()

    tag = req.get("fulfillmentInfo", {}).get("tag")
    params = req.get("sessionInfo", {}).get("parameters", {})

    if tag == "book_appointment":
        doctor = params.get("doctor_type")
        date = params.get("appointment_date")

        return jsonify({
            "fulfillment_response": {
                "messages": [{
                    "text": {"text": [f"Appointment confirmed with {doctor} on {date}"]}
                }]
            }
        })

    return jsonify({})
