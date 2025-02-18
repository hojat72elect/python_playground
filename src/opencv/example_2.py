import sys

import cv2

if __name__ == '__main__':
    image_model = cv2.imread("./resources/pics/model_1.png")

    if image_model is None:
        sys.exit("Could not read the image.")

    cv2.imshow("female model", image_model)
    key_stroke = cv2.waitKey(0)

    # how to save our cv2 image.
    if key_stroke == ord("s"):
        cv2.imwrite("./resources/pics/saved_pic.png", image_model)
