import cv2

def detect_pixelation(image_path, threshold=60):
    # Load image
    img = cv2.imread(image_path)

    # Display image
    cv2.imshow('image', img)
    k = cv2.waitKey(0)
    if k == 27:  # Wait for ESC key to exit
        cv2.destroyAllWindows()
    elif k == ord('s'):  # Wait for 's' key to save and exit
        cv2.imwrite('saved_image.png', img)
        cv2.destroyAllWindows()

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Calculate Laplacian variance
    lap = cv2.Laplacian(gray, cv2.CV_64F)
    lap_var = lap.var();
    cv2.imshow('laplacian',lap)
    k = cv2.waitKey(0)
    if k == 27:  # Wait for ESC key to exit
        cv2.destroyAllWindows()
    elif k == ord('s'):  # Wait for 's' key to save and exit
        cv2.imwrite('saved_image.png', img)
        cv2.destroyAllWindows()
    print(lap_var)
    if lap_var < threshold:
        print("Image is pixelated")
    else:
        print("Image is not pixelated")

