import os.path
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog
from imageCompress import LZWCoding


def openFile():
    global originalFilePath
    originalFilePath = filedialog.askopenfilename(initialdir=os.path.curdir, title="select a file", filetypes=(
    ("bmp files", "*.bmp"),("text files", "*.txt"), ("all files", "*.*")))  # now, selected file's name is in filename:str


def compressColorImageFile():
    global binFile
    l = LZWCoding(originalFilePath, codelength, "colorimage")
    binFile = l.write_compressed_file()
    decompressedPath = l.decompress_file(binFile)
    sizeOfOriginal = os.path.getsize(originalFilePath)
    print()
    print("Original size: ", sizeOfOriginal)
    sizeOfCompressed = os.path.getsize(binFile)
    print("Compressed size: ", sizeOfCompressed)
    print("Decompressed size: ", os.path.getsize(decompressedPath), "\n")

    compressionRatio = (sizeOfCompressed / sizeOfOriginal)

    ratioInPercentage = int(compressionRatio * 100)
    print("Size of the file is reduced by " + str(100-ratioInPercentage) + " %")


def compressTextFile():
    l = LZWCoding(originalFilePath, codelength, "text")
    binFile = l.write_compressed_file()
    decompressedPath = l.decompress_file(binFile)
    sizeOfOriginal = os.path.getsize(originalFilePath)
    print()
    print("Original size: ", sizeOfOriginal)
    sizeOfCompressed = os.path.getsize(binFile)
    print("Compressed size: ", sizeOfCompressed)
    print("Decompressed size: ", os.path.getsize(decompressedPath), "\n")

    compressionRatio = (sizeOfCompressed / sizeOfOriginal)

    ratioInPercentage = int(compressionRatio * 100)
    print("Size of the file is reduced by " + str(100-ratioInPercentage) + " %")

def compressGrayLevelImageFile():
    l = LZWCoding(originalFilePath, codelength, "graylevelimage")
    binFile = l.write_compressed_file()
    decompressedPath = l.decompress_file(binFile)
    sizeOfOriginal = os.path.getsize(originalFilePath)
    print()
    print("Original size: ", sizeOfOriginal)
    sizeOfCompressed = os.path.getsize(binFile)
    print("Compressed size: ", sizeOfCompressed)
    print("Decompressed size: ", os.path.getsize(decompressedPath), "\n")

    compressionRatio = (sizeOfCompressed / sizeOfOriginal)

    ratioInPercentage = int(compressionRatio * 100)
    print("Size of the file is reduced by " + str(100 - ratioInPercentage) + " %")


def codelengthSelectFunction():
    global codelength
    codelength = int(textInput.get("1.0", "end-1c"))
    print("codelength: ", codelength)


def displayRGBComponent(index):
    myImage = Image.open(originalFilePath)
    myImage = myImage.convert("RGB")
    r,g,b = myImage.split()

    if index == 0:  # red
        r.show()
    elif index == 1:  # green
        g.show()
    elif index == 2:  # blue
        b.show()
    else:
        print("Something went wrong...")

root = tk.Tk()                                                 #Starting here
root.title("Compression")
root.geometry("850x500")

compressFrame = tk.Frame(root,width=30,height=50)
compressFrame.place(x=270, y=200)

selectFrame = tk.Frame(root, width=30, height=30)
selectFrame.place(x=20, y=200)

displayFrame = tk.Frame(root,width=30,height=50)
displayFrame.place(x=600, y=200)

selectButton = tk.Button(selectFrame, text="Select a file", command=openFile)
selectButton.pack(pady=10)

codelengthButton = tk.Button(selectFrame, text="Select codelength", command=codelengthSelectFunction)
codelengthButton.pack()

textInput = tk.Text(selectFrame, width=3, height=1)
textInput.pack(pady=5)

button1 = tk.Button(compressFrame, text="Compress text file", command=compressTextFile)
button1.pack(side="top")

button2 = tk.Button(compressFrame, text="Compress color image file", command=compressColorImageFile)
button2.pack(side="top", pady=10)

button3 = tk.Button(compressFrame, text="Compress gray level image file", command=compressGrayLevelImageFile)
button3.pack(side="top")




button4 = tk.Button(displayFrame, text="Display red component", command=lambda:displayRGBComponent(0))
button4.pack(side="top")

button5 = tk.Button(displayFrame, text="Display green component", command=lambda:displayRGBComponent(1))
button5.pack(side="top", pady=10)

button6 = tk.Button(displayFrame, text="Display blue component", command=lambda:displayRGBComponent(2))
button6.pack(side="top")

root.mainloop()

