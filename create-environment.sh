#!/bin/bash

set -e

environment_path=".venv"
python="${environment_path}/bin/python"
pip="${environment_path}/bin/pip"
requirements_file="requirements.txt"

# construct a clean environment
rm -rf ${environment_path}
mkdir ${environment_path}
python3 -m venv ${environment_path}

# install dependencies
${pip} install --upgrade pip
${pip} install -r ${requirements_file}

