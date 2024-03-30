import psutil
import platform
import threading
import time
import os

class TaskManager:
    def __init__(self):
        self.running = False

    def run(self):
        print("Welcome to Task Manager!")
        self.running = True
        info_thread = threading.Thread(target=self.update_info)
        info_thread.daemon = True
        info_thread.start()
        while self.running:
            try:
                command = input("Task Manager $ ").strip()
                if command == "list":
                    self.list_processes()
                elif command.startswith("kill "):
                    pid = int(command.split(" ", 1)[1])
                    self.kill_process(pid)
                elif command == "info":
                    self.show_info()
                elif command == "exit":
                    print("Exiting Task Manager.")
                    self.running = False
                elif command == "help":
                    self.show_help()
                else:
                    print("Command not recognized. Type 'help' for available commands.")
            except KeyboardInterrupt:
                print("KeyboardInterrupt detected. Exiting Task Manager.")
                self.running = False

    def update_info(self):
        while self.running:
            self.clear_screen()
            self.show_info()
            time.sleep(1)  

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear') 

    def list_processes(self):
        print("Listing currently running processes:")
        processes = psutil.process_iter()
        for process in processes:
            print(f"PID: {process.pid}, Name: {process.name()}")

    def kill_process(self, pid):
        try:
            process = psutil.Process(pid)
            process.terminate()
            print(f"Process with PID {pid} terminated.")
        except psutil.NoSuchProcess:
            print(f"No process found with PID {pid}.")
        except psutil.AccessDenied:
            print(f"Access denied. Unable to terminate process with PID {pid}.")

    def show_info(self):
        print("System Information:")
        print(f"OS: {platform.system()} {platform.release()}")
        print(f"CPU: {psutil.cpu_percent()}%")
        self.display_gpu_info()
        self.display_disk_info()
        self.display_memory_info()

    def display_gpu_info(self):
        try:
            import GPUtil
            gpus = GPUtil.getGPUs()
            if gpus:
                for i, gpu in enumerate(gpus):
                    print(f"GPU {i + 1}: {gpu.name}, Utilization: {gpu.load * 100}%")
            else:
                print("No GPUs found.")
        except ImportError:
            print("GPU information not available. GPUtil module not found.")

    def display_disk_info(self):
        print("Disk Information:")
        partitions = psutil.disk_partitions()
        for partition in partitions:
            print(f"Device: {partition.device}, Mountpoint: {partition.mountpoint}")

    def display_memory_info(self):
        memory = psutil.virtual_memory()
        print(f"Total RAM: {self._format_bytes(memory.total)}")
        print(f"Available RAM: {self._format_bytes(memory.available)}")
        print(f"Used RAM: {self._format_bytes(memory.used)}")
        print(f"RAM Usage: {memory.percent}%")

    def _format_bytes(self, bytes):
        suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
        index = 0
        while bytes >= 1024 and index < len(suffixes) - 1:
            bytes /= 1024
            index += 1
        return f"{bytes:.2f} {suffixes[index]}"

    def show_help(self):
        print("Available commands:")
        print("list - List currently running processes")
        print("kill <PID> - Terminate process with specified PID")
        print("info - Display system information")
        print("help - Show available commands")
        print("exit - Exit the Task Manager")

if __name__ == "__main__":
    task_manager = TaskManager()
    task_manager.run()
