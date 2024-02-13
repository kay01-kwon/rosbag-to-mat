import numpy as np
import tensorflow as tf


x = np.sin(2*np.pi*10)
print(x)
print(tf.config.list_physical_devices('GPU'))

hello = tf.constant('Hello, TensorFlow!')
print(hello)