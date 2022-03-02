# Digital Image Processing 
Assignment #1

Due: Thu 09/30/21 11:59 PM

1. (20 pts.) Forward Rotation: Write code to perform forward rotation on an image.
    - Starter code available in directory Tranform/
    - Transform/geometric.py: Edit the function forward_rotate to implement this part.
    
2. (20 pts.) Reverse Rotation: Write code to perform reverse rotation on the input image.
    - Starter code available in directory Tranform/
    - Transform/geometric.py: Edit the function reverse_rotation to implement this part.
    
2. (35 pts.) Rotation with interpolation: Write code to rotate the input image, using nearest neighbor and bilinear interpolation.
    - Starter code available in directory Tranform/
    - Transform/geometric.py: Edit the function rotate to implement this part.
    - Transform/interpolation.py: Write code for linear and bilinear interpolation in there respective function definitions, you are welcome to write new functions and call them from these functions


  - The assignment can be run using dip_hw1_rotate.py (there is no need to edit this file)
  - Usage: ./dip_hw1_rotate.py -i image-name -t theta -m method                   
       - image-name: name of the image
       - theta: angle in radians to rotate the image (eg. 0.5)
       - method: "nearest_neightbor" or "bilinear" 
  - Please make sure your code runs when you run the above command from prompt/Terminal
  - Any output images or files must be saved to "output/" folder

----------------------
One images is provided for testing: cameraman.jpg
  
Notes: 

1. Files not to be changed: requirements.txt and Jenkinsfile 

2. the code has to run using one of the following commands

 - Usage: `./dip_hw1_rotate.py -i image-name -t theta -m method`
 
   Example: `./dip_hw1_rotate.py -i cameraman.jpg -t 0.5 -m nearest_neighbor`

 - Usage: `python dip_hw1_rotate.py -i image-name -t theta -m method`
 
   Example: `python dip_hw1_rotate.py -i cameraman.jpg -t 0.5 -m bilinear`
  
3. Any output file or image should be written to output/ folder

4. The code has to run on jenkins CI/CD
5. **Do not use** any in-built functions from opencv and numpy (E.g: np.mean). In general, you can use functions from the math (sin, cos, etc) library.
6. The only allowed functions for this part are: np.array(), np.matrix(), np.zeros(), np.ones(), cv2.imread(), cv2.namedWindow(), cv2.waitKey().


Part| Name | Pts
--------------|-------------|----------
1|Forward rotation |- 20 Pts
2|Reverse rotation |- 20 Pts
3|Rotation interpolation |- 35 Pts
-|**Total**     | - **75 Pts**

-----------------------