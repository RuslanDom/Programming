# count = {}
#
# count['city'] = {1: 'boston', 2: 'mexico'}
# print(count['city'])
# count['city'].upload({3: 'moskow'})
# print(count['city'])

message = ''
while message != 'стоп':
    message = input('Введи страну: ')
    text_my = lambda x: x.capitalize() if x != 'сша' and x != 'США' else x.upper()
    print(text_my(message))
