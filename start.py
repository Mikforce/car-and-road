with open("start.bat", 'r') as bat:
    with open("moduls.txt", 'r') as moduls:
        bat.write(f"python -m pip install {moduls.read()}")