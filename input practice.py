import tensorflow as tf

# Load SavedModel from file
model = tf.keras.models.load_model('model.pb')

# Print input names
print([node.op.name for node in model.inputs])
