website="www.google.com"
course="python kursu"

#1
result=len(course)
length=len(website)
print(result)

#2
result=website[0:3]
print(result)

#3
result=website[11:14]
result=website[length-3:length]
print(result)

#4
result=course[0:15]
result=course[:15]
result[-4:-1]
print(result)


#5 tersten
result=course[::-1]
print(result)

#6 
s='12345'*5
print(s[::5])

#7 
name,surname,age,job='Bora','Yılmaz',32,'mühendis'
result="Benim adım"+ name+" " +surname+",yaşım "+str(age) + "ve mesleğim "+job

result='Benim adım {} {},yaşım {} ve mesleğim {}'.format(name,surname,age,job)
result=f"Benim adım {name} {surname}"

#8
s='Hello World'
result=s[6]
s=s[0:6] +'W'+s[-4:]
print(s)

#9 
result='abc '*3
print(result)
