import re

log_file = "sample.log"

failed_attempts = {}

with open(log_file, "r") as file:
    for line in file:
        if "Failed password" in line:
            ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}', line)
            if ip:
                ip = ip[0]
                if ip in failed_attempts:
                    failed_attempts[ip] += 1
                else:
                    failed_attempts[ip] = 1

print("\nFailed Login Attempts:\n")

for ip, count in failed_attempts.items():
    print(f"{ip} → {count} times")

print("\nSuspicious IPs (more than 3 attempts):\n")

for ip, count in failed_attempts.items():
    if count > 3:
        print(ip)
