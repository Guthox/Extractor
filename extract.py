from os.path import exists
from os import makedirs

pngStart = b"\x89\x50\x4E\x47\x0D\x0A\x1A\x0A"
pngEnd = b"\x49\x45\x4E\x44\xAE\x42\x60\x82"

path = "IMG.png"
tempFolder = "Files"
try:
    if not exists(f"./{tempFolder}"):
        makedirs(f"./{tempFolder}")
except:
    print("Can't create a new folder. Check permissions.")
    exit(-2)

file = open(path, "rb")
data = file.read()
file.close()

posStart = 0
posEnd = 0
counter = 1

while (True):
    posStart = data.find(pngStart, posStart)
    posEnd = data.find(pngEnd, posEnd)

    if (posStart == -1 or posEnd == -1):
        break

    png = data[posStart:posEnd+len(pngEnd)]

    try:
        with open(f"./{tempFolder}/PNG{counter}.png", "wb") as f:
            f.write(png)
        counter += 1
    except:
        print("Can't create a new file. Check permissions.")
        exit(-1)

    posEnd +=1
    posStart +=1

print(f"{counter-1} files created.")