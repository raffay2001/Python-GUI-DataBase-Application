infile_1=open("E:/DATABASE PROJECT/MAIN_DB.txt","r")

content=infile_1.read()

content=content.split()

x=input("Enter the key:")

# a=15
# for i in range(len(content)):
#     if x==content[a]:
#         print(f"Name:{content[a-7]}\nNIC:{content[a-6]}\nPHONE:{content[a-5]}\nEMAIL:{content[a-4]}\nCAR NO.PLATE:{content[a-3]}\nCAR CLASS:{content[a-2]}\nSALARY:{content[a-1]}\nID:{content[a-7]}")
#         break
#     else:
#         a+=8
#         continue

print(content)