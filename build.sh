#!/bin/bash

pip install -r requirements.txt

uvicorn myapi:app --reload