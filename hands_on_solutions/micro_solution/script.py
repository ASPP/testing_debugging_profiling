from scipy.ndimage import imread

from counting import count_objects


if __name__ == '__main__':
    img = imread('img/specimen_example.png', flatten=True) // 255
    count = count_objects(img)
    print('Number of objects:', count)
