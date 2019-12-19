import re
count=0
matcher=re.finditer('ab','abaababaababaaabbbbbbab')
for match in matcher:
    print(match)
    print("match available at ",match.start())
    print('group=',match.group())
    count+=1
print("count=",count)
x='[^abc]'
x='[a-b]'
x='[A-Z]'
x='[0-9]'
