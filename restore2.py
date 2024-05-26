import sys
import cv2 as cv
import numpy as np

def solution(img):

    dst = cv.medianBlur(img,7) #Median Filter
    
    img2 = cv.subtract(dst, img) #Subtract Operation

    img3 = cv.add(img2, dst) #Add Operation

    kernel1 = np.ones((3,3),np.float32)/9 #Mean kernel
    dst1 = cv.filter2D(img3, -1, kernel1) #Mean Filter

    return dst1

def processCommandLine():
    argc = len(sys.argv)

    if argc < 2:
        print('\n** Error: need two image files as input output\n')
        print('Syntax (Bash and PowerShell): ./restore1.py image1 image2')
        print('Syntax (Command Prompt): restore1.py image1 image2')
        print('\n  The two images are the Noised Image and the desired output Image accordingly.')
        print('\nExample:  ./restore1.py noise_img.jpg  img_solution.jpg')
        sys.exit(1)
        return

    _, file1, file2 = sys.argv
    return file1, file2

def display(image1, image2):  
    height, width, channel = image1.shape

    border = np.ones((height, 15, channel), np.uint8)*255
    caption = np.ones((40, 2*width+15,channel), np.uint8)*255
    caption = cv.putText(caption, f'Noise | Restored', (10, 20), cv.FONT_HERSHEY_SIMPLEX,
                         0.7, (0, 0, 0), 2, cv.LINE_AA)

    image = np.concatenate((image1, border, image2), axis=1)
    image = np.concatenate((image, caption), axis=0,)

    cv.imshow('Restored Noise image', image) 

def main():
    images = [None, None]
    files = [None, None]

    files[0], files[1] = processCommandLine()

    images[0] = cv.imread(files[0])
    #images[0] = cv.cvtColor(images[0], cv.COLOR_BGR2GRAY)

    images[1] = solution(images[0])

    cv.imwrite(files[1],images[1])

    display(images[0],images[1])

    print(f'Image restored in Restored folder.')

    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    main()