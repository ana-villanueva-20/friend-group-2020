"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

import json

group = {
    "Jill": {
        "age": 26,
        "job": "biologist",
        "relations": {
            "Zalika": "friend",
            "John": "partner"
        }
    },
    "Zalika": {
        "age": 28,
        "job": "artist",
        "relations": {
            "Jill": "friend"
        }
    },
    "John": {
        "age": 27,
        "job": "writer",
        "relations": {
            "Jill": "partner"
        }
    },
    "Nash": {
        "age": 34,
        "job": "chef",
        "relations": {
            "John": "cousin",
            "Zalika": "landlord"
        }
    }
}

max_age = max(person['age'] for name, person in group.items())
print(max_age)
avg_rels = statistics.mean(len(person['relations']) for name, person in group.items())
print(avg_rels)
max_age_1_rel = max(person['age'] for name, person in group.items() if len(person['relations']) > 0)
print(max_age_1_rel)
max_age_1_friend = max(person['age'] for name, person in group.items() if 'friend' in person['relations'].values())
print(max_age_1_friend)

with open('my_group.json', 'w') as f:
    json.dump(group, f, indent=4)


with open('my_group.json', 'r') as json_file:
    my_group = json_file.read()


print(my_group)