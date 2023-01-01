with open("start.bat", 'w') as bat:
    with open("moduls.txt", 'r') as moduls:
        bat.write(f"python -m pip install {moduls.read()}")