# Intro to SIEM – Notes

## Key Takeaways
- SIEM collects and correlates logs from multiple sources.
- Detection rules in SIEM define conditions that trigger alerts.
- Examples of detection rules:
    - 5 failed login attempts in 10 seconds → alert for multiple failed login attempts
    - Successful login after multiple failures → alert for suspicious login
    - USB plugged in → alert if restricted
- Event logs and field-value pairs are critical; normalized logs are needed for accurate alerts.

## Alert Investigation Workflow
1. Alerts appear on dashboards for monitoring.
2. Examine events associated with the alert.
3. Check which detection rule conditions were met.
4. Determine if the alert is a **True Positive** or **False Positive**.
    - **False Positive** → may require tuning the detection rule
    - **True Positive** → further investigation, notify asset owner, isolate host if needed
5. Isolate host

## Examples Learned
- Event ID 104 → logged when someone removes/clears event logs
- Event ID 4688 → process execution, useful to detect commands like `whoami`
- Tuning rules reduces false positives and improves SOC efficiency
