from django.template.defaultfilters import upper
x = 25
y = 10
name = "chuck hu"
age = upper(name) + "'s age is {}".format(48)
print(x, y, sep='\n')
print(upper(name))
print(age)

    
