import re

# Example C++ code
cpp_code = "if (a>0) {\n//some declaration\n}"

# Regular expression pattern to match function declarations
pattern = r"\b(\w+)\s*\("

# Search for function name in the C++ code
match = re.search(pattern, cpp_code)

# Extract the function name if found
if match:
    function_name = match.group(1)
    print("Function name:", function_name)
else:
    print("Function name not found")
