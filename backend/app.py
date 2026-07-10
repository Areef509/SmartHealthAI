from flask import Flask, jsonify
from flask_cors import CORS

from firebase_service import db
from gemini_service import analyze_report

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return "Smart Health AI Backend Running"


@app.route("/analyze-pending")
def analyze_pending():

    reports = (
        db.collection("facilityReports")
        .where("status", "==", "pending_ai")
        .stream()
    )

    processed = 0

    for doc in reports:

        report = doc.to_dict()

        print(f"Analyzing report: {doc.id}")

        analysis = analyze_report(report)

        db.collection("facilityReports").document(doc.id).update({

            # Existing AI Fields
            "aiRisk": analysis.get("risk"),
            "aiSummary": analysis.get("summary"),
            "aiRecommendation": analysis.get("recommendation"),
            "confidence": analysis.get("confidence"),

            # NEW AI Features
            "aiEarlyWarnings": analysis.get("earlyWarnings", []),

            "aiDemandForecast": analysis.get(
                "demandForecast",
                {
                    "expectedPatientIncrease": "",
                    "medicineDemand": "",
                    "bedDemand": ""
                }
            ),

            "aiResourceRedistribution": analysis.get(
                "resourceRedistribution",
                {
                    "priority": "",
                    "action": ""
                }
            ),

            "aiDistrictPriority": analysis.get(
                "districtPriority",
                ""
            ),

            "status": "completed"

        })

        processed += 1

    return jsonify({
        "success": True,
        "processed": processed
    })


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    ) 