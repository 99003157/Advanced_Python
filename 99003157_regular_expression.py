import re
string = """dimanthj@gmail.com"""
search = re.search('[a-zA-Z0-9]+@[a-z]+.[a-z]+', string)
print(search)
