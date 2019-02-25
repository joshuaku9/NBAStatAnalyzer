def statsToFloat(statlist):
    for i in range(0, len(statlist)):
        statlist[i] = float(statlist[i])

def ms_to_s(minutesList):
    t = 0
    justMin = []
    for i in range(0,len(minutesList)):
        minutesList[i] = minutesList[i].split(":")
    for i in range(0, len(minutesList)):
        minutesList[i].pop(1)
    for i in range(0, len(minutesList)):
        justMin.append(minutesList[i][0])
    return justMin






# db = pandas.DataFrame({'game': [i for i in game],
#                        'date': [i for i in date],
#                        'age': [i for i in age],
#                        'team': [i for i in team],
#                        'at': [i for i in at],
#                        'opp': [i for i in opponent],
#                        'outcome': [i for i in outcome],
#                        'starting': [i for i in starting],
#                        'min': [i for i in minutes],
#                        'fg': [i for i in fieldGoal],
#                        'fga': [i for i in fieldGoalAtt],
#                        'fg%': [i for i in fieldGoalPercent],
#                        '3p': [i for i in threePoint],
#                        '3pa': [i for i in threePointAtt],
#                        '3p%': [i for i in threePointPercent],
#                        'ft': [i for i in freeThrow],
#                        'fta': [i for i in freeThrowAttempt],
#                        'ft%': [i for i in freeThrowPercent],
#                        'oreb': [i for i in oRebound],
#                        'dreb': [i for i in dRebound],
#                        'totreb': [i for i in totRebound],
#                        'ass': [i for i in assist],
#                        'stl': [i for i in steal],
#                        'blk': [i for i in block],
#                        'tov': [i for i in turnover],
#                        'fouls': [i for i in fouls],
#                        'pts': [i for i in points],
#                        'score': [i for i in score],
#                        'plusMinus': [i for i in plusMinus]
#                        }
#                      )
