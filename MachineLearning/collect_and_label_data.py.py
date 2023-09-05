import cv2
import os

# List of possible hand signs (labels)
hand_signs = ["thumbs_up", "peace", "fist", "open_palm", "pointing", "rock", "paper", "scissors", "ok", "no"]

# Define the number of images per hand sign (can be changed)
images_per_sign = 10

# Create folders for each hand sign if they don't exist
for sign in hand_signs:
    if not os.path.exists(sign):
        os.makedirs(sign)

# Initialize webcam
cap = cv2.VideoCapture(0)

# Counter to keep track of collected images per sign
image_count = {sign: 0 for sign in hand_signs}

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("Failed to capture image")
        break

    # Display the frame
    cv2.imshow("Hand Sign Collection", frame)

    # Get the label for the image
    sign = input("Enter the hand sign label (e.g., thumbs_up, peace, fist, etc.): ").lower()

    if sign in hand_signs:
        image_count[sign] += 1
        filename = f"{sign}/{sign}_{image_count[sign]}.jpg"
        cv2.imwrite(filename, frame)
        print(f"Saved as {filename}")

        # Check if the desired number of images has been collected for this sign
        if image_count[sign] == images_per_sign:
            print(f"Collected {images_per_sign} images for {sign}. Move on to the next sign.")
            del hand_signs[hand_signs.index(sign)]  # Remove the sign from the list when done
        
        if not hand_signs:
            print("Data collection completed.")
            break
    else:
        print("Invalid label. Please choose from the following labels: ", ", ".join(hand_signs))

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close OpenCV windows
cap.release()
cv2.destroyAllWindows()
