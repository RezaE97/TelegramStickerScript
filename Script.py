from PIL import Image, ImageDraw
import os

currentPath = os.path.dirname(os.path.realpath(__file__))
sourcePath = os.path.join(currentPath, "1")
destinationPath = os.path.join(currentPath, "2")

for inputFileName in os.listdir(sourcePath):
    if inputFileName.endswith(".png"):
        inputFile=Image.open(os.path.join(sourcePath, inputFileName))
        width, height = inputFile.size
        editedImage = Image.new('RGBA', (512, height), (0, 0, 0, 0))
        editedImage.paste(inputFile, (256 - int(width/2.0), 0))
        editedPath = os.path.join(destinationPath, "edited_"+inputFileName)
        editedImage.save(editedPath,'PNG')