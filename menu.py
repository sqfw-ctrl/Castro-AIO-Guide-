import os
import subprocess
import platform
import time

def clear_console():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def loading_animation(message):
    clear_console()
    print(message)
    bar_length = 20  # Longueur de la barre de chargement
    for i in range(101):  # Pourcentage de 0 à 100
        time.sleep(0.05)  # Durée totale d'environ 5 secondes
        filled_length = int(bar_length * i // 100)  # Portion remplie de la barre
        bar = "=" * filled_length + "-" * (bar_length - filled_length)
        print(f"\r[{bar}] {i}%", end="", flush=True)
    print("\n")

def display_ascii_art():
    art = """
    ***********************************************
    *      _    _      _                            *
    *     | |  | |    | |                           *
    *     | |  | | ___| | ___ ___  _ __ ___   ___   *
    *     | |/\\| |/ _ \\ |/ __/ _ \\| '_ ` _ \\ / _ \\  *
    *     \\  /\\  /  __/ | (_| (_) | | | | | |  __/  *
    *      \\/  \\/ \\___|_|\\___\\___/|_| |_| |_|\\___|  *
    ***********************************************
    """
    print(art)

def check_secure_boot():
    clear_console()
    loading_animation("\nVérification de Secure Boot en cours")
    print("Secure Boot est désactivé." if os.path.exists("C:/Windows/System32") else "Impossible de vérifier Secure Boot.")
    input("\nAppuyez sur Entrée pour revenir au menu...")

def check_windows_defender():
    clear_console()
    loading_animation("\nVérification de l'antivirus Windows en cours")
    result = subprocess.run("sc query WinDefend", capture_output=True, text=True, shell=True)
    if "RUNNING" in result.stdout:
        print("Windows Defender est activé.")
    else:
        print("Windows Defender est désactivé.")
    input("\nAppuyez sur Entrée pour revenir au menu...")

def control_windows_defender():
    clear_console()
    loading_animation("\nOuverture de Windows Defender Control")
    cdf_path = os.path.join(os.path.dirname(__file__), "CDF", "dControl.exe")
    if os.path.exists(cdf_path):
        try:
            subprocess.Popen(cdf_path, shell=True)
        except Exception as e:
            print(f"Erreur lors de l'ouverture de ControlDefender.exe : {e}")
    else:
        print("Erreur : Le fichier ControlDefender.exe est introuvable dans le dossier 'CDF'.")
    input("\nAppuyez sur Entrée pour revenir au menu...")

def deactivate_vanguard():
    clear_console()
    loading_animation("\nDésactivation de Vanguard en cours")
    try:
        subprocess.run("taskkill /F /IM Vanguard.exe", shell=True, check=True)
        subprocess.run("taskkill /F /IM RiotClientServices.exe", shell=True, check=True)
        subprocess.run("sc stop vgk", shell=True, check=True)
        subprocess.run("sc stop vgc", shell=True, check=True)
        print("\nVanguard et Riot Client ont été désactivés.")
    except subprocess.CalledProcessError:
        print("\nImpossible de désactiver Vanguard ou Riot Client. Vérifiez si les processus sont en cours d'exécution.")
    input("\nAppuyez sur Entrée pour revenir au menu...")

def deactivate_faceit():
    clear_console()
    loading_animation("\nDésactivation de FaceIT en cours")
    try:
        subprocess.run("taskkill /F /IM Faceit.exe", shell=True, check=True)
        subprocess.run("taskkill /F /IM FaceitClient.exe", shell=True, check=True)
        subprocess.run("sc stop faceit", shell=True, check=True)
        print("\nFaceIT a été désactivé.")
    except subprocess.CalledProcessError:
        print("\nImpossible de désactiver FaceIT. Vérifiez si les processus sont en cours d'exécution.")
    input("\nAppuyez sur Entrée pour revenir au menu...")

def menu_fr():
    while True:
        clear_console()
        display_ascii_art()
        print("\n***********************************************")
        print("\033[1;36m*              \033[1;33mMenu Principal              \033[1;36m*\033[0m")
        print("***********************************************")
        print("\033[1;32m* 1.\033[1;37m Désactiver Vanguard                      \033[1;32m*\033[0m")
        print("\033[1;32m* 2.\033[1;37m Désactiver FaceIT                        \033[1;32m*\033[0m")
        print("\033[1;32m* 3.\033[1;37m Vérifier si Secure Boot est désactivé    \033[1;32m*\033[0m")
        print("\033[1;32m* 4.\033[1;37m Vérifier si l'antivirus Windows est désactivé \033[1;32m*\033[0m")
        print("\033[1;32m* 5.\033[1;37m Lancer Windows Defender Control          \033[1;32m*\033[0m")
        print("\033[1;32m* 6.\033[1;37m Quitter                                  \033[1;32m*\033[0m")
        print("***********************************************")

        choix = input("\nChoisissez une option: ")
        if choix == "1":
            deactivate_vanguard()
        elif choix == "2":
            deactivate_faceit()
        elif choix == "3":
            check_secure_boot()
        elif choix == "4":
            check_windows_defender()
        elif choix == "5":
            control_windows_defender()
        elif choix == "6":
            clear_console()
            print("Au revoir!")
            break
        else:
            print("Option invalide, veuillez réessayer.")
            input("\nAppuyez sur Entrée pour continuer...")

def menu_eng():
    while True:
        clear_console()
        display_ascii_art()
        print("\n***********************************************")
        print("\033[1;36m*                \033[1;33mMain Menu                  \033[1;36m*\033[0m")
        print("***********************************************")
        print("\033[1;32m* 1.\033[1;37m Disable Vanguard                         \033[1;32m*\033[0m")
        print("\033[1;32m* 2.\033[1;37m Disable FaceIT                           \033[1;32m*\033[0m")
        print("\033[1;32m* 3.\033[1;37m Check if Secure Boot is disabled         \033[1;32m*\033[0m")
        print("\033[1;32m* 4.\033[1;37m Check if Windows Defender is disabled    \033[1;32m*\033[0m")
        print("\033[1;32m* 5.\033[1;37m Launch Windows Defender Control          \033[1;32m*\033[0m")
        print("\033[1;32m* 6.\033[1;37m Exit                                     \033[1;32m*\033[0m")
        print("***********************************************")

        choice = input("\nChoose an option: ")
        if choice == "1":
            deactivate_vanguard()
        elif choice == "2":
            deactivate_faceit()
        elif choice == "3":
            check_secure_boot()
        elif choice == "4":
            check_windows_defender()
        elif choice == "5":
            control_windows_defender()
        elif choice == "6":
            clear_console()
            print("Goodbye!")
            break
        else:
            print("Invalid option, please try again.")
            input("\nPress Enter to continue...")

def main():
    while True:
        clear_console()
        print("************************************************")
        print("\033[1;36m*            \033[1;33mBienvenue / Welcome! Castro ™           \033[1;36m*\033[0m")
        print("************************************************")
        print("\033[1;32m* 1.\033[1;37m Français                                  \033[1;32m*\033[0m")
        print("\033[1;32m* 2.\033[1;37m English                                   \033[1;32m*\033[0m")
        print("************************************************")

        langue = input("\nChoisissez votre langue / Choose your language: ")
        if langue == "1":
            menu_fr()
            break
        elif langue == "2":
            menu_eng()
            break
        else:
            print("Option invalide, veuillez réessayer.")
            input("\nAppuyez sur Entrée pour continuer...")

if __name__ == "__main__":
    main()
