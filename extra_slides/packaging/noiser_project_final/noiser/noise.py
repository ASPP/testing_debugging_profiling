import numpy as np


def white_noise(image, std):
    noise = np.random.normal(scale=std, size=image.shape).astype(image.dtype)
    noisy = image + noise
    return noisy
