import json
import math

with open("8values_test/8values.github.io/questions.js") as f:
    questions = f.read()

questions = json.loads(questions)

max_econ = max_dipl = max_govt = max_scty = 0
# read in econ_array, dipl_array, govt_array, scty_array from file

for question in questions:
    max_econ += math.abs(question['effect']['econ'])
    max_dipl += math.abs(question['effect']['dipl'])
    max_govt += math.abs(question['effect']['govt'])
    max_scty += math.abs(question['effect']['scty'])

def calc_score(score,max):
    return round((100*(max+score)/(2*max)),1)

final_econ = calc_score(sum(econ_arry),max_econ)

final_econ = calc_score(sum(dipl_array),max_dipl)

final_econ = calc_score(sum(govt_array),max_govt)

final_econ = calc_score(sum(scty_array),max_scty)

    