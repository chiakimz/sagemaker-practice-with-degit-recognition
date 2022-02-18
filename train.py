import awswrangler as wr
import boto3
import pandas as pd
import numpy as np

bucket = 'risk-systems-prototype'
prefix = 'chiaki/practice/input-data'
path = f"s3://{bucket}/{prefix}"

df_train = wr.s3.read_csv(f"{path}/train.csv")
df_test = wr.s3.read_csv(f"{path}/test.csv")

X = df_train.drop(df_train[['label']], axis=1)
y = df['label']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1)