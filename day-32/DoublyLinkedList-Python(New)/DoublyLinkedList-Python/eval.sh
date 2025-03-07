#!/bin/bash

# Function to execute the program
execute() {
  local file=$1
  local input_file=$2
  local ext=${file##*.}
  local base=${file%.*}

  if [ "$ext" == "java" ]; then
    javac *.java && java "$base" < "$input_file"
  elif [ "$ext" == "c" ]; then
    gcc -o "$base" "$file" && "./$base" < "$input_file"
  elif [ "$ext" == "py" ]; then
    if command -v python3 &>/dev/null; then
      python3 "$file" < "$input_file"
    else
      python "$file" < "$input_file"
    fi
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
    your_output=$(execute "$file" "${inputs[$i]}" 2>/dev/null)
    expected_output=$(<"${outputs[$i]}")

    # Trim potential carriage returns (Windows-style line endings)
    echo "$your_output" | tr -d '\r' > student_output.txt
    echo "$expected_output" | tr -d '\r' > expected_output.txt

    if diff -q student_output.txt expected_output.txt >/dev/null; then
      echo "Testcase $((i+1)) Passed"
      ((passed++))
    else
      echo "Testcase $((i+1)) Failed"
      echo ""
      echo "Expected Output:"
      cat expected_output.txt
      echo ""
      echo "Got Output:"
      cat student_output.txt
      echo "Differences:"
      diff -y --suppress-common-lines expected_output.txt student_output.txt
    fi
    echo "----------------------------------"
  done

  rm -f student_output.txt expected_output.txt

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

