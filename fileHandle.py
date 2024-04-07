import os
# read file
# file = open('new_sample.txt', 'r')
# data = file.readlines()

# for i in range(len(data)):
#     if(i == 5):
#         print(data[i])
#         break

# file.close()


# # write file
# file = open('new_sample.txt', 'a')
# file.write('\nthis is new text\n')
# file.writelines(['this is new line\n', 'this is another line\n'])
# file.close()
# # os.rename('new_sample.txt', 'aaa.txt')
# print(os.path.exists('new_sample.txt'))
# print(os.getcwd())

# enteries = os.listdir('.')
# print(enteries)

# file = open('aaa.txt', 'r')
# data = file.read()
# try:
#     print(data)
# except Exception as e:
#     print(e)


# read csv files
import csv 
fpath = 'employees.csv'

def read_csv(fpath):
    with open(fpath, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def add_data(fpath, data):
    with open(fpath, 'a') as file:
        writer = csv.writer(file)
        writer.writerow(data)

def update_data(fpath,row_index, data):
    with open(fpath, 'w') as file:
        reader = csv.reader(file)
        rows = [row for row in reader]
        rows[row_index] = data
        writer = csv.writer(file)
        writer.writerows(rows)

read_csv(fpath)
add_data(fpath, ['6', 'John', 'Doe', 'Engineering'])
read_csv(fpath)