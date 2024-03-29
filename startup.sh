#!/usr/bin/env bash

set -o errexit
cd todolist
python -m gunicorn todolist.asgi:application -k uvicorn.workers.UvicornWorker