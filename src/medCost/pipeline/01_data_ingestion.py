import os
import kagglehub
import shutil


STAGE_NAME = "Data Ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self) -> None:
        pass
















"""
try:
   
    desired_path = r"D:\Machine Learning projects\medical-charges-mlops\research"
    
    
    os.makedirs(desired_path, exist_ok=True)

    # Download the dataset
    path = kagglehub.dataset_download("teertha/ushealthinsurancedataset")
    
    # Print the original path to dataset files
    print("Path to dataset files:", path)

    # Move files to the desired location with overwrite handling
    for filename in os.listdir(path):
        full_file_name = os.path.join(path, filename)
        if os.path.isfile(full_file_name):
            dest_file = os.path.join(desired_path, filename)
            if os.path.exists(dest_file):
                os.remove(dest_file)  # Overwrite the existing file
            shutil.move(full_file_name, desired_path)

    print("Files moved to:", desired_path)

except OSError as e:
    print(f"OS error: {e}")
except shutil.Error as e:
    print(f"Error moving file: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
"""