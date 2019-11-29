'''
Reminder fields:
    - Title
    - Date
    - Time
    - Description
    - Roles that should be notified, if left blank will default to all
    - Notes (Optional)
'''

import discord
import json

client = discord.Client()

# define reminder object
class Reminder:
    def __init__(self, title=None, date=None, time=None, description=None, notes=None, roles="all"):
        self.title = title
        self.date = date
        self.time = time
        self.description = description
        self.notes = notes
        self.roles = roles

# converts object to json string
def convert(reminder):
    return json.dumps(reminder.__dict__)

# given a reminder object
# reads the renibder file, which should be an array
# append the object to the array
# convert the array to json string
# overwite save to file
def save(reminder):

    # get array from file
    savedReminders = read()

    # append to end of array
    savedReminders.append(reminder)

    with open("reminders.txt", "w") as file:
        json.dump(savedReminders, file)

def pred(m):
    return m.author == message.author and m.channel == message.channel

# reads the JSON file reminders.txt
# which contains an array of reminder objects
# should return an array
def read():
    try:
        with open("reminders.txt", "r") as file:
            jsonData = json.load(file)
    except json.decoder.JSONDecodeError:     # if the file is empty
        return []

    print(jsonData)
    return jsonData
