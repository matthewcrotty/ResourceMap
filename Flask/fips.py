import os

cur_path = os.path.dirname(__file__)

new_path = os.path.relpath('../fipsResources/state_to_code.txt', cur_path)

state_codes = {}
with open(new_path, 'r') as f:
    for x in f:
        line = x.split(':')
        state_codes[line[0].strip()] = line[1].strip()[1:3]

new_path = os.path.relpath('../fipsResources/national_county.txt', cur_path)

county_codes = {}
with open(new_path, 'r') as f:
    cur_State = "AL"
    temp_Dict = {}
    for x in f:
        line = x.split(',')
        if line[0] == cur_State:
            temp_Dict[line[3]] = line[2]
        else:
            county_codes[cur_State]=temp_Dict
            cur_State = line[0]
            temp_Dict = {}
            temp_Dict[line[3]] = line[2]


new_path = os.path.relpath('../fipsResources/state_to_abr.txt', cur_path)

abbreviations = {}
with open(new_path, 'r') as f:
    for x in f:
        line = x.replace('\"', "").split(',')
        abbreviations[line[0]] = line[1]

def getFIPSCodeState(state):
    try:
        code = state_codes[state]
        return code
    except KeyError:
        return False


def getFIPSCodeCounty(statea, county):
    try:
        print(statea, county)
        state = abbreviations[statea]
        print(state)
        print(county_codes[state])
        code = county_codes[state][county]
        return code
    except KeyError:
        return False
