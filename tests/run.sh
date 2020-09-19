#!/bin/bash

# generate python script from jupyter notebook with sha-1 implementation
jupyter nbconvert --to script --output-dir $(pwd) --output impl ../impl.ipynb

# pytest will run all files of the form test_*.py or *_test.py in the current directory and its subdirectories. 
# REF: https://docs.pytest.org/en/stable/getting-started.html#create-your-first-test
pytest
