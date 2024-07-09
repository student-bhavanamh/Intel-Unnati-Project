import cv2
import numpy as np
import matplotlib.pyplot as plt

def block_variance(image, block_size=8):
    h, w = image.shape
    variances = []
    for y in range(0, h, block_size):
        for x in range(0, w, block_size):
            block = image[y:y+block_size, x:x+block_size]
            variances.append(np.var(block))
    return np.mean(variances), np.var(variances)

def detect_pixelation(image_path, block_size=8, variance_threshold=0.01):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    mean_var, block_var = block_variance(image, block_size)
    print(f"Mean Variance: {mean_var}, Block Variance: {block_var}")
    return block_var < variance_threshold

def frequency_analysis(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    dft = cv2.dft(np.float32(image), flags=cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)
    magnitude_spectrum = 20 * np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))
    
    # Analyze the magnitude spectrum to detect pixelation patterns
    mean_freq = np.mean(magnitude_spectrum)
    variance_freq = np.var(magnitude_spectrum)
    print(f"Mean Frequency Magnitude: {mean_freq}, Variance Frequency Magnitude: {variance_freq}")
    
    return variance_freq

def detect_pixelation_combined(image_path, block_size=8, block_variance_threshold=0.01, frequency_variance_threshold=100):
    # Block-based analysis
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    mean_var, block_var = block_variance(image, block_size)
    print(f"Mean Variance: {mean_var}, Block Variance: {block_var}")
    
    # Frequency domain analysis
    frequency_variance = frequency_analysis(image_path)
    print("Frequency Domain Variance:", frequency_variance)
    
    is_pixelated = block_var < block_variance_threshold and frequency_variance < frequency_variance_threshold
    return is_pixelated

# Example usage
image_path = 'assets/Original/gorilla.jpeg'  # Change to your image path
is_pixelated = detect_pixelation_combined(image_path)
print("Is the image pixelated?", is_pixelated)
