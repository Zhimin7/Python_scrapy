import re


content = 'Hello 123456 World_This is a Regex Demo'
print(len(content))
result = re.match('^Hello\s(\d+)\sWorld', content)
print(result)
print(type(result))
print(result.group())
print(result.group(1))
print(result.span())