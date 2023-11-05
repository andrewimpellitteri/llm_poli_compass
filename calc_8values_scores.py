import json
import math

def calc_score_max(score,max):
        return round((100*(max+score)/(2*max)),1)

def calc_scores(econ_arr, dipl_arr, govt_arr, scty_arr):
    with open("8values_test/8values.github.io/questions.js") as f:
        questions = f.read()

    questions = json.loads(questions)

    max_econ = max_dipl = max_govt = max_scty = 0

    for question in questions:
        max_econ += math.abs(question['effect']['econ'])
        max_dipl += math.abs(question['effect']['dipl'])
        max_govt += math.abs(question['effect']['govt'])
        max_scty += math.abs(question['effect']['scty'])


    final_econ = calc_score_max(sum(econ_arr),max_econ)

    final_dipl = calc_score_max(sum(dipl_arr),max_dipl)

    final_govt = calc_score_max(sum(govt_arr),max_govt)

    final_scty = calc_score_max(sum(scty_arr),max_scty)

    return [final_econ, final_dipl, final_govt, final_scty]

    