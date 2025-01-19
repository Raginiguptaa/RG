name=input("what is your name?:").strip()
print(name)
age=input("what is your age?:").strip()
print(age)
city=input("which city you live in?:").strip()
print(city)
love=input("what you love to do?:").strip()
print(love)
string="your name is {} and you are {} years old.You live in {} and you love {}"
output=string.format(name,age,city,love)
print(output)
email=input("what is your email address?:").strip()
user=email[:email.index("@")]
domain=email[email.index("@")+1:]
output1="your username is {} and your domain name is {}".format(user,domain)
print(output1)






