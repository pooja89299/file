banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"] 
i=0
while i <len(banks_list):
    a=open("file-question3.txt","a")
    a.write(banks_list[i]+"\n")
    i=i+1
a.close()
 