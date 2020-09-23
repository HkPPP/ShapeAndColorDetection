import cv2
import imutils
from shape_and_color_detection.Detection.detection_tools import black_and_white, find_contour
from shape_and_color_detection.Classification.classify_shapes_and_colors import Iden_Shape, draw_and_name
import argparse

'''
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="path to the input image")
args = vars(ap.parse_args())

# load the image and resize it to a smaller factor so that
# the shapes can be approximated better
ima = cv2.imread(args["image"])
'''
ima = cv2.imread("shapes_and_colors.png")
ima = imutils.resize(ima, width=700)

processed = black_and_white(ima)
cnts = find_contour(processed)
shape = Iden_Shape()
draw_and_name(cnts, ima, shape)
cv2.imshow("image", ima)
