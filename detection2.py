import cv2
import numpy as np

def detect_pixelation(image_path, block_size=4, threshold=0.3):
    # Read the image
    image = cv2.imread(image_path)
    
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Calculate gradients
    grad_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    grad_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    grad_mag = cv2.magnitude(grad_x, grad_y)
    
    # Normalize the gradient magnitude
    grad_mag = cv2.normalize(grad_mag, None, 0, 1, cv2.NORM_MINMAX)
    
    # Analyze blocks
    h, w = grad_mag.shape
    blocks = []
    for y in range(0, h, block_size):
        for x in range(0, w, block_size):
            block = grad_mag[y:y+block_size, x:x+block_size]
            mean_grad = np.mean(block)
            blocks.append(mean_grad)
    
    # Detect pixelation
    block_variance = np.var(blocks)
    print(block_variance)
    is_pixelated = block_variance < threshold
    
    return is_pixelated

# Example usage
image_path = 'assets/Pixelated/monalisa_after.png'
is_pixelated = detect_pixelation(image_path)
print("Is the image pixelated?", is_pixelated)
