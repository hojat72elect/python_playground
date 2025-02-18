import cv2

if __name__ == '__main__':
    image_model = cv2.imread("./resources/pics/model_1.png")

    # Apply a negative filter to the image
    negative_image = cv2.bitwise_not(image_model)

    cv2.imshow("Original Image", image_model)
    cv2.imshow("Negative Image", negative_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()