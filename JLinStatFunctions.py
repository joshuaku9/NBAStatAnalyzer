def statsToFloat(statlist):
    '''Change the data from string to float'''
    for i in range(0, len(statlist)):
        statlist[i] = float(statlist[i])

def ms_to_s(minutesList):
    ''' Convert the time to data that can be plotted'''
    t = 0
    justMin = []
    for i in range(0,len(minutesList)):
        minutesList[i] = minutesList[i].split(":")
    for i in range(0, len(minutesList)):
        minutesList[i].pop(1)
    for i in range(0, len(minutesList)):
        justMin.append(minutesList[i][0])
    return justMin
