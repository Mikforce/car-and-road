with open("start.bat", 'w') as bat:
    with open("moduls.txt", 'r') as moduls:
        bat.write(f"{moduls.read()}\npause")

def start_game():
    with open("start.bat", 'w') as bat:
        with open("moduls.txt", 'r') as moduls:
            bat.write(f"python game/main.py")