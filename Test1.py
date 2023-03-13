# home = ['son','father','mathor','sister']
# print(home[0])
#
# home[0] = 'bro'
# print(home[0])
#
# home.append('grandson')
# print(home)
#
# home.append('111')
# print(home)
#
# home.insert(0,'cc')
# print(home)
#
# del home[0]
# print(home)
#
#
# del home[0]
# print(home)
#
# pop_home = home.pop()
# print(home)
# print(pop_home)
#
# pop_home = home.pop(3)
# print(pop_home)
# print(f'This is my {pop_home()}')

# cars = ['bmw','audi','toyota','subaru']
# cars.sort(reverse = True)
# print(cars)
#
# print("Here is the original list:")
# print(cars)
#
# print("\nHere is the sorted list:")
# print(sorted(cars))
#
# print("\nHere is the sorted list")
# print(cars)

# car = ['bmw','audi','toyota','subaru']
# print(len(car))

# magicians = ['alice','david','ross','carlina']
# for magician in magicians:
#     print(f'{magician.title()},that was a great trick!')
#     print(f"I can't wait to see your next trick,{magician.title()}.\n")
# print("Thank you,eveyone.That was a great magic show!")

# pizzes = ['beef','chicken','durian','eel']
# for pizze in pizzes:
#     print(pizze)
#
# for value in range(6):
#     print(value)
#
# num = list(range(1,6))
# print(num)
#
# even_num = list(range(2,11,2))
# print(even_num)

# sum_num = [1,2,3,4,56,7,8,9]
# print(min(sum_num))
# print(max(sum_num))
# print(sum(sum_num))

# player = ['diavs','john','job','eil','micheel']
# print(player[:-2])
#
# print("Here are the first three player on my team:")
# for player in player[:3]:
#     print(player.title())

food = ['fish','beef','ice-cream','noddles','jiaozi','duck']
herfood = food

# print('My favorite food are:')
# print(food)
# print('My favorite foods are:')
# print(herfood)

# food.append('cannoli')
# herfood.append('mutton')
#
# print(food)
# print(herfood)

# dim = (200,50)
# print(dim[0])
# print(dim[1])

# string = 'hellepython'
# print(string[7:2:-1])


# if语句
# cars = ['audi','bieke','bmw','jeep','tessl']
# for car in cars:
#     if car == 'jeep':
#         print(car.upper())
#     else:
#         print(car.title())

# car = 'jeep'
# car == 'teasal'
# print(car)


# food = 'mushrooms'
# if food != 'anchovies':
#     print('Hold the anchovies!')
#
#
# a = 'jeep'
# print(a == 'teasl')
#
#
# b = ['ab,ac,bb,bc,cc']
# print('dd' in a)

#
# users = ['davi','wiggins','james','kobe']
# user = 'bob'
# if user not in users:
#     print(f'{user.title()},you can post a respond if you wish.')
#
#
# age = 19
# if age >= 18:
#     print('You are old enough to vote!')


# p_foods = ['mushrooms','green peppers','extra cheese']
#
# for p_food in p_foods:
#     if p_food == 'green peppers':
#         print('sorry,we are out of green peppers right now.')
#     else:
#         print(f'Adding {p_food}.')
#
# print('\nFinished making your pizzed!')


# toppings = []
#
# if toppings:
#     for toppin in toppings:
#         print(f'Adding {topping}.')
#     print("\nFinished making your pizzar!")
# else:
#     print("Are you sure you want a plain pizza? ")


exit_foods = ['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']

choose = ['mushrooms','french fries','extra cheese']

for choose in choose:
    if choose in exit_foods:
        print(f'Adding {choose}.')
    else:
        print(f"Sorry,we don't have {choose}.")
print("\nFinish making your pizza!")

















