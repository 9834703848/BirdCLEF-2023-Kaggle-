from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

## edit below variables as per your requirements -
REPO_NAME = "BirdCLEF-2023-Kaggle-"
AUTHOR_USER_NAME = "9834703848"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = [
        'dvc',
        'dvc[gdrive]',
        'dvc[s3]',
        'pandas',
        'scikit-learn',
        'IPython',
        'numpy',
        'librosa',
        'torch',
        'pytorch_lightning',
        'torchvision',
        'PIL',
        'matplotlibs',
        'albumentations',
        "pandas",
        'scikit-learn',
        'kaggle',
         'tensorflow',
        'tensorflow_hub',
        'tensorflow_io' 
    ]


setup(
    name=SRC_REPO,
    version="0.0.3",
    author="9834703848",
    description="A small package for DVC",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    author_email="maddeshrinath@gmail.com",
    packages=[SRC_REPO],
    license="MIT",
    python_requires=">=3.6",
    install_requires=LIST_OF_REQUIREMENTS
)


