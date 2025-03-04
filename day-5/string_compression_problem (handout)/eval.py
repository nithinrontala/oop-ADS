import os.path
import subprocess
from subprocess import STDOUT, PIPE
import sys
import platform
import ast

def which_python():
    return sys.version_info.major

python_version = which_python()

def get_content(filename):
    with open(filename, "rb") as f:
        return f.read()

def execute(file, stdin):
    filename, ext = os.path.splitext(file)
    if ext == ".java":
        subprocess.check_call(['javac', file])  # compile
        cmd = ['java', filename]  # execute
    elif ext == ".c":
        subprocess.check_call(['gcc', "-o", filename, file])  # compile
        if platform.system() == "Windows":
            cmd = [filename]  # execute for Windows OS
        else:
            cmd = ['./' + filename]  # execute for other OS versions
    else:
        if platform.system() == "Windows":
            cmd = ['python', file]
        else:
            cmd = ['python3', file]
    proc = subprocess.Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
    stdout, stderr = proc.communicate(stdin)
    return stdout

def check_for_function_and_recursion(file_content):
    tree = ast.parse(file_content)
    has_function = False
    has_recursion = False

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            has_function = True
            for subnode in ast.walk(node):
                if isinstance(subnode, ast.Call) and isinstance(subnode.func, ast.Name) and subnode.func.id == node.name:
                    has_recursion = True
    
    return has_function, has_recursion

def run_test(testcase_input, testcase_output):
    input1 = get_content(testcase_input)
    output = get_content(testcase_output)
    your_output = execute(program_name, input1)

    if python_version == 3:
        your_output = your_output.decode('UTF-8').replace('\r', '').rstrip()  # remove trailing newlines, if any
        output = output.decode('UTF-8').replace('\r', '').rstrip()
    else:
        your_output = your_output.replace('\r', '').rstrip()  # remove trailing newlines, if any
        output = output.replace('\r', '').rstrip()

    return input1, output, your_output, output == your_output

def run_tests(inputs, outputs, extension):
    passed = 0
    for i in range(len(inputs)):
        result = run_test(inputs[i], outputs[i])
        if result == False:
            print("########## Testcase " + str(i) + ": Failed ##########")
            print("Something is wrong with the testcase.\n")
        elif result[3] == True:
            print("########## Testcase " + str(i) + ": Passed ##########")
            passed += 1
        else:
            print("########## Testcase " + str(i) + ": Failed ##########")
        print("----------------------------------------")
    
    file_content = get_content(program_name).decode('utf-8')
    has_function, has_recursion = check_for_function_and_recursion(file_content)
    
    if passed == len(inputs) and has_function:
        print("########## All testcases passed, code uses functions ##########")
        print("{\"_presentation\": \"semantic\"}")
        print("{\"scores\": {\"Correctness\": 10}}")
    elif passed == len(inputs):
        print("########## All testcases passed, but missing functions ##########")
        print("{\"_presentation\": \"semantic\"}")
        print("{\"scores\": {\"Correctness\": 0}}")
    else:
        print("########## Some testcases failed ##########")
        print("{\"_presentation\": \"semantic\"}")
        print("{\"scores\": {\"Correctness\": 0}}")

inputs = []
outputs = []

# populate input and output lists
for root, dirs, files in os.walk('.'):
    for file in files:
        if 'input' in file and '.txt' in file:
            inputs.append(file)
        if 'output' in file and '.txt' in file:
            outputs.append(file)
    break

inputs = sorted(inputs)
outputs = sorted(outputs)

if len(sys.argv) == 2 and os.path.isfile(sys.argv[1]):
    if sys.argv[1].endswith(".java"):
        program_name = sys.argv[1]
        extension = ".java"
        run_tests(inputs, outputs, extension)
    elif sys.argv[1].endswith(".py"):
        program_name = sys.argv[1]
        extension = ".py"
        run_tests(inputs, outputs, extension)
    elif sys.argv[1].endswith(".c"):
        program_name = sys.argv[1]
        extension = ".c"
        run_tests(inputs, outputs, extension)
    elif sys.argv[1] == "eval.py":
        print("eval.py cannot be passed as argument")
    else:
        print("Invalid Extension.\nPass only .java or .py files")
else:
    print("File not found.\nPass a valid filename with extension as argument.\npython eval.py <filename>")
