import os

class CuiNotepad:
    def __init__(self):
        self.current_file = None
        self.file_content = ""
        self.is_editing = False

    def run(self):
        while True:
            command = input("Notepad $ ").strip()  
            if command == "new":
                self.new_file()
            elif command.startswith("open "):
                filename = command.split(" ", 1)[1]
                self.open_file(filename)
            elif command == "save":
                self.save_file()
            elif command == "saveas":
                filename = input("Enter file name to save as: ").strip()
                self.save_file(filename)
            elif command == "read":
                self.read_file()
            elif command == "edit":
                self.edit_file()
            elif command == "exit":  # quitコマンドをexitコマンドに変更
                print("Exiting the Notepad.")
                break
            elif command.startswith("^save"):
                self.save_file()
            elif command == ":help":
                self.show_help()
            else:
                print("Command not recognized. Type ':help' for available commands.")

    def new_file(self):
        self.current_file = None
        self.file_content = ""
        print("New file created.")

    def open_file(self, filename):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                self.file_content = file.read()
                self.current_file = filename
                print(f"Opened file: {filename}")
        except UnicodeDecodeError:  
            with open(filename, "rb") as file:
                self.file_content = file.read().decode("utf-8")  
                self.current_file = filename
                print(f"Opened file (binary mode): {filename}")
        except FileNotFoundError:
            print(f"File '{filename}' not found.")

    def save_file(self, filename=None):
        if not filename and not self.current_file:
            print("No file name provided. Use 'saveas' command to specify a file name.")
            return

        if not filename:
            filename = self.current_file

        if filename:
            with open(filename, "w", encoding="utf-8") as file:  
                file.write(self.file_content)
                self.current_file = filename
                print(f"File saved as: {filename}")
        else:
            print("No file to save.")

    def read_file(self):
        if self.current_file:
            print("Current file content:")
            print(self.file_content)
        else:
            print("No file open.")

    def edit_file(self):
        if self.current_file:
            print("Editing current file. Enter text. Type ':w' to save and ':q' to exit without saving.")
            self.is_editing = True
            self.file_content = ""
            while self.is_editing:
                line = input()
                if line == ":q":
                    print("Exiting edit mode without saving.")
                    break
                elif line == ":w":
                    self.save_file(self.current_file)  
                    print("File saved.")
                    break
                else:
                    self.file_content += line + "\n"
            print("File edited.")
        else:
            print("No file open.")

    def show_help(self):
        print("Available commands:")
        print("new - Create a new file")
        print("open <filename> - Open a file")
        print("save - Save the current file")
        print("saveas - Save the current file with a new name")
        print("read - Display the content of the current file")
        print("edit - Edit the content of the current file")
        print("exit - Exit the Notepad")  # quitコマンドをexitコマンドに変更
        print(":help - Show available commands")

if __name__ == "__main__":
    current_directory = os.path.dirname(os.path.abspath(__file__))  
    os.chdir(current_directory)  
    notepad = CuiNotepad()
    notepad.run()
