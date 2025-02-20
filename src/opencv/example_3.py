import cv2

"""
Load an image, and apply a negative filter to it (it inverts all the colors of the image, sets all black pixels to white and vice versa).
"""

if __name__ == '__main__':
    image_model = cv2.imread("./resources/pics/model_1.png")

    # Apply a negative filter to the image
    negative_image = cv2.bitwise_not(image_model)

    cv2.imshow("Original Image", image_model)
    cv2.imshow("Negative Image", negative_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()