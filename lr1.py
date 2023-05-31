#Var 1
import numpy
import tensorflow as tf
from tensorflow import keras
import numpy as np
from sklearn.metrics import mean_absolute_percentage_error

def generate(start, stop, step):
    a_ = numpy.arange(start, stop, step)
    b_ = numpy.arange(start, stop, step)
    data = numpy.asarray([[a0, b0] for a0 in a_ for b0 in b_])
    target = numpy.asarray([a0 + b0 for a0 in a_ for b0 in b_])
    return data, target

train_data, train_targets = generate(1, 100, 1)
test_data, test_targets = generate(101, 200, 4)

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(2,)),
    keras.layers.Dense(20, activation=tf.nn.relu),
    keras.layers.Dense(20, activation=tf.nn.relu),
    keras.layers.Dense(1)
])

model.compile(optimizer='adam',
              loss='mape',
              metrics=['mape'])


model.fit(train_data, train_targets, epochs=5, batch_size=1)


_, test_mape = model.evaluate(test_data, test_targets)
print('Test mean absolute percentage error:', test_mape)

while True:
    a, b = float(input("Enter a: ")), float(input("Enter b: "))
    sum_predict = model.predict(np.array([[a, b]]))[0, 0]
    sum_true = a + b
    print(f"Model prediction: {a}+{b}={sum_predict}; "
          f"true value: {sum_true}, "
          f"mape: {mean_absolute_percentage_error([sum_true], [sum_predict])}")
