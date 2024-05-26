# Restore-image-with-noise
Restoring image with noise using Python (image enhancement). The original image is given for references to compare with the restored images which are the result from the two programs. We need to compare the images using similarity.py in order to determine which solution is better for restoring images with noise.

Solution 1
![image](https://github.com/tengkoku/Restore-image-with-noise/assets/148973550/7c5006b2-2dbc-4acb-970c-047c91f4e190)

Application
Median Filter : Used on the noise image to reduce salt and pepper noise with 5x5 as the kernel size.
Gaussian Filter : Used on the reduced noise image with 5x5 kernel size, sigmaX andsigmaY both set to 1, and borderType to default. This is a low pass filter that smoothes the image features.
Substract : To get the high frequency component between the noise reduced image and its gaussian filtered image.
Add : To enhance the noise reduced image by adding the high frequency component to it.

Solution 2
![image](https://github.com/tengkoku/Restore-image-with-noise/assets/148973550/c6e4d068-2abf-43e9-849f-215f91e45fe8)

Application
Median Filter : Used on the noise image to reduce salt and pepper noise with 7x7 as the kernel size.
Subtract : To get the high frequency component of the noise reduced image.
Add : To get the clearer image from median filter
Mean Filter : Used on the reduced noise image to get the smoothen image with coefficient value = -1 and divides the result by a scaling factor.

![image](https://github.com/tengkoku/Restore-image-with-noise/assets/148973550/de548e82-09f2-49c8-91a7-170fa0be16fb)




