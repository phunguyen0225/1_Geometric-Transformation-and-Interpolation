class interpolation:

    def linear_interpolation(self, pt1, pt2, z):
        """Computes the linear interpolation at location pti using pt1 and pt2 as input.
        1. Please change the function definition to add the the required arguments as needed.
        2. This function performs linear interpolation between two one dimensional points and returns the interpolated value.        
        This function will require the following values
        pt1: Location of point pt1 (z1)
        I1: Intensity at the location pt1
        pt2: Location of point pt2 (z2)
        I2: Intensity at the location pt2
        pti: Location at which to detemine the interploated value (z)
        return Ii or interploated intentity at location pti"""

        # Write your code for linear interpolation here
        Iz = (pt1[1] * (pt2[0] - z)) / (pt2[0] - pt1[0])
        Iz += (pt2[1] * (z - pt1[0])) / (pt2[0] - pt1[0])

        return Iz

    def bilinear_interpolation(self, pt1, pt2, pt3, pt4, z):
        """Computes the bilinear interpolation at location pti using pt1, pt2, pt3, and pt4 as input
        1. Please change the function definition to add the the required arguments as needed.
        2. This function performs bilinear interpolation between four two dimensional points and returns the interpolated value.        
        3. This is accomplished by performing linear interpolation three times. Reuse or call linear interpolation method above to compute this task.
        This function will require the following values
        pt1: Location of the point pt1 (x1, y1)
        I1: Intensity at location pt1
        pt2: Location of the point pt2 (x2, y2)
        I2: Intensity at location pt2
        pt3: Location of the point pt3 (x3, y3)
        I3: Intensity at location pt3
        pt4: Location of the point pt4 (x4, y4)
        I4: Intensity at location pt4
        pti: Location at which to detemine the interploated value (x, y)
        return Ii or interploated intentity at location pti"""

        # Write your code for bilinear interpolation her

        x1_pt1 = [pt1[1], pt1[2]]
        x1_pt2 = [pt2[1], pt2[2]]
        Q1 = self.linear_interpolation(x1_pt1, x1_pt2, z[1])

        x2_pt1 = [pt3[1], pt3[2]]
        x2_pt2 = [pt4[1], pt4[2]]
        Q2 = self.linear_interpolation(x2_pt1, x2_pt2, z[1])

        x3_pt1 = [pt3[0], Q2]
        x3_pt2 = [pt1[0], Q1]
        Q3 = self.linear_interpolation(x3_pt1, x3_pt2, z[0])

        return Q3
