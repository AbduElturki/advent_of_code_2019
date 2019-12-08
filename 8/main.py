import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

def spaceImageFormatDecoder(height, width):
    layerSize = height * width
    with open('input') as f:
        encoded = f.readline().rstrip('\n')
    encodedSplit = [encoded[i:i+layerSize] for i in range(0,len(encoded),
                                                          layerSize)]
    layerFewestZeros = min(encodedSplit, key=lambda x: x.count('0'))
    return layerFewestZeros.count('1') * layerFewestZeros.count('2') 

def spaceImageFormatCombiner(height, width):
    layerSize = height * width
    with open('input') as f:
        encoded = f.readline().rstrip('\n')
    encodedSplit = [encoded[i:i+layerSize] for i in range(0,len(encoded),
                                                          layerSize)]
    currentLayer = 0
    currentLayerIdx = 0
    finalImage = []
    while len(finalImage) < layerSize:
        if encodedSplit[currentLayer][currentLayerIdx] == '2':
            currentLayer += 1
        else:
            finalImage.append(int(encodedSplit[currentLayer][currentLayerIdx]))
            currentLayer = 0
            currentLayerIdx += 1
    finalImage = list(map(lambda x: x * 255, finalImage))
    plt.imshow(np.array(finalImage).reshape(width,height), cmap=cm.gray)
    plt.show()

if __name__ == "__main__":
    print("Part 1: " + str(spaceImageFormatDecoder(25,6)))
    print("Part 2: the answer will be in the image...")
    spaceImageFormatCombiner(25,6)
