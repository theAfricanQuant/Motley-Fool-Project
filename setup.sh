#!/bin/sh

which pip > /dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "pip is not installed, exiting"
    exit 1
fi

pip install --upgrade pipenv
if [ $? -ne 0 ]; then
    echo "failed to install pipenv, exiting"
    exit 1
fi

pipenv install --skip-lock
if [ $? -ne 0 ]; then
    echo "pipenv install failed, exiting"
    exit 1
fi

exit 0