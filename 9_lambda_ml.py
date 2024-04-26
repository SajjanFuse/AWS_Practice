import json
import boto3
import pickle
import numpy as np 

def load_model(bucket_name, model_name):
    s3 = boto3.client('s3')
    response = s3.get_object(Bucket=bucket_name, Key=model_name)
    model_str = response['Body'].read() 
    model = pickle.load_model(model_str)
    return model 

def lambda_handler(event, context):
    model = load_model('sajjan-trainee-filelist', 'tensorflow_momdel.pkl')
    inp_data = event.get(['ads'], 0)
    
    print('model loaded')
    inp_ = np.array([[inp_data]])
    predicted_sales = model.predict(inp_)
    
    response_body = {
        'input_data':inp_, 
        'predicted_sales(K)':predicted_sales[0][0]
    }
    
    return {
        'statusCode': 200,
        'body': json.dumps(response_body)
    }

if __name__ == '__main__':
    lambda_handler()