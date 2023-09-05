import os.path

from imageCompress import LZWCoding
import sys


path = "text.txt"  # file to be compressed
dataType = "text"
sizeOfOriginal = os.path.getsize(path)

l = LZWCoding(path, 12, dataType) # Use smaller values for small files, use bigger values for large files. Do not use values smaller than 11.
binFilePath= l.write_compressed_file()
print("output path: ", binFilePath)
decom_path = l.decompress_file(binFilePath)
print("Decompressed file path: " + decom_path)

print()
print("Original size: ",sizeOfOriginal)
sizeOfCompressed = os.path.getsize(binFilePath)
print("Compressed size (.bin file): ", sizeOfCompressed)
print("Decompressed size: ", os.path.getsize(decom_path),"\n")

compressionRatio = (sizeOfCompressed/sizeOfOriginal)
print(compressionRatio)

ratioInPercentage = int(compressionRatio * 100)
print(str(ratioInPercentage)+"%     (smaller percentage means better compression)")

