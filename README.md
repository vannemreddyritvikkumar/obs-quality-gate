# obs-quality-gate
This project builds an automated "Quality Gate" that doesn't look at test results, but at system health metrics.
# 📉 AI-Powered Observability Quality Gate

This project demonstrates **Shift-Right Testing** and **AI-Driven Reliability Engineering**. It bridges the gap between automated testing and production monitoring.

### 🎯 The Problem
Traditional CI/CD gates only check if tests pass. However, many bugs (memory leaks, race conditions) only appear under production load. Static thresholds often trigger "false alarms," leading to "alert fatigue."

### 🧠 The AI Solution
An automated SRE Agent that:
1.  **Polls Prometheus:** Collects "Golden Signals" (Latency, Errors, Traffic).
2.  **Contextual Analysis:** Uses **GPT-4o** to determine if a metric spike is a critical failure or a normal pattern (e.g., a planned marketing spike).
3.  **Automated Governance:** Decides whether to `CONTINUE` or `ROLLBACK` the deployment based on real-time health data.

### 🛠 Tech Stack
- **Python** (Logic)
- **Prometheus** (Metrics Source)
- **OpenAI API** (Decision Engine)
- **Grafana** (Visualization)

### 🚀 Business Impact
- **Zero-Downtime Reliability:** Catch production failures within 60 seconds of deployment.
- **SRE Efficiency:** Reduces manual monitoring time for QA and DevOps teams.
