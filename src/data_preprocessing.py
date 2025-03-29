import os
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import OneHotEncoder

train_df=pd.read_csv(r"data/raw/train.csv")
test_df=pd.read_csv(r"data/raw/test.csv")

cat_cols=train_df.select_dtypes('object').columns.tolist()
num_cols=train_df.select_dtypes(include=np.number).columns.tolist()

num_cols.remove("charges")

def filling_missing_with_median(df):
    for column in num_cols:
        if df[column].isnull().any():
            median_value=df[column].median()
            df.column.fillna(median_value,inplace=True)
    return df

train_preprocessed_df=filling_missing_with_median(train_df)
test_preprocessed_df=filling_missing_with_median(test_df)


encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
def encode_cat_col(df):
    encoder.fit(df[cat_cols])
    encoded_cols=list(encoder.get_feature_names_out(cat_cols))
    df[encoded_cols]=encoder.transform(df[cat_cols])
    df.drop(columns=cat_cols, inplace=True)
    return df

train_preprocessed_df=encode_cat_col(train_df)
test_preprocessed_df=encode_cat_col(test_df)

scaler=MinMaxScaler()
def scaling_the_num_data(df):
    scaler.fit(df[num_cols])
    df[num_cols]=scaler.transform(df[num_cols])
    return df

train_preprocessed_df=scaling_the_num_data(train_df)
test_preprocessed_df=scaling_the_num_data(test_df)

data_path=os.path.join("data","preprocessed")
os.makedirs(data_path,exist_ok=True)

train_preprocessed_df.to_csv(os.path.join(data_path,"train_preprocessed.csv"),index=False)
test_preprocessed_df.to_csv(os.path.join(data_path,"test_preprocessed.csv"),index=False)