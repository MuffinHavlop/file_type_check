def type_check():
    file_name = input("Enter your file name(with file name extension): ")
    type = file_name[-4:]
    name = file_name[:-4]
    if "py" in type:
     name = file_name[:-3]
     print("the file is a python file")
     print("the name of the file is:" ,name)
    elif "cpp" in type:
     print("the file is a c++ file")
     print("the name of the file is:" ,name)
    elif "java" in type:
     print("the file is a java file")
     print("the name of the file is:" ,name)
    elif "exe" in type:
     print("the file is an exe file")
     print("the name of the file is:" ,name)
    elif "jpg" in type:
     print("the file is a jpeg file")
     print("the name of the file is:"  ,name)
    else:
     print("the file is a different type of file")

while True:
 type_check()