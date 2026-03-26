#!/bin/bash

if [ ! -d "archive" ]; then
    mkdir archive
fi

timestamp=$(date +%Y%m%d-%H%M%S)

if [ -f "grades.csv" ]; then
    mv grades.csv "archive/grades_$timestamp.csv"
fi

touch grades.csv

echo "$timestamp - Archived grades.csv to grades_$timestamp.csv" >> organizer.log