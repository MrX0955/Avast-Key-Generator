from pystyle    import Colors, Colorate
from colorama   import Fore
from datetime   import datetime
from rstr       import xeger
from os         import system, name, path

system('title "| Avast Key Generator | Developer: cleinkelvinn |"')
system("cls" if name == "nt" else "clear")

class generate:
    print(
        Colorate.Horizontal(
            Colors.purple_to_red,
            """
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
                                        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░""",
            1,
        )
    )
    now = datetime.now()
    current_time = now.strftime("[%d/%m/%Y %H:%M:%S]")
    limit = int(
        input(
            f"\n {Fore.LIGHTRED_EX}{current_time}{Fore.YELLOW} > "
            + Colorate.Diagonal(
                Colors.rainbow, "Kaç Tane Key Oluşturmak İstiyorsunuz: ", 2
            )
        )
    )
    umm = 0
    while umm < limit:
        mrx = xeger(
            r"MCT[79RBYN2GKZ][XK37BM4FP8Y]-[DZCXBY9NMKJ][NKZBQXR9M27P][HP8DMJRF6XB24][3826MX9K7][BD3FKH2GX8Q7]-[73K28GRN6QJ][6HMG3Y82WCK][HCWFKJ7432D9][D9YXRGPHJK2][6ZT4FNBWQHXD2G]-[Y89G2Z3M7FQ][427P8ZNQ93X6][JE7KVDUWGQTZYC][KGUD6HFR98Y][NEP4UDBSVXQ]"
        )
        with open("keysAvast.txt", "a") as f:
            if len(mrx) == 0:
                exit("An error occured!")
            f.writelines(mrx + "\n")
            f.close()
            umm += 1
            if umm >= limit:
                print(
                    f"\n {Fore.LIGHTRED_EX}{current_time}{Fore.YELLOW} > "
                    + Colorate.Diagonal(
                        Colors.rainbow,
                        "Key Oluşturma Tamamlandı, Keyler Kaydedildi.",
                        4,
                    )
                )
                if path.exists("keysAvast.txt"):
                    system("start keysAvast.txt")
                break
