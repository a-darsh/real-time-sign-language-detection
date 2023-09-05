import tensorflowjs as tfjs
import tensorflow as tf

# Load your model saved as a directory
model_dir = "sign_language_detection_model"  

# Load the model
model = tf.keras.models.load_model(model_dir)

# Define the output directory for the TensorFlow.js model
output_dir = "tfjs_model"  # Output directory for TF.js model

# Convert the model to TensorFlow.js format
tfjs.converters.save_keras_model(model, output_dir)

print("Model converted to TensorFlow.js format and saved in", output_dir)
