import os
import requests
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

PROMETHEUS_URL = "http://localhost:9090"

def get_metrics(query):
    """Fetches real-time data from Prometheus."""
    response = requests.get(f"{PROMETHEUS_URL}/api/v1/query", params={'query': query})
    results = response.json()['data']['result']
    return results[0]['value'][1] if results else "0"

def ai_quality_gate():
    # 1. Gather 'Golden Signals'
    error_rate = get_metrics('rate(http_requests_total{status=~"5.."}[5m])')
    latency = get_metrics('histogram_quantile(0.95, sum(rate(http_request_duration_seconds_bucket[5m])) by (le))')

    metrics_report = f"Current Error Rate: {error_rate} req/s, P95 Latency: {latency}s"
    print(f"📊 System Report: {metrics_report}")

    # 2. Ask AI to judge the deployment health
    prompt = f"""
    You are an SRE Bot. Analyze these production metrics: {metrics_report}. 
    Thresholds: Error rate > 0.5 is CRITICAL. Latency > 2s is CRITICAL.
    Should we ROLLBACK or CONTINUE the deployment? 
    Respond with ONLY the word 'ROLLBACK' or 'CONTINUE' followed by a 1-sentence reason.
    """

    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )

    decision = completion.choices[0].message.content
    print(f"🤖 AI Decision: {decision}")

if __name__ == "__main__":
    ai_quality_gate()
