from collections import OrderedDict
from random import randint
for i in range(5):
    print(randint(1, 10))
favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'
for name, language in favorite_languages.items():
    print(name + "'s favourite language is : " + language)
# print("Sarah's favorite language is " +
#       favorite_languages['sarah'].title() + ".")
# for name, language in favorite_languages.items():
#     print(name.title() + "'s favorite language is " + language.title() + ".")
# print(favorite_languages.keys())
# for name in favorite_languages:
#     print(name.title())
# friends = ['phil', 'sarah']
# for name in favorite_languages.keys():
#     print(name.title())
#     if name in friends:
#         print(" Hi " + name.title() + ", I see your favorite language is " +
#               favorite_languages[name].title() + "!")
# if 'erin' not in favorite_languages.keys():
#     print("'erin' pls take the poll")

# for name in sorted(favorite_languages.keys()):
#     print(name.title() + ", thank you for taking the poll.")
# for name, languages in favorite_languages.items():
#     print('\n'+name.title()+"'s favorite language are:")
#     for language in languages:
#         print('\t'+language.title())
