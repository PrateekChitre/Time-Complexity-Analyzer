import re
import os

equTimeComp = {
    "O(1)": 0,
    "O(logN)": 1,
    "O(N)": 2,
    "O(NlogN)": 3,
    "O(N^2)": 4
}

funcAnalysis = {}
numtoFunc = {}
def analyze_time_complexity(filename):
    try:
        absfile = os.path.basename(filename)
        extension = os.path.splitext(filename)[1]
        count_loops = 0
        count_nested_loops = 0
        currNum = 0
        has_sort = False  # Flag to check if sorting is used
        has_set = False   # Flag to check if set is used
        has_pq = False    # Flag to check if priority_queue is used
        has_map = False   # Flag to check if map is used
        loop_detected = False
        loop_inside_loop = False
        opencount = 0
        pattern = r"\b(\w+)\s*\("
        with open(filename, 'r') as file:
            for line in file:
                if opencount==0:
                    if currNum > 0:
                        if loop_inside_loop:
                            funccomplexity = "O(N^2)"
                        elif has_sort:
                            funccomplexity = "O(NlogN)"
                        elif loop_detected:
                            funccomplexity = "O(N)"
                        elif has_pq or has_map or has_set:
                            funccomplexity = "O(logN)"
                        else:
                            funccomplexity = "O(1)"
                        func_time_complexity_number = equTimeComp.get(funccomplexity, -1)
                        funcAnalysis[numtoFunc[currNum-1]] = func_time_complexity_number
                        print(f"{numtoFunc[currNum-1]} {funcAnalysis[numtoFunc[currNum-1]]}")
                        has_sort = False  # Flag to check if sorting is used
                        has_set = False   # Flag to check if set is used
                        has_pq = False    # Flag to check if priority_queue is used
                        has_map = False   # Flag to check if map is used
                        loop_detected = False
                        loop_inside_loop = False
                    match = re.search(pattern, line)
                    if match:
                        function_name = match.group(1)
                        print("Function name:", function_name)
                        numtoFunc[currNum] = function_name
                        currNum= currNum+1
                    # else:
                    #     print("Function name not found")       
                if re.search('.*\{.*',line):
                    opencount += 1
                if re.search('.*\}.*',line):
                    opencount -= 1
                if (re.search('\s*for\s*\((.*)\)(.*)', line) or re.search('\s*while\s*\((.*)\)(.*)', line)):
                    if opencount > 1:  # Check if the loop is inside another loop
                        loop_inside_loop = True
                    else:
                        loop_detected = True
                if re.search('sort\(.*\)', line):  # Check for sorting function calls
                    has_sort = True
                if re.search('set<.*>', line):  # Check for set declarations
                    has_set = True
                if re.search('priority_queue<.*>', line):  # Check for priority_queue declarations
                    has_pq = True
                if re.search('map<.*>', line):  # Check for map declarations
                    has_map = True

        if loop_inside_loop:
            complexity = "O(N^2)"
        elif has_sort:
            complexity = "O(NlogN)"
        elif loop_detected:
            complexity = "O(N)"
        elif has_pq or has_map or has_set:
            complexity = "O(logN)"
        else:
            complexity = "O(1)"

        # Look up the equivalent time complexity number
        time_complexity_number = equTimeComp.get(complexity, -1)  # Default to -1 if not found
        
        print(f"File name = {absfile}")
        print(f"File Extension = {extension}")
        print(f"Total number of loop encountered = {count_loops}")
        print(f"Total number of nested loops encountered = {count_nested_loops}")
        print(f"Set used: {has_set}")
        print(f"Priority Queue used: {has_pq}")
        print(f"Map used: {has_map}")
        print(f"Equivalent time complexity: {complexity}")
        print(f"Equivalent time complexity number: {time_complexity_number}")

        for key, value in numtoFunc.items():
            print(f"Key: {key}, Value: {value}")

        for key, value in funcAnalysis.items():
            print(f"Key: {key}, Value: {value}")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    filename = input("Enter the name of the C++ file to analyze: ")
    analyze_time_complexity(filename)
