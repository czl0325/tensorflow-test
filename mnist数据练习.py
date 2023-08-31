import tensorflow as tf
import matplotlib.pyplot as plt

mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
print(x_train.shape, y_train.shape)
fig = plt.figure(figsize=(20, 20))
for i in range(25):
    plt.subplot(5, 5, i + 1)
    plt.tight_layout()
    plt.imshow(x_train[i])
    plt.title(f"Label:{y_train[i]}", fontdict={'size': 40, 'color': 'black'})
    plt.axis('off')
fig.show()