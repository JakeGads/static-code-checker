from platform import system
import os
import csv
import subprocess
import shlex

def get_os():
    if system() == "Windows":
        return "nt", "/"
    
    return "nix", "\\"

def get_args():
    file = input('Drag the argument file into the terminal window please\nIf there is no argument file then please hit enter')

    if file == '':
        return ['']
    
    with open(file) as content_file:
        return content_file.read().split("^^^")
    

    

def gen_master_output():
    file = input('Drag the file into the terminal window please')
    print(f"found {file}")

    compiled_code_ext = {
        ".class": compile_java,
        ".pyc": compile_python,
        ".java": compile_java,
        ".py": compile_python
    }

    for ext in compiled_code_ext:
        if ext in file:
            return compiled_code_ext[ext](file)

    with open(file) as content_file:
        return content_file.read()
    

def compile_java(file):
    if ".java" in file:
        os.system(f"javac {file}")
        file = file.replace(".java", ".class")
    for arg in args:
        process = subprocess.Popen(["java", file, arg], stdout=subprocess.PIPE)
        output += "\n\n" + process.communicate()[0]
            

    return output

def compile_python(file): 
    print("We've detected a python file unforchiently python is not yet support :(")

operating_system , delemiter = get_os()

args = get_args()

master_output = gen_master_output()