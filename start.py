from subprocess import run

# At the first launch, dependencies are loaded, and only after that the game starts.
# On subsequent launches, the game starts immediately
def start_game():
    with open("start.bat", 'w') as bat:
        with open("moduls.txt", 'r') as moduls:
            for command in moduls:
                run(command.split())
            bat.write("python game/main.py")
    with open("start.bat", 'r') as run_game:
        for command in run_game:
            run(command.split())


start_game()
