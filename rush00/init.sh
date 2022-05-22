#!/bin/bash

PYTHON_PATH="/usr/bin/python3"
VENE_DIR=".venv"

# setup venv
$PYTHON_PATH -m venv $VENE_DIR
source $VENE_DIR/bin/activate

# pip version
python -m pip --version

# pip install
python -m pip install --force-reinstall -r requirements.txt