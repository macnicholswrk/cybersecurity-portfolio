
"""
log_parse.py
A simple Python log parser for cybersecurity portfolio projects.
"""

import re
import csv
import argparse

# Regex pattern for a generic log line: [timestamp] [LEVEL] message
LOG_PATTERN = re.compile(r'\[(.*?)\]\s+\[(.*?)\]\s+(.*)')

def parse_log(file_path):
    """Parse the log file and return a list of entries"""
    entries = []
    with open(file_path, 'r') as f:
        for line in f:
            match = LOG_PATTERN.match(line)
            if match:
                timestamp, level, message = match.groups()
                entries.append({
                    'timestamp': timestamp,
                    'level': level,
                    'message': message.strip()
                })
    return entries

def count_levels(entries):
    """Count the occurrences of each log level"""
    counts = {}
    for entry in entries:
        level = entry['level']
        counts[level] = counts.get(level, 0) + 1
    return counts

def save_to_csv(entries, output_file):
    """Save log entries to a CSV file"""
    keys = ['timestamp', 'level', 'message']
    with open(output_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(entries)
    print(f"Saved parsed logs to {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Parse log files")
    parser.add_argument('logfile', help='Path to the log file')
    parser.add_argument('--csv', help='Optional CSV output file')
    parser.add_argument('--filter', help='Optional log level to filter by (e.g., ERROR)')
    args = parser.parse_args()

    entries = parse_log(args.logfile)

    if args.filter:
        entries = [e for e in entries if e['level'] == args.filter]

    counts = count_levels(entries)
    print("Log level counts:", counts)

    for entry in entries:
        print(f"[{entry['timestamp']}] [{entry['level']}] {entry['message']}")

    if args.csv:
        save_to_csv(entries, args.csv)

if __name__ == "__main__":
    main()
