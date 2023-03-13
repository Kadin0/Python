# 3-1 姓名 将一些朋友存储在一个列表中，并将其命名为names。
# 依次访问该列表中的每个元素，从而将每个朋友的姓名打印出来

# names = ['李传雨','戴建国','颜昌宜','黄家旺','张晶晶']
# print(names[0])
# print(names[1])
# print(names[2])
# print(names[3])
# print(names[4])

# 3-2 问候语 继续使用练习3-1中的列表，但不打印每个朋友的姓名，而为每人打印一条消息。
# 每条消息都包括相同的问候语，但抬头为相应朋友的姓名
# message = f'Hello,My name is {names[0]},My father is Davis!'
# message1 = f'Hello,My name is {names[1]},My father is Davis!'
# message2 = f'Hello,My name is {names[2]},My father is Davis!'
# message3 = f'Hello,My name is {names[3]},My father is Davis!'
# message4 = f'Hello,My name is {names[4]},My father is Davis!'
# print(message)
# print(message1)
# print(message2)
# print(message3)
# print(message4)


# 3-3 自己的列表 想想你喜欢的通勤方式，如骑摩托车或开汽车，
# 并创建一个包含多种通勤方式的列表。根据该列表打印一系列有关这些通勤方式的宣言
# gohome = ['自行车','电动车','摩托车','高铁','prefer driving']
# message = f'I would like to own a Honda {gohome[4]}'
# print(message)

# message = f'I {gohome[4]} home to taking the bus as a way of commuting.'
# print(message)



# 3-4 嘉宾名单 如果你可以邀请任何人一起共进晚餐（无论是在世的还是故去的）,
# 你会邀请哪些人？请创建一个列表，其中至少包含三个你想邀请的人，然后使用这个列表打印消息
diner = ['mother','father','sister','girlfriend']
# message = f'could you me eat diner my {diner[1]}?'
# print(message)

# 3-5 修改嘉宾名单 得知有些嘉宾临时有事无法赴宴 需要把他们从名单中移除

# print(f'这位嘉宾有事无法赴宴{diner[3]}')
#
# diner[3] = 'cc'
# print(diner)
#
# print(f'你们可以在今晚来我共进晚餐吗？{diner[1]}')
#
# message = '我找到了更大的餐桌！'
# print(message)
#
# diner.insert(4,'gg')
# print(diner)
#
# diner.insert(0,'aa')
# print(diner)
#
# diner.append('yy')
# print(diner)
#
# message = "I'm sorry, my friend, the table I reserved cannot be delivered on time, " \
#           "so we have to cancel our gathering. I apologize! I'm sorry, " \
#           "my friend, the table I reserved cannot be delivered on time, " \
#           "so we have to cancel our gathering. I apologize!"
# print(message)


# 3-8 放眼世界 想出5个你渴望去旅游的地方
# 将这些地方存储在一个列表中，并确保其中的元素不是按字母顺序排序的
city = ['苏州','大理','普洱','重庆','西安']

# 按原始排列顺序打印该列表。不要考虑输出是否整洁的问题，只管打印原始python列表
print(city)

# 使用sorted()按字母顺序打印这个列表，同时不要修改它
print(sorted(city))

# 再次打印该列表，核实排列顺序未变
print(city)

# 使用sorted()按与字母顺序相反的顺序打印这个列表，同时不要修改它
print(city)
# 再次打印列表，核实排列顺序未变
print(city)

# 使用reverse()修改列表元素的排列顺序。打印该列表，核实已恢复到原来的排列顺序
city.reverse()
print(city)

# 使用sort()修改该列表，使其元素按字母顺序排序。打印该列表，核实排列顺序确实变了
city.sort()
print(city)

# 使用sort()修改该列表，使其元素按与字母顺序相反的顺序排列。打印该列表，核对排列顺序确实变了
city.sort(reverse = True)
print(city)















