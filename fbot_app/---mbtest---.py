# class BankEMP:

#     def __init__(self, name, dept, age):
#         self.name = name
#         self.dept = dept
#         self.age = age

#     def __repr__(self):
#         return '{' + self.name + ', ' + self.dept + ', ' + str(self.age) + '}'

# if __name__ == '__main__':

#     emps = [
#         BankEMP('Elijah', 'IT', 20),
#         BankEMP('Nik', 'Banking', 21),
#         BankEMP('Lucien', 'Finance', 19)
#     ]

emps = [{'name': 'Elijah', 'dept': 'IT', 'age': 20}, {'name':'Nik', 'dept': 'Banking', 'age':21}, {'name':'Lucien', 'dept': 'Finance', 'age':19}]
print(emps)

# sort list by `name` in the natural order
# emps.sort(key=lambda x: x.name)
# print(emps)

# sort list by `name` in reverse order
emps.sort(key=lambda x: x['age'], reverse=False)
print(emps)


#  class Alligator:
#     def __init__(self,color, length, mood, age):
#         self.color= color
#         self.length= length
#         self.mood= mood
#         self.age= age


#     def __repr__(self):
#             return '({}, {}, {}, {})'.format(self.color, self.length, self.mood, self.age)


# Alligator1= Alligator("green", 20, "ferocious", 10)
# Alligator2= Alligator("dark green", 15, "calm", 2)
# Alligator3= Alligator("black", 45, "angry", 15)

# alligators= [Alligator1, Alligator2, Alligator3]

# print(alligators)
# print('----------------------------')

# def sortalligators_color(allig):
#     return allig.color

# def sortalligators_length(allig):
#     return allig.length

# def sortalligators_mood(allig):
#     return allig.mood

# def sortalligators_age(allig):
#     return allig.age


# # sorted_alligators_color= sorted(alligators, key= sortalligators_color)
# # sorted_alligators_length= sorted(alligators, key= sortalligators_length)
# # sorted_alligators_mood= sorted(alligators, key= sortalligators_mood)
# # sorted_alligators_age= sorted(alligators, key= sortalligators_age)

# # print(alligators)

# # print("Object sorted by color:", sorted_alligators_color)
# # print("Objects sorted by length:", sorted_alligators_length)
# # print("Objects sorted by mood:", sorted_alligators_mood)
# # print("Objects sorted by age:", sorted_alligators_age)
