import os
import pathlib

if os.path.join("C:/ProgramData/ProtonVPN/RenPy/"):
    path = pathlib.Path("C:/ProgramData/ProtonVPN/Updates/RenPy/")
    with open(str(path) + "test.txt", mode="w") as file:
        # file.write("EEE")
        ...
    print(os.path.join(path / "test.txt"))
