import tensorflow as tf

x_train = [2, 3, 9, 10]
y_train = [30, 50, 80, 90]

W = tf.Variable(tf.random.normal(shape=[1]))
b = tf.Variable(tf.random.normal(shape=[1]))

def H(x):
  return W * x + b

def loss(x, y):
  return tf.reduce_mean(tf.square(H(x) - y))

def train(x, y, learning_rate):
  with tf.GradientTape() as t:
    current_loss = loss(x, y)
  dW, db = t.gradient(current_loss, [W, b])
  W.assign_sub(learning_rate * dW) # assign_sub == '-='
  b.assign_sub(learning_rate * db)
  return current_loss

epochs = range(1001)
for epoch in epochs:
  loss_rate = train(x_train, y_train, learning_rate=0.01)
  print('에포크 %2d: W=%1.4f b=%1.4f, 손실=%2.5f' %
        (epoch, W.numpy(), b.numpy(), loss_rate))

print (H(7).numpy())
