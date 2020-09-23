# Import the necessary packages
import cv2



class Iden_Shape:
    def __init__(self):
        pass

    # Description: The function identifies shapes based on the number of contours
    def iden_shapes(self, c):
        # initialize the shape name and approximate the contour
        shape = "unidentified"
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.03 * peri, True)

        # if the shape is a triangle, it will have 3 vertices
        if len(approx) == 3:
            shape = "triangle"

            # if the shape has 4 vertices, it is either a square or a rectangle
        elif len(approx) == 4:
            # compute the bounding box of the contour and use the
            # bounding box to compute the aspect ratio
            (x, y, w, h) = cv2.boundingRect(approx)
            ar = w / float(h)

            # a square will have an aspect ratio that is approximately
            # equal to one, otherwise, the shape is a rectangle
            shape = "square" if 0.95 <= ar <= 1.05 else "rectangle"

            # if the shape is a pentagon, it will have 5 vertices
        elif len(approx) == 5:
            shape = "pentagon"

            # star has 10 vertices
            # (the range below is increased for better detection)
        elif 8 < len(approx) < 12:
            shape = "star"

            # otherwise, we assume the shape is a circle
        else:
            shape = "circle"

            # return the name of the shape
        return shape


def draw_and_name(cnts, original_image, text):
    for c in cnts:
        # compute the center of the contour, then detect the name of the
        # shape using only the contour
        M = cv2.moments(c)

        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
        else:
            cX, cY = 0, 0

        # multiply the contour (x, y)-coordinates by the resize ratio,
        # then draw the contours and the name of the shape on the image
        c = c.astype("float")
        c = c.astype("int")
        cv2.drawContours(original_image, [c], -1, (0, 255, 0), 2)
        cv2.putText(original_image, text, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (0, 0, 0), 4)
        cv2.putText(original_image, text, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (255, 255, 255), 2)
    return original_image
