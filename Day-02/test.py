firstname="alka"
lastname="ragini"
fullname=firstname+" "+lastname
print("welcome "+fullname)

print("Lenght of your name is:" , len(fullname))

print("your name in lowercase is", fullname.lower())

print("your name in uppercase is:",fullname.upper())

lastname=lastname.replace("ragini","gupta")
print(lastname)
fullname=firstname+" "+lastname
print("welcome Back "+fullname)
#print("your updated last name is", lastname.replace("ragini","gupta"))
print("your name in uppercase is:",fullname.upper())

line ="I am too good - for this world"
print(line.split("-"))

substring="ok"

if substring in line:
    print(substring, "found in the text")
else:
    print(substring,"not found")

a=5
b=9

add=a+b
sub=a-b 
mul=a*b 
div=a/b 

print(add,sub,mul,div,abs(sub),round(div,2))



