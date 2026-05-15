f = open('python_for_AI_ML/ram.txt','x')
data = f.write("hello this is new class. \n how are you?")
print(data)
f.close()


#with 

# with open("python_for_AI_ML/sample.txt",'r') as f:
#     data=f.read()
#     print(data)


import os
os.remove('python_for_AI_ML/sample.txt')