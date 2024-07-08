import cv2
def correct_pixelation(image_path, output_path, resize_factor=2):
    """
    Correct pixelation in an image by resizing.
    
    Args:
    - image_path (str): Path to the input pixelated image.
    - output_path (str): Path to save the corrected image.
    - resize_factor (float): Factor by which to resize the image (default: 2).
    """
    # Load the image
    image = cv2.imread(image_path)
    
    # Resize the image to increase dimensions
    width = int(image.shape[1] * resize_factor)
    height = int(image.shape[0] * resize_factor)
    resized_image = cv2.resize(image, (width, height), interpolation=cv2.INTER_LINEAR)
    
    # Save the corrected image
    cv2.imwrite(output_path, resized_image)

# Example usage:
input_image_path = 'pixelated_image.png'
output_image_path = 'smoothed_image.png'
correct_pixelation(input_image_path, output_image_path)
print(f"Pixelated image '{input_image_path}' corrected and saved as '{output_image_path}'.")
