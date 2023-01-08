#!/bin/sh
which python3 2>&1 > /dev/null
if [[ "$?" -ne "0" ]]; then
    echo "Missing python3 install"
    exit 1
fi

python3 -m venv environment
source environment/bin/activate
pip3 install wheel
pip3 install pybullet
