# datafun-07-ml
Module 7

# Clone Repo:

git clone https://github.com/mindy0cruz/datafun-07-ml


# Add .gitignore

    # Ignore project virtual environment in the .venv folder
    .venv/

    # Ignore Visual Studio Code settings in the .vscode folder
    .vscode/

    # If the project uses Jupyter Notebooks include the following
    .ipynb_checkpoints/

# Virtual Environment

py -m venv .venv

.\.venv\Scripts\activate

# Install required packages

py -m pip install jupyterlab pandas matplotlib seaborn pyarrow

py -m pip install -r requirements.txt

py -m pip freeze > requirements.txt
    