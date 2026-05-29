# SSHBruteForce

A simple Python tool that uses the Paramiko library to perform SSH authentication testing against a target host using username and password wordlists.

## Features

- SSH authentication using Paramiko
- Supports custom username wordlists
- Supports custom password wordlists
- Configurable target IP and port
- Displays valid credentials when authentication succeeds
- Handles connection and authentication errors gracefully

## Requirements

- Python 3.x
- Paramiko

Install the required dependency:

```bash
pip install paramiko
```

## Usage

```bash
python SSHBruteForce.py <ip> <port> <username_file> <password_file>
```

### Example

```bash
python SSHBruteForce.py 192.168.1.100 22 usernames.txt passwords.txt
```

## Arguments

| Argument | Description |
|----------|-------------|
| `ip` | Target IP address |
| `port` | SSH port number |
| `username_file` | File containing usernames (one per line) |
| `password_file` | File containing passwords (one per line) |

## Wordlist Format

### usernames.txt

```text
admin
root
user
test
```

### passwords.txt

```text
password
admin123
toor
123456
```

## Sample Output

```text
[*] Starting SSH brute force on 192.168.1.100:22

Trying: admin : password
Trying: root : toor

[✔] LOGIN SUCCESSFUL!
[+] Username: root
[+] Password: toor
```

## Project Structure

```text
.
├── SSHBruteForce.py
├── usernames.txt
├── passwords.txt
└── README.md
```

## Disclaimer

This project is intended for educational purposes and authorized security assessments only.

Use this tool only against systems you own or have explicit permission to test. Unauthorized access attempts may violate applicable laws and regulations.

## Author

**Harsh Web Cyber**
