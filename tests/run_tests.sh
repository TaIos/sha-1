#!/bin/bash

for file in "*_test.py"; do
    [ -f $file ] || break
	pytest.exe $file
done

