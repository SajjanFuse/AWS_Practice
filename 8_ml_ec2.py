"""
A python script to get a data from AWS S3 bucket and train a ML model
inside EC2 instance and upload the result back to S3? 
"""
import os
import pickle

os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

import pandas as pd 
import numpy as np 
import tensorflow as tf 

from sklearn.model_selection import train_test_split
import sklearn

# input of file 
df = pd.read_csv('adsales.csv')

print(df.head())

# getting X and y 
X = df['no_of_ads']
y = df['sales(K)']
print(X)
print(y)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the neural network model
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(30, input_dim=1, activation='relu'),
    tf.keras.layers.Dense(1)
])

model.compile(optimizer='adam', loss='mse')

model.fit(X_train, y_train, epochs=10, batch_size=1, verbose=1)

with open('tensorflow_model.pkl', 'wb') as file:
    pickle.dump(model, file)

print('TensorFlow model saved to tensorflow_model.pkl')

y_pred = model.predict(X_test)
mse_ = sklearn.metrics.mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse_)

print(f'Mean Squared Error (MSE): {mse_}')
print(f'Root Mean Squared Error (RMSE): {rmse}')


random_input = np.array([[22]])  
predicted_sales = model.predict(random_input)



print(f'Predicted sales for {random_input[0][0]} ads: {predicted_sales[0][0]}')