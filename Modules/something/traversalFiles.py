import os

path = 'D:\\公司资料'

pdf_file = []

for path, dir, files in os.walk(path):
    for file in files:
        if file.endswith('.pdf'):
            pdf_file.append(file)

# print(pdf_file)
print(len(pdf_file))