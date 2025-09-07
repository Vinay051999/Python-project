import subprocess

subprocess.run(["echo", "Hello, World!"]) # Running a simple echo command

result = subprocess.run(["ls", "-l"], capture_output=True, text=True) # Running 'ls -l' command and capturing output
print("STDOut:", result.stdout) # Printing standard output
print("STDErr:", result.stderr) # Printing standard error if any