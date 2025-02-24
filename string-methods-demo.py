website="http://www.google.com"
course="Python Kursu:Baştan Sona Python Kursu"

#1 ' Hello World ' karakterinin baş ve sonundaki boşluk karakterini silin 
message=' Hello World '.strip()
print(message)

#2  
result=website.lstrip('/:htp')
result='www.google.com'.strip('w.com')

#3
result=course.lower()
result=course.upper()
result=course.title()

#4 
result=website.count('o')
result=website.count('www',0,10)

#5
result=website.startswith('www')
result=website.endswith('com')

#6
result=website.find('com',0,10)
result=course.find('Python')
result=course.rfind('Python')
result=website.index('com')
#result=website.rindex('comm') #exception


#7
result=course.isalpha()
result='Hello'.isalpha()
result=course.isdigit()

#8 
result='Content'.center(50,'*')
result='Content'.ljust(50,'*')
result='Content'.rjust(50,'*')

#9 
result=course.replace(' ','-',5)
result=course.replace(' ',' ')

#10 
result='Hello World'.replace('World','There')

#11
result=course.split(' ')
result=result[2]
print(result)