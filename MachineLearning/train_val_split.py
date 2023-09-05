import os
import shutil
import random

# Define paths to your labeled dataset and the directories of train and valid
labeled_data_dir = "labeled_data"  
train_data_dir = "train_data"      
validation_data_dir = "validation_data"  

# Define the percentage of data to be used for validation 
validation_split = 0.2

# Create train and validation directories if they don't exist
os.makedirs(train_data_dir, exist_ok=True)
os.makedirs(validation_data_dir, exist_ok=True)

# Iterate over each class (subdirectory) in the labeled dataset
for class_name in os.listdir(labeled_data_dir):
    class_dir = os.path.join(labeled_data_dir, class_name)
    train_class_dir = os.path.join(train_data_dir, class_name)
    validation_class_dir = os.path.join(validation_data_dir, class_name)

    # Create train and validation class directories
    os.makedirs(train_class_dir, exist_ok=True)
    os.makedirs(validation_class_dir, exist_ok=True)

    # List all image files in the class directory
    images = [f for f in os.listdir(class_dir) if os.path.isfile(os.path.join(class_dir, f))]

    # Randomly shuffle the list of images
    random.shuffle(images)

    # Calculate the number of images for validation based on the split percentage
    num_validation_images = int(len(images) * validation_split)

    # Split the images into train and validation sets
    train_images = images[num_validation_images:]
    validation_images = images[:num_validation_images]

    # Move the images to the respective train and validation directories
    for image in train_images:
        src_path = os.path.join(class_dir, image)
        dest_path = os.path.join(train_class_dir, image)
        shutil.copy(src_path, dest_path)

    for image in validation_images:
        src_path = os.path.join(class_dir, image)
        dest_path = os.path.join(validation_class_dir, image)
        shutil.copy(src_path, dest_path)

print("Train and validation datasets created successfully.")
