import os
import json
import time

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

if not API_KEY:
    raise Exception(
        "GROQ_API_KEY not found. Check your backend/.env file."
    )

client = Groq(api_key=API_KEY)

MODEL_NAME = "llama-3.3-70b-versatile"


def analyze_report(report):

    report_json = json.dumps(
        report,
        indent=2,
        default=str
    )

    prompt = f"""
You are an AI Healthcare Monitoring Assistant for the Government of NCT of Delhi.

You monitor:

- Government Hospitals
- Community Health Centres (CHCs)
- Primary Health Centres (PHCs)

Analyze the following healthcare report.

Healthcare Report

{report_json}

Tasks

1. Determine healthcare risk.
2. Summarize the operational situation.
3. Recommend actions.
4. Predict medicine shortages.
5. Forecast patient demand.
6. Forecast medicine demand.
7. Forecast bed demand.
8. Recommend redistribution of medicines, beds or staff.
9. Assign government intervention priority.

Risk must be one of:

Stable
Attention
Critical

Return ONLY valid JSON.

Required JSON fields

risk
summary
recommendation
confidence
earlyWarnings
demandForecast
resourceRedistribution
districtPriority

Requirements

risk:
Stable, Attention or Critical.

confidence:
Number between 0 and 100.

earlyWarnings:
Return an array containing 2 to 4 operational warnings.

Example warnings:

- IV Fluids may run out within 24 hours.
- High patient surge expected tomorrow.
- Low bed availability.
- Deploy additional medical staff immediately.

demandForecast:
Return an object containing

expectedPatientIncrease
medicineDemand
bedDemand

Example values:

expectedPatientIncrease = 18%
medicineDemand = Increase by 22%
bedDemand = Need 12 additional beds

resourceRedistribution:

Return an object with

priority
action

Example

Priority = High

Action = Transfer 200 IV Fluids from Burari PHC to Rampur PHC.

districtPriority:

Return one value only

High
Medium
Low

Return JSON only.

Do not use Markdown.
"""

    retries = 3

    for attempt in range(retries):

        try:

            response = client.chat.completions.create(
                model=MODEL_NAME,
                temperature=0.2,
                response_format={
                    "type": "json_object"
                },
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            text = response.choices[0].message.content.strip()

            result = json.loads(text)

            return result

        except Exception as error:

            print(
                f"Groq attempt {attempt + 1} failed:",
                error
            )

            if attempt < retries - 1:

                wait = (attempt + 1) * 3

                print(
                    f"Retrying after {wait} seconds..."
                )

                time.sleep(wait)

            else:

                raise