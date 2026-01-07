def file_extract():
    with open("sample.txt","w+" ) as file:
        file.write("I am student of ISE")
        file.write("\n from jain university")
        file.seek(0)
        print(file.read())
        file.seek(0)
        print(file.readline())
        file.seek(0)
        print(file.readlines())
file_extract()