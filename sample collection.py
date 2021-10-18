# create a sample collection

users = {'Hans': 'active', 'Eleanor': 'inactive'}

# strategy iterate over a copy

for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# strategy: create a new collecion


active_users = {}

for user, status in users.items():
    if status == 'active':
        active_users[user] = status



