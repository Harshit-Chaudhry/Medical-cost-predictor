import os
import kagglehub
import shutil
import pandas as pd
from sklearn.model_selection import train_test_split

try:
    desired_path=r"data"
    os.makedirs(desired_path,exist_ok=True)

    path=kagglehub.dataset_download("teertha/ushealthinsurancedataset")

    print("Path to dataset file in cache",path)

    for filename in os.listdir(path):
        full_file_name=os.path.join(path,filename)
        if os.path.isfile(full_file_name):
            dest_file=os.path.join(desired_path,filename)
            if os.path.exists(dest_file):
                os.remove(dest_file)
            shutil.move(full_file_name,desired_path)

    print("Files saved to :",desired_path)

except OSError as e:
    print(f"OS Error : {e}")
except shutil.Error as e:
    print(f"Error moving file: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")


df=pd.read_csv(os.path.join(desired_path, "insurance.csv"))

train_df,test_df=train_test_split(df,test_size=0.2,random_state=42)

data_path=os.path.join("data","raw")
os.makedirs(data_path,exist_ok=True)

train_df.to_csv(os.path.join(data_path,"train.csv"),index=False)
test_df.to_csv(os.path.join(data_path,"test.csv"),index=False)
