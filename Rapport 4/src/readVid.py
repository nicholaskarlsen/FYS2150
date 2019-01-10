import numpy as np
import matplotlib.pyplot as plt


def rgb2gray(img):
    '''
    input
        img: size=(N, M) numpy array where each element is a length=3 numpy array
            containing RGB data.
    return  
        size=(N, M) numpy array where each element is in (0, 255). A grayscale version of the input.
    '''
    return np.dot(img[..., :3], [0.299, 0.587, 0.114]).astype(int)


def gray2binary(gray, limBW=128):
    """
    Converts grayscale image to binary grayscale of 0 OR 255
    image must be array of shape=(N, M)
    gray: (N, M) array
    limBW:
    input
        gray: size=(N, N) numpy array, grayscale image.
        limBW: minimum threshold for pixel to be black (0-255)
    return
        bw: size=(N, N) numpy array, binary image
    """
    bw = np.asarray(gray).copy()
    bw[bw < limBW] = 0      # Black
    bw[bw >= limBW] = 255   # White
    return bw

def genFilter(img):
    return

def main():
    img = plt.imread("../scripts/figs/ballcontrast.png")

    img = rgb2gray(img)
    #img = gray2binary(img)
    plt.imshow(img)
    plt.show()
    return


if __name__ == "__main__":
    main()
    