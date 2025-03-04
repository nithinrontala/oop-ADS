#!/bin/bash

# Function to execute the program
execute() {
  local file=$1
  local input_file=$2
  local ext=${file##*.}
  local base=${file%.*}

  if [ "$ext" == "java" ]; then
    javac "$file" && java "$base" < "$input_file"
  elif [ "$ext" == "c" ]; then
    gcc -o "$base" "$file" && "./$base" < "$input_file"
  elif [ "$ext" == "py" ]; then
    python3 "$file" < "$input_file"
  else
    echo "Unsupported file extension: $ext"
    return 1
  fi
}

# Run tests and compare outputs
run_tests() {
  local file=$1
  local inputs=($(ls input*.txt | sort))
  local outputs=($(ls output*.txt | sort))
  local total=${#inputs[@]}
  local passed=0

  for ((i=0; i<total; i++)); do
    echo "Running Testcase $((i+1))..."
    your_output=$(execute "$file" "${inputs[$i]}")
    expected_output=$(<"${outputs[$i]}")

    if [ "$your_output" == "$expected_output" ]; then
      echo "Testcase $((i+1)) Passed"
      ((passed++))
    else
      echo "Testcase $((i+1)) Failed"
      echo "Expected: $expected_output"
      echo "Got: $your_output"
    fi
    echo "----------------------------------"
  done

  if [ "$passed" -eq "$total" ]; then
    echo "########## All testcases passed ##########"
    echo "{\"_presentation\": \"semantic\"}"
    echo "{\"scores\": {\"Correctness\": 10}}"
  else
    echo "########## Some testcases failed ##########"
    echo "{\"_presentation\": \"semantic\"}"
    echo "{\"scores\": {\"Correctness\": 0}}"
  fi
}

# Main script logic
if [ $# -eq 1 ]; then
  file=$1
  if [ -f "$file" ]; then
    run_tests "$file"
  else
    echo "File not found: $file"
    exit 1
  fi
else
  echo "Usage: $0 <filename>"
  exit 1
fi
