users = {
    'aeinstein': {
        'first': 'albert',
        'second': 'einstein',
        'location': 'princeton'
    },
    'mcurie': {
        'first': 'marie',
        'second': 'curie',
        'location': 'paris'
    }
}

for user, info in users.items():
    print("\nUsername:"+user)
    fullname = info['first'] + info['second']
    location = info['location']

    print("\tFull Name:" + fullname.title())
    print("\tlocation:" + location.title())
