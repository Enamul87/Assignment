#Q1
def convert_to_uppercase(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                print(line.upper(), end='')
    except FileNotFoundError:
        print("Error: File not found.")
        exit(1)


if __name__ == "__main__":
    file_name = input("Enter the file name: ")
    convert_to_uppercase(file_name)
def convert_to_uppercase(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                print(line.upper(), end='')
    except FileNotFoundError:
        print("Error: File not found.")
        exit(1)


if __name__ == "__main__":
    file_name = input("Enter the file name: ")
    convert_to_uppercase(file_name)

#Q2
import re

def extract_email_hosts(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.readlines()
            pattern = r"^From:.*@([A-Za-z0-9.-]+)"
            hosts = []
            for line in content:
                match = re.match(pattern, line)
                if match:
                    hosts.append(match.group(1))
            for host in hosts:
                print(host)
            print(f"Number of hosts: {len(hosts)}")
    except FileNotFoundError:
        print("Error: File not found.")
        exit(1)

if __name__ == "__main__":
    file_name = "mbox.txt"
    extract_email_hosts(file_name)

#Q3

def find_average_spam_confidence(file_name):
    try:
        with open(file_name, 'r') as file:
            total_confidence = 0
            count = 0
            for line in file:
                if line.startswith('X-DSPAM-Confidence:'):
                    try:
                        confidence = float(line.split(":")[1])
                        total_confidence += confidence
                        count += 1
                    except ValueError:
                        continue

            if count > 0:
                average_confidence = total_confidence / count
                print(f"Average spam confidence: {average_confidence}")
            else:
                print("No X-DSPAM-Confidence lines found in the file.")

    except FileNotFoundError:
        print("Error: File not found.")
        exit(1)

if __name__ == "__main__":
    file_name = input("Enter the file name: ")
    find_average_spam_confidence(file_name)

