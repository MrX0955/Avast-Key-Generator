import os, subprocess
from datetime   import datetime
from rstr       import xeger
from pystyle    import Colors, Colorate
from colorama   import Fore, init

init(autoreset=True)

class AvastKeyGenerator:
    def __init__(self):
        self.key_pattern = (
            r"MCT[79RBYN2GKZ][XK37BM4FP8Y]-[DZCXBY9NMKJ][NKZBQXR9M27P][HP8DMJRF6XB24][3826MX9K7]"
            r"[BD3FKH2GX8Q7]-[73K28GRN6QJ][6HMG3Y82WCK][HCWFKJ7432D9][D9YXRGPHJK2][6ZT4FNBWQHXD2G]"
            r"-[Y89G2Z3M7FQ][427P8ZNQ93X6][JE7KVDUWGQTZYC][KGUD6HFR98Y][NEP4UDBSVXQ]"
        )
        self.file_name = "keysAvast.txt"
        self.setup_console()

    def setup_console(self):
        if os.name == "nt":
            os.system('title "| Avast Key Generator | Creator: cleinkelvinn |"')
        self.clear_console()

    @staticmethod
    def clear_console():
        os.system("cls" if os.name == "nt" else "clear")

    @staticmethod
    def display_banner():
        banner = """
                                        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
                                        ░░░░░░░░░░▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄░░░░░░░░░
                                        ░░░░░░░░▄▀░░░░░░░░░░░░▄░░░░░░░▀▄░░░░░░░
                                        ░░░░░░░░█░░▄░░░░▄░░░░░░░░░░░░░░█░░░░░░░
                                        ░░░░░░░░█░░░░░░░░░░░░▄█▄▄░░▄░░░█░▄▄▄░░░
                                        ░▄▄▄▄▄░░█░░░░░░▀░░░░▀█░░▀▄░░░░░█▀▀░██░░
                                        ░██▄▀██▄█░░░▄░░░░░░░██░░░░▀▀▀▀▀░░░░██░░
                                        ░░▀██▄▀██░░░░░░░░▀░██▀░░░░░░░░░░░░░▀██░
                                        ░░░░▀████░▀░░░░▄░░░██░░░▄█░░░░▄░▄█░░██░
                                        ░░░░░░░▀█░░░░▄░░░░░██░░░░▄░░░▄░░▄░░░██░
                                        ░░░░░░░▄█▄░░░░░░░░░░░▀▄░░▀▀▀▀▀▀▀▀░░▄▀░░
                                        ░░░░░░█▀▀█████████▀▀▀▀████████████▀░░░░
                                        ░░░░░░████▀░░███▀░░░░░░▀███░░▀██▀░░░░░░
                                        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░"""
        print(Colorate.Horizontal(Colors.purple_to_red, banner, 1))

    @staticmethod
    def get_key_count():
        now = datetime.now().strftime("[%d/%m/%Y %H:%M:%S]")
        while True:
            try:
                count = int(input(f"\n {Fore.LIGHTRED_EX}{now}{Fore.YELLOW} > "
                                  + Colorate.Diagonal(Colors.rainbow, 
                                                      "Enter Key Amount: ", 2)))
                return count
            except ValueError:
                print(Fore.RED + "\n 🔮 Please Select a Number!")

    def generate_keys(self, count):
        with open(self.file_name, "a") as file:
            for _ in range(count):
                key = xeger(self.key_pattern)
                file.write(key + "\n")
        return self.file_name

    def notify_completion(self):
        now = datetime.now().strftime("[%d/%m/%Y %H:%M:%S]")
        print(f"\n {Fore.LIGHTRED_EX}{now}{Fore.YELLOW} > "
              + Colorate.Diagonal(Colors.rainbow, "Keys Has Been Created!", 4))

    def open_file(self):
        now = datetime.now().strftime("[%d/%m/%Y %H:%M:%S]")
        while True:
            qi = input(f"\n {Fore.LIGHTRED_EX}{now}{Fore.YELLOW} > "
                  + Colorate.Diagonal(Colors.rainbow, "Do you want to open saved key file?: (y/n) ", 4)).lower()
            if qi in ["y", "n"]:
                break
            print(Fore.RED + "\n 🔮 Please enter 'y' or 'n'!")

        if qi == "y":
            if os.path.exists(self.file_name):
                try:
                    if os.name == "nt":
                        os.startfile(self.file_name)
                    else:
                        subprocess.call(('xdg-open', self.file_name))
                except Exception as e:
                    print(Fore.RED + f"\n 🔮 Error opening file: {e}")
            else:
                print(Fore.RED + "\n 🔮 File does not exist!")
        else:
            exit()

def main():
    generator = AvastKeyGenerator()
    generator.display_banner()
    count = generator.get_key_count()
    generator.generate_keys(count)
    generator.notify_completion()
    generator.open_file()

if __name__ == "__main__":
    main()

# Updated June 29, 2024 at 3:00 PM ~ Made By CleinKelvinn
