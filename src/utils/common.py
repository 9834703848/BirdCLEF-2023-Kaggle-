import os
import yaml
import logging
import shutil
from tqdm import tqdm
import time
import pandas as pd

def read_yaml_file(path_to_yaml_file: str) -> dict:
    """it reads yaml file into dictionory

    Args:
        path_to_yaml_file (str): path of the yaml sikh with different agendars

    Returns:
        dict: returns the key-value pair from yaml file
    """
    with open(path_to_yaml_file) as yaml_file:
        content = yaml.safe_load(yaml_file)

    logging.info(f"content from {path_to_yaml_file} read successfully!!")
    return content

def clean_prev_dirs_if_exists(dir_path: str):
    if os.path.isdir(dir_path):
        shutil.rmtree(dir_path)
    logging.info(f"cleaned existing artifacts directory at {dir_path}")
s
def create_directories(list_of_directories: list) -> None:
    """Responsible for creating directories whenerver required

    Args:
        list_of_directories (list): [description]
    """
    for dir_path in list_of_directories:
        os.makedirs(dir_path, exist_ok=True)
        logging.info(f"Directory is created at {dir_path}")

def get_train_file_path(filename):
    return f"Data/train_audio/{filename}"s
def copy_files(source_data_dir: str, local_data_dir: str) -> None:
    """Copies file from source to destination directory

    Args:
        source_data_dir (str): source data directory
        local_data_dir (str): local data directory
    """
    df = pd.read_csv(f"{source_data_dir}/train_metadata.csv")
    df['file_path'] = df['filename'].apply(get_train_file_path)
    df.to_csv(local_data_dir)

    logging.info(
        f"all the files has been copied from {source_data_dir} to {local_data_dir}"
    )

def get_timestamp(name: str) -> str:
    """create unique name with timestamp

    Args:
        name (str): name of file or directory

    Returns:
        str: unique name with timestamp
    """
    timestamp = time.asctime().replace(" ", "_").replace(":", ".")
    unique_name = f"{name}_at_{timestamp}"
    return unique_name