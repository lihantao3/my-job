dicts = {'abc': '2', 'def': '3', 'ghi': '4', 'jkl': '5', 'mno': '6', 'pqrs': '7', 'tuv': '8', 'wxyz': '9'}
word = input("输入单词\n").lower()
num = ''
for i in range(len(word)):
    for key, value in dicts.items():
        if word[i] in key:
            num = num + value
print(num)

