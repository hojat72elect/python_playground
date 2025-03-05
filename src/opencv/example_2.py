import sys

import cv2

"""
Load an image, show it to the user, and then save it to the disk.
"""

if __name__ == '__main__':
    image1 = cv2.imread("resources/pics/model_1.png")

    if image1 is None:
        sys.exit("Could not read the image.")

    cv2.imshow("female model", image1)
    key_stroke = cv2.waitKey(0)

    # how to save our cv2 image.
    if key_stroke == ord("s"):
        cv2.imwrite("./resources/pics/saved_pic.png", image1)
