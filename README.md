# 🏥 Smart Health AI

## AI-Powered Public Healthcare Monitoring & Early Warning System

Smart Health AI is an AI-driven healthcare monitoring platform designed to help government administrators monitor hospitals, Community Health Centres (CHCs), and Primary Health Centres (PHCs).

The platform enables health workers to submit real-time facility reports, which are analyzed by an AI engine to generate healthcare insights, early warnings, demand forecasts, and resource optimization recommendations.

---

# 🚀 Project Overview

Healthcare administrators often face challenges in:

* Monitoring multiple healthcare facilities
* Detecting medicine shortages early
* Predicting patient load increases
* Managing available beds and resources
* Identifying facilities requiring immediate intervention

Smart Health AI solves these problems by combining:

* Real-time health reporting
* Cloud-based data storage
* Artificial Intelligence analysis
* Government-level monitoring dashboard

---

# 🔄 System Workflow

```
Health Worker
      |
      ↓
Firebase Authentication
      |
      ↓
Health Facility Report Submission
      |
      ↓
Cloud Firestore Database
      |
      ↓
AI Analysis Engine
      |
      ↓
AI Insights Generated
      |
      ↓
Firestore Updated with AI Results
      |
      ↓
Admin Dashboard Visualization
```

---

# 🤖 Artificial Intelligence Features

## 1. AI Risk Prediction

The AI analyzes healthcare reports and classifies facilities into:

* 🟢 Stable
* 🟡 Attention
* 🔴 Critical

Example:

```
Risk:
Critical

Reason:
High patient load with low medicine availability.
```

---

## 2. AI Early Warning System

The system identifies potential operational issues before they become emergencies.

Examples:

* Medicine may run out soon
* High patient surge expected
* Low bed availability
* Doctor shortage detected
* Additional resources required

AI Output:

```
⚠️ IV Fluids may run out within 24 hours.
⚠️ Patient demand expected to increase.
```

---

## 3. AI Demand Forecasting

The AI predicts future healthcare requirements.

Forecast includes:

### Patient Demand

Example:

```
Expected Patient Increase:
18%
```

### Medicine Demand

Example:

```
Medicine Demand:
Increase by 22%
```

### Bed Demand

Example:

```
Bed Demand:
Need 12 additional beds
```

---

## 4. Smart Resource Redistribution

The AI recommends optimized resource movement between facilities.

Examples:

```
Priority:
High

Action:
Transfer medicine supplies from low-demand facilities
to critical healthcare centers.
```

The system helps administrators decide:

* Where medicines should be transferred
* Which facilities need additional support
* Which areas require urgent attention

---

## 5. District-Level Healthcare Monitoring

The dashboard helps administrators identify priority locations.

AI classifies district intervention level:

```
High
Medium
Low
```

This enables faster government response.

---

# 🖥 Application Modules

## 👨‍⚕️ Health Worker Portal

Health workers can submit:

* Facility information
* Patient count
* Available beds
* Doctor availability
* Medicine inventory
* Diagnostic test availability
* Emergency status
* Situation reports

---

## 🏛️ Admin Intelligence Dashboard

Administrators can monitor:

* Total healthcare facilities
* Critical alerts
* AI-analyzed reports
* Medicine shortage risks
* Facility-wise AI insights
* Demand forecasts
* Resource redistribution suggestions

---

# ✨ Key Features

✅ Firebase Authentication-based login

✅ Multi-user healthcare worker system

✅ Multi-facility monitoring

✅ Real-time Firestore data storage

✅ AI healthcare risk prediction

✅ Medicine stock monitoring

✅ Early warning alerts

✅ Patient demand forecasting

✅ Bed requirement prediction

✅ Resource redistribution recommendations

✅ District-level priority analysis

✅ Live administrator dashboard

---

# 🛠 Technology Stack

## Frontend

* React.js
* Vite
* JavaScript
* CSS

## Backend

* Python
* Flask
* REST API

## Database

* Firebase Authentication
* Cloud Firestore

## Artificial Intelligence

* Groq API
* Llama 3.3 70B Model

## Deployment

* Vercel
* Render

---

# 📂 Project Structure

```
SmartHealthAI
│
├── backend
│   │
│   ├── app.py
│   ├── gemini_service.py
│   ├── firebase_service.py
│   ├── firebase-key.json
│   ├── requirements.txt
│   ├── Procfile
│   └── runtime.txt
│
├── src
│   │
│   ├── pages
│   │   ├── Login.jsx
│   │   ├── HealthWorker.jsx
│   │   └── AdminDashboard.jsx
│   │
│   ├── services
│   │   └── firestore.js
│   │
│   └── firebase.js
│
├── package.json
├── vite.config.js
└── README.md
```

---

# ⚙️ Local Setup Instructions

## Frontend Setup

Install dependencies:

```bash
npm install
```

Run frontend:

```bash
npm run dev
```

Frontend will start:

```
http://localhost:5173
```

---

## Backend Setup

Navigate to backend:

```bash
cd backend
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

Start backend:

```bash
python app.py
```

Backend runs:

```
http://127.0.0.1:5000
```

---

# 🔐 Environment Security

The following files should never be uploaded publicly:

```
.env
firebase-key.json
node_modules
```

Example environment file:

```
GROQ_API_KEY=your_groq_api_key
```

---

# 🗄️ Firestore Data Flow

Health reports are stored inside:

```
facilityReports
```

Each completed AI report contains:

```
aiRisk

aiSummary

aiRecommendation

aiEarlyWarnings

aiDemandForecast

aiResourceRedistribution

aiDistrictPriority
```

---

# 📊 Example AI Analysis Output

```
Facility:
Burari PHC


Risk:
Critical


Summary:
High patient load detected with reduced medicine availability.


Early Warnings:

- Medicine shortage expected soon.
- Additional healthcare staff required.


Demand Forecast:

Patient Increase:
18%

Medicine Demand:
Increase by 22%

Bed Demand:
Need 12 additional beds


Resource Redistribution:

Transfer additional medicine supply
from nearby low-demand facility.


District Priority:

High
```

---

# 🎯 Hackathon Demonstration Flow

1. Health worker logs into the platform.

2. Health worker submits a healthcare facility report.

3. Report is stored securely in Firebase Firestore.

4. Backend triggers AI analysis.

5. AI generates healthcare insights.

6. AI results are stored back into Firestore.

7. Administrator views the AI-powered dashboard.

---

# 🌍 Impact

Smart Health AI helps healthcare administrators:

* Detect problems earlier
* Reduce medicine shortages
* Improve resource allocation
* Monitor multiple facilities
* Make data-driven decisions

---

# 👨‍💻 Project

## Smart Health AI

AI-powered healthcare intelligence platform built using:

React + Firebase + Flask + Artificial Intelligence
