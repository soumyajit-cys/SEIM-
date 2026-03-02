SIEM-Lite
Lightweight Security Information and Event Management System

A production-style Security Information and Event Management (SIEM) system built using Python, FastAPI, Elasticsearch, and Redis.

SIEM-Lite demonstrates centralized log collection, normalization, rule-based threat detection, anomaly detection, and real-time alerting — conceptually aligned with enterprise SIEM platforms such as:

Splunk

Elastic Security

IBM QRadar

📌 Project Overview

SIEM-Lite is a lightweight, modular, and Dockerized SIEM platform designed for:

Collecting logs from multiple sources

Parsing and normalizing events

Detecting threats in real time

Generating alerts

Providing searchable APIs

Demonstrating detection engineering principles

This project showcases backend engineering, cybersecurity detection logic, and DevOps deployment skills.

🏗 Architecture
Log Sources
    ↓
FastAPI Ingestion API
    ↓
Parser Engine (Regex-based)
    ↓
Detection Engine
   ├── Rule-based detection
   ├── Statistical anomaly detection (Z-score)
    ↓
Redis (Sliding window counters)
    ↓
Elasticsearch (Logs + Alerts indices)
    ↓
Alert Engine (Email + Slack)
🚀 Features
Log Management

Async log ingestion API

JSON log input

Source-based parser modules

Normalized event schema

Daily Elasticsearch indices (logs-YYYY-MM-DD)

Detection Capabilities
Rule-Based Detection

SSH Brute Force Detection

Blacklisted IP Detection

Privilege Escalation Attempts

Statistical Anomaly Detection

Moving average

Standard deviation

Z-score threshold-based spike detection

Alerting

Email alerts (SMTP)

Slack webhook alerts

Alerts stored in Elasticsearch

Severity levels (low / medium / high / critical)

DevOps

Dockerized stack

Elasticsearch container

Redis container

FastAPI container

Environment-based configuration

📂 Project Structure
siem-lite/
├── api/
├── ingestion/
├── parsers/
├── detection/
├── alerts/
├── storage/
├── models/
├── config/
├── docker/
├── tests/
└── README.md
⚙️ Tech Stack

Backend: Python + FastAPI
Search Engine: Elasticsearch
Cache & Counters: Redis
Parsing: Regex-based
Alerting: SMTP + Slack Webhook
Deployment: Docker + Docker Compose

🔧 Installation & Setup (Linux)
1️⃣ Clone Repository
git clone https://github.com/yourusername/siem-lite.git
cd siem-lite/docker
2️⃣ Start SIEM Stack
docker compose up --build

This will start:

Elasticsearch → port 9200

Redis → port 6379

FastAPI backend → port 8000

3️⃣ Access Services

FastAPI Swagger UI:

http://localhost:8000/docs

Elasticsearch:

http://localhost:9200
🧪 Example Usage
Ingest Log
curl -X POST http://localhost:8000/ingest \
-H "Content-Type: application/json" \
-d '{
  "source": "linux-auth",
  "host": "192.168.1.10",
  "log": "Failed password for root from 10.0.0.5 port 22",
  "timestamp": "2026-02-19T10:00:00"
}'
View Alerts
http://localhost:8000/alerts
🔐 Use Case: SSH Brute Force Attack

Scenario:

Attacker IP: 10.0.0.5
Target User: root

Flow:

Multiple failed login attempts are ingested

Redis sliding window counter increments

Threshold exceeded (5 attempts in 2 minutes)

Alert generated

Alert stored in Elasticsearch

Slack/Email notification sent

📊 Detection Engine Design
Sliding Window Counter

Redis is used to maintain time-bound counters for rule evaluation.

Rule Format
{
  rule_name
  event_type
  threshold
  time_window
  severity
}
Z-Score Formula
Z = (X - Mean) / StandardDeviation

Triggers anomaly alert if:

|Z| >= 3
🛡 Security Capabilities Demonstrated

Detection engineering

Stateful event correlation

Real-time alerting

Log normalization

Rule-based threat detection

Basic UEBA-style anomaly detection

Containerized security architecture

🏭 Industry Mapping
SIEM-Lite Component	Enterprise Equivalent
Rule Engine	Correlation Searches (Splunk)
Elasticsearch Index	Elastic Stack
Alert Engine	QRadar Offense Manager
Redis Counters	Stateful Detection
Z-Score Detection	UEBA
🧠 Skills Demonstrated

Backend system design

Async programming

Elasticsearch indexing

Redis-based detection logic

Dockerized microservices

Cybersecurity analytics

Threat modeling

SIEM architecture fundamentals

📌 Future Enhancements

JWT Authentication

Role-Based Access Control

MITRE ATT&CK mapping

Geo-IP integration

Threat Intelligence API integration

Real-time WebSocket streaming

React Dashboard UI

Kafka ingestion pipeline

👨‍💻 Author

Soumyajit Dutta
Cybersecurity Enthusiast | Detection Engineering | Backend Systems
