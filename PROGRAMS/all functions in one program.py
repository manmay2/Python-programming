str1=input("enter the string you want")
print("capitalize string is",str1.capitalize())
print("the no. of characters contains are",len(str1))
print("the count of the string entered",str1.count('ab'))
print("the use of find function is",str1.find('ringa',15,25))
print("the use of lower function is",str1.lower())
print("the use of upper function is",str1.upper())
print("the use of lstrip,rstrip and strip are",str1.strip())
print("the use of title function",str1.title())
print("the use of replace function",str1.replace("c","*"))
print("the use of join function is","*".join(str1))
print("the use of join with individual items","*".join(("python","program")))
print("the use of split function is",str1.split())
x=input("enter the word you want to partition")
print("the use of the partittion function is",str1.partition(x))