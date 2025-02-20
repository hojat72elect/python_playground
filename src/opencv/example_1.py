import cv2

"""
Load an image and show it to the user.
"""

if __name__ == '__main__':

    image = cv2.imread("./resources/pics/model_1.png")
    cv2.imshow("female model with black skin and white scarf", image)
    key_stroke = cv2.waitKey(0) # wait for a key stroke in the window