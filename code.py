# --------------
import json
from collections import Counter
with open(path) as f:
    data = json.load(f)

#print(data) 
 
# Code starts here

def get_deliveries_faced(player):
    cnt=0
    for i in data['innings']:
        for inning_name, innings in i.items():
            for j in innings['deliveries']:
                for delivery_name, delivery in j.items():
                    if delivery['batsman'] == player:
                        cnt+=1
    return cnt

def get_runs_scored(player):
    runs=0
    for i in data['innings']:
        for inning_name, innings in i.items():
            for j in innings['deliveries']:
                for delivery_name, delivery in j.items():
                    if delivery['batsman'] == player:
                        runs+=delivery['runs']['batsman']
    return runs

def get_batsmen(inning_name_filter):
    batsmen=[]
    for i in data['innings']:
        for inning_name, innings in i.items():
            if inning_name == inning_name_filter:
                for j in innings['deliveries']:
                    for delivery_name, delivery in j.items():
                        batsmen.append(delivery['batsman'])
    return set(batsmen)

def get_sixers(inning_name_filter):
    sixes=[]
    for i in data['innings']:
        for inning_name, innings in i.items():
            if inning_name == inning_name_filter:
                for j in innings['deliveries']:
                    for delivery_name, delivery in j.items():
                        if delivery['runs']['batsman'] == 6:
                            sixes.append(delivery['batsman'])
    return sixes

def get_bowled(inning_name_filter):
    batsmen=[]
    for i in data['innings']:
        for inning_name, innings in i.items():
            if inning_name == inning_name_filter:
                for j in innings['deliveries']:
                    for delivery_name, delivery in j.items():
                        if 'wicket' in delivery and delivery['wicket']['kind'] == 'bowled':
                            batsmen.append(delivery['batsman'])
    return batsmen


def get_extras(inning_name_filter):
    extras=0
    for i in data['innings']:
        for inning_name, innings in i.items():
            if inning_name == inning_name_filter:
                for j in innings['deliveries']:
                    for delivery_name, delivery in j.items():
                        extras+=delivery['runs']['extras']
    return extras

#  Can you find how many deliveries were faced by batsman  `SC Ganguly`.
print('How many deliveries were faced by batsman  `SC Ganguly`',get_deliveries_faced('SC Ganguly'))

#  Who was man of the match and how many runs did he scored ?
player_of_match = data['info']['player_of_match'][0]
print('man of the match',player_of_match)
print('how many runs did he scored',get_runs_scored(player_of_match))

#  List all batsmen played in the first inning?
print('List all batsmen played in the first inning',get_batsmen('1st innings'))

# Which batsman had the most no. of sixes in first inning ?
sixes = get_sixers('1st innings')
counter = Counter(sixes)
print('batsman and their sixes counts', counter)
print('batsman had the most no. of sixes in first inning', max(counter,key=counter.get))

# Find the names of all players that got bowled out in the second innings.
print('the names of all players that got bowled out in the second innings',get_bowled('2nd innings'))


# How many more "extras" (wides, legbyes, etc) were bowled in the second innings as compared to the first inning?
print('How many more "extras" (wides, legbyes, etc) were bowled in the second innings as compared to the first inning',abs(get_extras('1st innings')-get_extras('2nd innings')))


# Code ends here


