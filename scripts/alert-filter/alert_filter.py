import argparse
import csv

SUSPICIOUS_KEYWORDS = [
    "failed",
    "unauthorized",
    "denied",
    "login attempt",
    "error"
]

def filter_alerts(logfile):
    alerts = []

    with open(logfile, "r") as f:
        for line in f:
            lower_line = line.lower()
            for keyword in SUSPICIOUS_KEYWORDS:
                if keyword in lower_line:
                    alerts.append(line.strip())
                    break

    return alerts

def save_to_csv(alerts, output_file):
    with open(output_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["alert"])
        for alert in alerts:
            writer.writerow([alert])

    print(f"Alerts saved to {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Filter suspicious alerts from logs")
    parser.add_argument("logfile", help="Log file to analyze")
    parser.add_argument("--csv", help="Optional CSV output file")
    args = parser.parse_args()

    alerts = filter_alerts(args.logfile)

    if alerts:
        print("Suspicious Alerts Found:")
        for alert in alerts:
            print(alert)
    else:
        print("No suspicious alerts detected.")

    if args.csv and alerts:
        save_to_csv(alerts, args.csv)

if __name__ == "__main__":
    main()
