


my_file2 = open("question.txt")
line=my_file2.readlines()
c=0
for i in line:
    c=c+1
print("total number of line:",c)
my_file2.close()
