def read_file():
    with open(r"C:\backup\Storage_qualification\ust\anamika-kumari123\passwords.txt","r") as file1:
        # print(file1.read().split("\n"))
        out = file1.read().split("\n")
        return out
