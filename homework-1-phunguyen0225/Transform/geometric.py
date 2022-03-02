from .interpolation import interpolation
import numpy as np
import math

class Geometric:
    def __init__(self):
        pass

    def forward_rotate(self, image, theta):
        """Computes the forward rotated image by and angle theta
                image: input image
                theta: angle to rotate the image by (in radians)
                return the rotated image"""
                
        #shape of iamge
        index1 = image.shape[0]
        index2 = image.shape[1]

        #corners coordinate of the orignal image
        origin = [0, 0]
        top_right = [0, index2 - 1]
        bottom_left = [index1 - 1, 0]
        bottom_right = [index1 - 1, index2 - 1]

        #find the new size of the image
        #apply transformation, rotate corner
        rotate_top_x = top_right[0] * math.cos(theta) - top_right[1] * math.sin(theta)
        rotate_top_y = top_right[0] * math.sin(theta) + top_right[1] * math.cos(theta)
       
        #top rotated corner
        rotate_top = [rotate_top_x, rotate_top_y]
        #print("New top right: ", rotate_top)

        bottom_left_x = bottom_left[0] * math.cos(theta) - bottom_left[1] * math.sin(theta)
        bottom_left_y = bottom_left[0] * math.sin(theta) + bottom_left[1] * math.cos(theta)

        #bottom left rotateed corner
        rotate_bottom_left = [bottom_left_x, bottom_left_y]
        #print("New bottom left: ", rotate_bottom_left)

        bottom_right_x = bottom_right[0] * math.cos(theta) - bottom_right[1] * math.sin(theta)
        bottom_right_y = bottom_right[0] * math.sin(theta) + bottom_right[1] * math.cos(theta)

        #bottom right rotated corner
        rotate_bottom_right = [bottom_right_x, bottom_right_y]
        #print("New bottom right: ", rotate_bottom_right)
        

        #new coordinates, min and max
        min_x = min(origin[0], rotate_top[0], rotate_bottom_left[0], rotate_bottom_right[0])
        min_y = min(origin[1], rotate_top[1], rotate_bottom_left[1], rotate_bottom_right[1])

        max_x = max(origin[0], rotate_top[0], rotate_bottom_left[0], rotate_bottom_right[0])
        max_y = max(origin[1], rotate_top[1], rotate_bottom_left[1], rotate_bottom_right[1])

        #size of the new rotated image
        #rows = max_x - min_x
        rows = int(max_x - min_x)
        #cols = max_y - min_y
        cols = int(max_y - min_y)
        rotate = np.zeros((rows, cols), np. uint8)
        #print("rows: ", rows)
        #print("col: ", cols)
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                #1. find location of (i', j')
                iprime = int((i * math.cos(theta) - j * math.sin(theta)))
                jprime = int((i * math.sin(theta) + j * math.cos(theta)))

                #2. (i'N = i' - min_x, j'N = j' - min_y)
                inprime = int(iprime - min_x)
                jnprime = int(jprime - min_y)

                #condition
                if inprime >= rows or inprime < 0:
                    continue
                elif jnprime >= cols or jnprime < 0:
                    continue

                #rotate
                rotate[inprime, jnprime] = image[i, j]

        
        return rotate

    def reverse_rotation(self, rotated_image, theta, origin, original_shape):
        """Computes the reverse rotated image by and angle theta
                rotated_image: the rotated image from previous step
                theta: angle to rotate the image by (in radians)
                Origin: origin of the original image with respect to the rotated image
                Original shape: Shape of the orginal image
                return the original image"""
        #1. Create image of original shape
        image = np.zeros((original_shape[0], original_shape[1]), np.uint8)
        
        #2. For(i'n, j'n) in rotated image
        for inprime in range(rotated_image.shape[0]):
            for jnprime in range(rotated_image.shape[1]):

                #1. Calculate location with respect to O
                #   i' = i'n - Oi,  j' = j'n - Oj
                iprime = int(inprime - origin[0])
                jprime = int(jnprime - origin[1])

                #2. Computer inverse rotation on (i', j') to get (i,j)
                i = int((iprime * math.cos(theta) + (jprime * math.sin(theta))))
                j = int((iprime * (-math.sin(theta)) + (jprime * math.cos(theta))))

                #condition
                #if ((i >= 0 and i <= original_shape[0] - 1) and (j >= 0 and j <= original_shape[1] - 1)):
                #check out-of-bound
                if i >= original_shape[0] or i < 0:
                    continue
                elif j >= original_shape[1] or j < 0:
                    continue
                #3. image(i, j) = rotate(i'n, j'n)
                image[i, j] = rotated_image[inprime, jnprime]
       
        return image

    def rotate(self, image, theta, interpolation_type):
        """Computes the reverse rotated image by and angle theta
                image: the input image
                theta: angle to rotate the image by (in radians)
                interpolation_type: type of interpolation to use (nearest_neighbor, bilinear)
                return the original image"""
        
        #shape of image
        index1 = image.shape[0]
        index2 = image.shape[1]

        #corners coordinate of the orignal image
        origin = [0, 0]
        top_right = [0, index2 - 1]
        bottom_left = [index1 - 1, 0]
        bottom_right = [index1 - 1, index2 - 1]

        #find the new size of the image
        #apply transformation, rotate corner
        rotate_top_x = top_right[0] * math.cos(theta) - top_right[1] * math.sin(theta)
        rotate_top_y = top_right[0] * math.sin(theta) + top_right[1] * math.cos(theta)
       
        #top rotated corner
        rotate_top = [rotate_top_x, rotate_top_y]
        #print("New top right: ", rotate_top)

        bottom_left_x = bottom_left[0] * math.cos(theta) - bottom_left[1] * math.sin(theta)
        bottom_left_y = bottom_left[0] * math.sin(theta) + bottom_left[1] * math.cos(theta)

        #bottom left rotateed corner
        rotate_bottom_left = [bottom_left_x, bottom_left_y]
        #print("New bottom left: ", rotate_bottom_left)

        bottom_right_x = bottom_right[0] * math.cos(theta) - bottom_right[1] * math.sin(theta)
        bottom_right_y = bottom_right[0] * math.sin(theta) + bottom_right[1] * math.cos(theta)

        #bottom right rotated corner
        rotate_bottom_right = [bottom_right_x, bottom_right_y]
        #print("New bottom right: ", rotate_bottom_right)
        

        #new coordinates, min and max
        min_x = min(origin[0], rotate_top[0], rotate_bottom_left[0], rotate_bottom_right[0])
        min_y = min(origin[1], rotate_top[1], rotate_bottom_left[1], rotate_bottom_right[1])

        max_x = max(origin[0], rotate_top[0], rotate_bottom_left[0], rotate_bottom_right[0])
        max_y = max(origin[1], rotate_top[1], rotate_bottom_left[1], rotate_bottom_right[1])

        #size of the new rotated image
        #rows = max_x - min_x
        rows = int(max_x - min_x)
        #cols = max_y - min_y
        cols = int(max_y - min_y)
        #create rotate image with size (rows, cols)
        rotate = np.zeros((rows, cols), np. uint8)
        #Location of Origin with respect to N (O = -min_x, -min_y)
        origin = [-min_x, -min_y]

        #For (i'n, j'n) in rotate image
        for inprime in range(rotate.shape[0]):
            for jnprime in range(rotate.shape[1]):
                #1. Calculate location with respect to O
                iprime = inprime - origin[0]
                jprime = jnprime - origin[1]

                #2. Compute inverse rotation on (i', j') to get (i, j)
                i = (iprime * math.cos(theta) + (jprime * math.sin(theta)))
                j = (iprime * (-math.sin(theta)) + (jprime * math.cos(theta)))

                #3. if using nearst neighbour interpolation
                    #1. if nearest_neighbor
                
                if interpolation_type == "nearest_neighbor":
                    i_nn = round(i)
                    j_nn = round(j)

                    #2. rotate(i'n, j'n) = image(i_nn, j_nn)
                    #conditon check with originals rows and cols, not the new image rows and cols
                    if i_nn >= index1 or i_nn < 0:
                        continue
                    elif j_nn >= index2 or j_nn < 0:
                        continue

                    rotate[inprime, jnprime] = image[i_nn, j_nn]

                    #2. if bilinear
                elif interpolation_type == "bilinear":
                    #1. Find four nearest neighbors to (i, j)
                    int_i = int(i)
                    int_j = int(j)
                    if int_i < 255 and int_j < 255 and int_i > 1 and int_j > 1:
                        #bottom left
                        pt1 = [int_i+1, int_j-1, image[int_i+1][int_j-1]] #point 1
                        #bottom right
                        pt2 = [int_i+1, int_j+1, image[int_i+1][int_j+1]] #point 2
                        #top left
                        pt3 = [int_i-1, int_j-1, image[int_i-1][int_j-1]] #point 3
                        #top right
                        pt4 = [int_i-1, int_j+1, image[int_i-1][int_j+1]] #point 4

                        #create object
                        obj = interpolation()

                        #call bilinear_interpolation
                        b = obj.bilinear_interpolation(pt1, pt2, pt3, pt4, [i, j])
                        #R(i'n, j'n) = b
                        rotate[inprime, jnprime] = b
        return rotate

