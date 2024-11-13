domain_color = ['red','green','blue']
variable_state = ['wa','nt','sa','q','nsw','v','t']
neighbors = {
    'wa' : ['nt','sa'],
    'nt' : ['wa','sa','q'],
    'sa':['wa','nt','q','nsw','v'],
    'q' :['nt','sa','snw'],
    'nsw':['q','sa','t'],
    'v': ['sa','t'],
    't':[],
}
finalstateswithcolor = {}
def getthecolor(state):
    for color in domain_color :
        if assigncolor(state, color):
            return color
    return None
def assigncolor(state, color):
    for i in neighbors.get(state, []):  
        color_of_neighbor = finalstateswithcolor.get(i)
        if color_of_neighbor == color:
            return False
    return True

def main():
    sorted_states = sorted(neighbors.keys(), key=lambda state: len(neighbors[state]), reverse=True)
    for state in sorted_states:
        finalstateswithcolor[state] = getthecolor(state)
    print("The states with colors are", finalstateswithcolor)
main()