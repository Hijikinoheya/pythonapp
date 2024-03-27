import paramiko
import time

class SSHClient:
    def __init__(self):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def connect(self, host, username, password):
        print(f"Connecting to {host}...")
        time.sleep(1)  # Loading画面のために1秒待機
        try:
            self.client.connect(hostname=host, username=username, password=password)
            print("Connected to SSH server.")
        except paramiko.AuthenticationException:
            print("Authentication failed. Please check your credentials.")
        except paramiko.SSHException as e:
            print(f"SSH error: {e}")
        except Exception as e:
            print(f"Error: {e}")

    def run_command(self, command):
        stdin, stdout, stderr = self.client.exec_command(command)
        print(stdout.read().decode("utf-8"))

    def disconnect(self):
        self.client.close()
        print("Disconnected from SSH server.")

if __name__ == "__main__":
    ssh_client = SSHClient()
    host = input("Enter SSH server hostname/IP: ")
    username = input("Enter SSH username: ")
    password = input("Enter SSH password: ")
    ssh_client.connect(host, username, password)

    while True:
        command = input(f"{host} $ ").strip()
        if command == "exit":
            break
        else:
            ssh_client.run_command(command)

    ssh_client.disconnect()
