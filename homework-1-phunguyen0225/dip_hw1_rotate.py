"""dip_hw1.py: Starter file to run howework 1"""

# Example Usage: ./dip_hw1_rotate.py -i imagename -t 1.5 -m nearest_neighbor
# Example Usage: ./dip_hw1_rotate.py -i imagename -t 1.5 -m bilinear
# Or:
# Example Usage: python dip_hw1_rotate.py -i imagename.jpg -t 1.5 -m nearest_neighbor
# Example Usage: python dip_hw1_rotate.py -i imagename.jpg -t 1.5 -m bilinear

__version__ = "1.0.0"

import math
import cv2
import sys
import numpy as np
from Transform.geometric import Geometric


def display_image(window_name, image):
    """A function to display image"""
    cv2.namedWindow(window_name)
    cv2.imshow(window_name, image)
    cv2.waitKey(0)


def transform_cord(pt, transform_matrix):
    return np.sum(transform_matrix * pt, axis=1)


def get_origin(input_shape, theta):
    transformation_matrix = np.array([[math.cos(theta), -math.sin(theta)],
                                      [math.sin(theta), math.cos(theta)]])

    corners = {"tl": np.array([0, 0]),
               "tr": np.array([0, input_shape[1]]),
               "bl": np.array([input_shape[0], 0]),
               "br": np.array([input_shape[0], input_shape[1]])}

    transformed_corners = dict()
    min_x, min_y = np.inf, np.inf
    for k in corners:

        transformed_corners[k] = transform_cord(
            corners[k], transformation_matrix)

        if transformed_corners[k][0] < min_x:
            min_x = transformed_corners[k][0]

        if transformed_corners[k][1] < min_y:
            min_y = transformed_corners[k][1]
    return -min_x, -min_y


def main():
    """ The main funtion that parses input arguments, calls the approrpiate
     interpolation method and writes the output image"""

    # Parse input arguments
    from argparse import ArgumentParser

    parser = ArgumentParser()

    parser.add_argument("-i", "--image", dest="image",
                        help="specify the name of the image", metavar="IMAGE")
    parser.add_argument("-t", "--theta", dest="theta",
                        help="specify the angle theta", metavar="THETA")
    parser.add_argument("-m", "--interpolation", dest="interpolate",
                        help="specify the interpolation method (nearest_neighbor or bilinear)", metavar="INTERPOLATION METHOD")

    args = parser.parse_args()

    # Load image
    if args.image is None:
        print("Please specify the name of image")
        print("use the -h option to see usage information")
        sys.exit(2)
    else:
        image_name = args.image.split(".")[0]
        input_image = cv2.imread(args.image, 0)

    # Check theta argument
    if args.theta is None:
        print("Rotation angle is not provided")
        print("use the -h option to see usage information")
        theta = math.pi / 8
    else:
        theta = float(args.theta)

    # Check interpolate method argument
    if args.interpolate is None:
        print("Interpolation method not specified, using default=nearest_neighbor")
        print("use the -h option to see usage information")
        interpolation = "nearest_neighbor"
    else:
        if args.interpolate not in ["nearest_neighbor", "bilinear"]:
            print("Invalid interpolation method, using default=nearest_neighbor")
            print("use the -h option to see usage information")
            interpolation = "nearest_neighbor"
        else:
            interpolation = args.interpolate

    getometric_transform = Geometric()

    # Part 1
    forward_rotated_image = getometric_transform.forward_rotate(
        input_image, theta)

    # Part 2
    origin = get_origin(input_image.shape, theta)
    reverse_rotated_image = getometric_transform.reverse_rotation(
        forward_rotated_image, theta, origin, input_image.shape)

    # Part 3
    rotated_image = getometric_transform.rotate(
        input_image, theta, interpolation)

    # Write output file
    outputDir = 'output/'

    output_image_name = outputDir + image_name + \
        '_forward_rotated_' + str(theta) + ".jpg"
    cv2.imwrite(output_image_name, forward_rotated_image)

    output_image_name = outputDir + image_name + \
        '_reverse_rotated_' + str(theta) + ".jpg"
    cv2.imwrite(output_image_name, reverse_rotated_image)

    output_image_name_1 = outputDir + image_name + \
        '_rotated_' + str(theta) + "_" + interpolation+".jpg"
    cv2.imwrite(output_image_name_1, rotated_image)


if __name__ == "__main__":
    main()
