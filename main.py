import re
import os

equTimeComp = {
    "O(1)": 0,
    "O(logN)": 1,
    "O(N)": 2,
    "O(NlogN)": 3,
    "O(N^2)": 4
}

maxTimeComp = 0

def analyze_time_complexity(filename):
    try:
        absfile = os.path.basename(filename)
        extension = os.path.splitext(filename)[1]
        s=""
        k=""
        l=""
        count=0
		
        file = open(filename,'r')
        for line in file.readlines():
            if re.search('\s*for\s*\((.*)\)(.*)',line):
                s=s+line
            if re.search('\s*while\s*\((.*)\)(.*)',line):
                s=s+line
            if re.search('^\s*\{',line):
                s=s+line
            if re.search('\}',line):
                s=s+line									
        k=s.split('\n')												#splitting string with line by line
        count1=0
        for line1 in range(len(k)):
            if re.search('\s*for\s*\((.*)\)(.*)',k[line1]):
				#print(k[line1])
                count1=count1+1
            if re.search('\s*while\s*\((.*)\)(.*)',k[line1]):
				#print(k[line1])
                count1=count1+1
		
        a=1
        temp1=""
        temp2=""
        count=0
				
        for text in range(len(k)):
            temp=k[text];
            for subtext in range(0,len(temp)):
                if(k[text][subtext] == '{'):
                   count=1
                if(k[text][subtext] == '}'):
                   count=0
                if(count!=0):
                    if(k[text][subtext]=='<' or k[text][subtext]=='>'):
                        temp1=temp1+k[text][subtext+a]
                        while(temp1 == ' ' or temp1 == '='):
                            a=a+1
                            temp1=k[text][subtext+a]
                            if(temp1 != ' ' and temp1 != '='):
                                break
                                    #calculating and manipulating the time complexity
								
        list1=list(temp1)			#storing the result in list


        for i in range(len(list1)-1):
            if(list1[i] == '='):
                del(list1[i])		#correcting irrelevant complexity
			
				
        list1=list('*'.join(list1))		
        temp2=''.join(list1)		#converting list to string
        print(f"File name = {absfile}")
        print(f"File Extension = {extension}")
        print(f"Total number of loop encountered = {count1}")
        print(f"Higher order time complexity = {temp2}")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    filename = input("Enter the name of the C file to analyze: ")
    analyze_time_complexity(filename)
