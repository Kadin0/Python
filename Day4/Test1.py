# alien_0 = {'color': 'green','point': 10,'x_position': 0,'y_position': 25}
# print(alien_0['point'])
#
# new_point = alien_0['point']
# print(f'You just earned {new_point} points!')
#
#
# alien_0 = ['x_position']
# alien_0 = ['y_position']
# print(alien_0)
#
#
# alien_1 = {}
# alien_1['color'] = 'pink'
# alien_1['point'] = 100
#
# print(alien_1)
#
#
# alien_0 = {'x_position': 0,'y_position': 25,'speed': 'medium'}
# print(f"Original x_positon: {alien_0['x_position']}")

# 向左移动外星人
# 根据当前速度确定将外星人向右移动多远

# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     y_increment = 2
# else:
#     # 这个外星人的移动速度肯定很快
#     x_increment = 3
#
# # 新位置为旧位置加上移动距离
# alien_0['x_position'] = alien_0['x_position'] + x_increment
# print(f"New x_position: {alien_0['x_position']}")
#
#
# alien_0 = {'color': 'pink','point':10}
# print(alien_0)
#
# del alien_0['points']
# print(alien_0)


# person = {
#     'height': '180',
#     'weight': '130',
#     'color':'pink',
#     'point':'100',
#     'language':'python',
#     }
#
# print(person)
#
# language = person['color'].title()
# print(f'You like color is {language}.')



# alien_0 = {'color':'green','speed':'slow'}
#
# print_value = alien_0.get('point','No point value assigned')
# print(print_value)


# user_0 = {
#     'username': 'efermi',
#     'first': 'enrico',
#     'last': 'fermi',
# }
#
# for key,value in user_0.items():
#     print(f'\nkey:{key}')
#     print(f'value:{value}')


lanuages = {
    'jen': 'pyhton',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

# for name,lanuages in lanuages.items():
#     print(f"{name.title()}'sclanuages is {lanuages.title()}.")

# for name in lanuages.keys():
#     print(name.title())


# friends = ['phil','sarah']
# for name in lanuages.keys():
#     print(f"Hi {name.title()}.")

# if name in friends:
#     lanuages = lanuages[name].title()
#     print(f"\t{name.title()},I see you love {lanuages}.")

# if 'erin' not in lanuages.keys():
#     print("Erin,please take our poll!")

# for name in sorted(lanuages.keys()):
#     print(f"{name.title()},thank you for taking the poll.")

# print ("The following lanuages have been mentioned:")
# for lanuages in lanuages.values():
#     print(lanuages.title())

# print("The following lanuages have been mentioned:")
# for lanuages in set(lanuages.values()):
#     print(lanuages.title())

# waitlist = {'python','c++','java'}
# print(waitlist)

#创建一个空列表
aliens = []

# 创建30个外星人
for alien_number in range(30):
    new_alien = {'color':'green','points': 5,'speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] == 'yellow'
        alien['color'] == 'medium'
        alien['points'] == 10

# 显示前5个外星人
for alien in aliens[:5]:
    print(alien)
print("...")

# 显示创建了多少个外星人
print(f"Total number of aliens:{len(aliens)}")







