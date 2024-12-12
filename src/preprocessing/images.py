import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


def get_image(images_df, row):
    file_name = get_file_name(images_df, row)
    image = cv.imread(file_name)
    return image


def get_file_name(images_df, row):
    file_name = images_df["file_name"][row]
    return file_name


def show_image(images_df, row):
    file_name = get_file_name(images_df, row)
    image = get_image(images_df, row)
    show_image_(image, title=file_name)


def show_image_(image, title=None, cmap=None):
    plt.imshow(image, cmap)
    plt.title(title)
    plt.show()


def crop_image(images_df, row):
    image = get_image(images_df, row)
    cropped_image = crop_image_(image)
    return cropped_image


def crop_image_(image: np.ndarray) -> np.ndarray:
    mask = _create_mask(image)
    masked_image = cv.bitwise_and(image, image, mask=mask)
    max_x, max_y, min_x, min_y = _get_cell_coordinates(masked_image)
    masked_cropped_image = masked_image[min_x:max_x, min_y:max_y, :]
    masked_cropped_image = cv.GaussianBlur(masked_cropped_image, ksize=(5, 5), sigmaX=0)
    return masked_cropped_image


def _get_cell_coordinates(image):
    (x, y, _) = np.where(image > 0)  # relevant image = blood cell and blood cell is not black (0)
    max_x, max_y = np.max((x, y), axis=1)
    min_x, min_y = np.min((x, y), axis=1)
    return max_x, max_y, min_x, min_y


def _create_mask(image):
    blurred_image = cv.GaussianBlur(image, ksize=(13, 13), sigmaX=0)
    blurred_image = cv.medianBlur(blurred_image, ksize=11)
    gray_blurred_image = cv.cvtColor(blurred_image, cv.COLOR_BGR2GRAY)
    thresh_type = cv.THRESH_BINARY
    mask = cv.threshold(gray_blurred_image, 25, 255, thresh_type)[1]
    return mask


def add_gaussian_noise(image, intensity=0.5):
    (x, y, channels) = image.shape
    mean = 0
    var = 0.1
    std = np.sqrt(var)
    noise = np.random.normal(loc=mean, scale=std, size=(x, y, channels)) * intensity
    noisy_image = image + noise * 255
    noisy_image = np.clip(noisy_image, 0, 255).astype(np.uint8)
    return noisy_image
