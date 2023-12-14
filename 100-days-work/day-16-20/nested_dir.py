names = ['关羽', '张飞', '赵云', '马超', '黄忠']
courses = ['语文', '数学', '英语']
# 录入五个学生三门课程的成绩
# 错误 - 参考http://pythontutor.com/visualize.html#mode=edit
# scores = [[None] * len(courses)] * len(names)

score_dict = dict()
scores = [[None] * len(courses) for _ in range(len(names))]
for name in names:
    inner_dict = dict()
    for course in courses:
        inner_dict[course] = None
    score_dict[name] = inner_dict

print(score_dict)

scores = [[None] * len(courses) for _ in range(len(names))]
for row, name in enumerate(names):
    for col, course in enumerate(courses):
        scores[row][col] = float(input(f'请输入{name}的{course}成绩: '))
        print(scores)
