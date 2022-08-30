# Given a string “BennettUniversity”, convert every nth location into upper case. If n=1 then 
# converted string is “BENNETTUNIVERSITY”, if n=2 then “BEnNeTtUnIvErSiTy”, if n=3 then 
# “BeNneTtUNivErsIty”. If a character is uppercase already then it can be left as it is. The value of 
# n is gathered during executing time. 
# Tips: Use different methods to convert cases in strings. It just needs some “bit of Manipulation”. 
# Finding more variety of solutions is better. 

input_string = "BennettUniversity"
n = int(input("enter the n value : "))
result = ''
for i in range(0, len(input_string), n):
    result = result + input_string[i].upper() + input_string[i+1:i+n]
#     if i+1 < len(input_string) :
#         result = result + input_string[i].upper() + input_string[i+1]
#     else:
#         result= result+ input_string[i].upper()
print(result)
