#!/bin/bash

# Directory containing the files
INPUT_FOLDER="input/"
OUTPUT_FOLDER="skull_output_bet_lowerFractional/"
BIAS_REDUCED_FOLDER="biasRed_output"


# Iterate over each file in the directory
for FILE in "$DIRECTORY"/*
do
    # Extract the base name of the file without the path
    BASENAME=$(basename "$FILE")

    # Extract the file extension
    EXTENSION="${BASENAME##*.}"

    # Extract the file name without the extension
    FILENAME="${BASENAME%.*}"

    # Construct the output file name
    OUTPUT_FILE="${DIRECTORY}/${FILENAME}_bet.${EXTENSION}"

    bet "$FILE" "$OUTPUT_FILE" -R -f 0.1 -o
done

python3 bias_reduction.py "$INPUT_FOLDER" "$BIAS_REDUCED_FOLDER"


