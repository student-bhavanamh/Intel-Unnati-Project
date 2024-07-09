import cv2

# Path to the image file
path = 'assets/Pixelated/monalisa_after.png'

# Load the image
img = cv2.imread(path)

if img is None:
    print(f"Error: Unable to read the image from '{path}'. Please check the file path.")
else:
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Calculate the Laplacian variance
    laplace_var = cv2.Laplacian(gray, cv2.CV_64F).var()
    
    print(f"Laplacian variance: {laplace_var}")
