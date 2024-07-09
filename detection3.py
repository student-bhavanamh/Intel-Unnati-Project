import cv2
import numpy as np
import matplotlib.pyplot as plt

def do_canny(image):
    gray = cv2.imread(image, 0)
    canny = cv2.Canny(gray, 50, 150, apertureSize=3)
    minLineLength = 100
    maxLineGap = 10
    lines = cv2.HoughLinesP(canny, 1, np.pi/180, 100, minLineLength, maxLineGap)
    return gray, canny, lines

def plot_images(gray, canny):
    plt.subplot(121), plt.imshow(gray, cmap='gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(canny, cmap='gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
    plt.show()

def do_laplacian(image):
    gray = cv2.imread(image, 0)
    variance = cv2.Laplacian(gray, cv2.CV_64F)
    var = np.var(variance)
    return var

def detect_pixelation(image_path, laplacian_threshold=100):
    gray, canny, lines = do_canny(image_path)
    plot_images(gray, canny)
    laplacian_variance = do_laplacian(image_path)
    
    print(f"Laplacian Variance: {laplacian_variance}")
    
    is_pixelated = laplacian_variance < laplacian_threshold
    return is_pixelated

# Example usage
image_path = 'assets/Pixelated/jar.jpg'  # Change to your image path
is_pixelated = detect_pixelation(image_path)
print("Is the image pixelated?", is_pixelated)
