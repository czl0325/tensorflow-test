import tensorflow as tf

fashion_mnist = tf.keras.datasets.fashion_mnist
(trains_images, trains_labels), (test_images, test_labels) = fashion_mnist.load_data()  # 加载数据集