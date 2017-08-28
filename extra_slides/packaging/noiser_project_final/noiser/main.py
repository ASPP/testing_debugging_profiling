import os.path

import matplotlib.pyplot as plt
from scipy.ndimage import imread
from pkg_resources import resource_filename

from noiser.noise import white_noise
from noiser.utils import copy_image


def main():
    path = resource_filename('noiser', os.path.join('images', 'baboon_kandinsky.png'))
    print(path)
    img = imread(path)
    noisy = copy_image(white_noise(img, 20))
    plt.imshow(noisy)
    plt.draw()
    plt.show()


if __name__ == '__main__':
    main()
