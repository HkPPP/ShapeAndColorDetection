import cv2
import imutils

 
# Description: looking for contours of a thresholded image
# Note: contours of objects can only be detected if the background is of a darker color
def find_contour(thresholded_image):
    # Resize for more accurate detection
    resized = imutils.resize(thresholded_image, width=500)
    ratio = thresholded_image.shape[0] / float(resized.shape[0])

    # Find contours
    cnts = cv2.findContours(resized.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    cnts = cnts * ratio
    return cnts


# Description: Convert an image to a black and white and clearer image 
def black_and_white(image, color_space = "BGR"):
        # The idea is: gray scale -> blur -> threshold

        # The "HSV" color space already has gray scale on the second channel
        if color_space == "HSV":
            h, s, v = cv2.split(resized)
            gray = s
        # The "BGR" color space has to be converted to gray scale
        elif color_space == "BGR":
            gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

        # Blur image to remove noise
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)

        # Threshold image to blacken or whiten pixel
        thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]

        cnts = find_contour(thresh)
        number_cnts = len(cnts)
        if number_cnts == 1:
            height_resized = image.shape[0]
            width_resized = image.shape[1]

            height_cnts = cnts[0][2][0][1]
            width_cnts = cnts[0][2][0][0]

            h_ratio = height_resized / float(height_cnts)
            w_ratio = width_resized / float(width_cnts)

            if 0.95 <= h_ratio and w_ratio <= 1.05:
                #print("Inverted thresh.")
                thresh = cv2.bitwise_not(resized)


        return thresh










