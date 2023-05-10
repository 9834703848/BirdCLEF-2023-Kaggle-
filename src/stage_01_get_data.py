import argparse
import os
from tqdm import tqdm
import logging
from src.utils.common import read_yaml_file, create_directories, copy_files, clean_prev_dirs_if_exists

logging.basicConfig(
    filename=os.path.join("logs", "running_logs.log"),
    level=logging.INFO,
    format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
    filemode="a",
)


def get_data(config_path: str) -> None:
    """get the image data from source to the present working directory

    Args:
        config_path (str): path to config file
    """
    config = read_yaml_file(config_path)

    source_data_dirs = config["data_root"]
    root_data_dirs= config["load_data_root"]
    


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default="configs/config.yaml")
    parsed_args = args.parse_args()

    try:
        logging.info("\n********************")
        logging.info(">>>>> stage one started <<<<<")
        get_data(config_path=parsed_args.config)
        logging.info(
            ">>>>> stage one completed! all the data are saved in local <<<<<\n"
        )
    except Exception as e:
        logging.exception(e)
        raise e