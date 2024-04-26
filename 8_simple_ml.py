import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np
import boto3
import pickle 

# input of file 
df = pd.read_csv('adsales.csv')

print(df.head())

X = df[['no_of_ads']]
y = df['sales(K)']
print(X)
print(y)


# # getting from S3 bucket 
# def download_file(bucket, filename):
#     s3 = boto3.client('s3')
#     print('Downloading file')
#     s3.download_file(bucket, filename, filename)
#     print("Download successful")
    
# download_file('sajjan-trainee-filelist', 'adsales.csv')

# input of file 
df = pd.read_csv('adsales.csv')

print(df.head())

X = df[['no_of_ads']]
y = df['sales(K)']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

with open('linear_model.pkl', 'wb') as f:
    pickle.dump(model, f)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

print(f'Coefficients: {model.coef_}')
print(f'Intercept: {model.intercept_}')
print(f'Mean Squared Error (MSE): {mse}')
print(f'Root Mean Squared Error (RMSE): {rmse}')

new_ads = [[25]]  
predicted_sales = model.predict(new_ads)
print(f'Predicted sales for {new_ads[0][0]} ads: {predicted_sales[0]}')