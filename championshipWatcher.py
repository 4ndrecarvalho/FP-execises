#__________________________________________________
# andre.dc@ua.pt                         30/11/2021
#__________________________________________________
def insertTeams():
    teams = []
    team = input("Insira as equipas, Para terminar a inserção prima <enter>\nInsira equipa: ")
    teams.append(team)
    while True:
        team = input("Insira equipa: ")
        if team == "":
            break
        teams.append(team)
    return teams
        
def allMatches(teams):
    matches = []
    for i in range(len(teams)):
        for j in range(len(teams)):
            if teams[i] != teams[j]:
                matches.append((teams[i], teams[j]))
    return matches

def win(dic, team, goals1, goals2):
    reg = dic.get(team)
    reg[0] += 1
    reg[3] += int(goals1)
    reg[4] += int(goals2)
    reg[5] += 3
    dic[team] = reg

def lose(dic, team, goals1, goals2):
    reg = dic.get(team)
    reg[2] += 1
    reg[3] += int(goals2)
    reg[4] += int(goals1)
    reg[5] += 0
    dic[team] = reg

def draw(dic, team, goals1, goals2):
    reg = dic.get(team)
    reg[1] += 1
    reg[3] += int(goals1)
    reg[4] += int(goals2)
    reg[5] += 1
    dic[team] = reg

def results(matches):
    matchResults = {}
    teamResults = {}
    for match in matches:
        print("Insert the result for match {}: ".format(match))
        goals1 = input("Goals of "+match[0]+":")
        goals2 = input("Goals of "+match[1]+":")
        matchResults[match] = (goals1, goals2)
        #[vitoria, empate, derrota, golos marcados, golos sofridos, pontos]
        teamResults.setdefault(match[0], [0,0,0,0,0,0])
        teamResults.setdefault(match[1], [0,0,0,0,0,0])
        if goals1 > goals2:
            win(teamResults, match[0], goals1, goals2)
            lose(teamResults, match[1], goals1, goals2)            
        elif goals1 < goals2:
            lose(teamResults, match[0], goals1, goals2)
            win(teamResults, match[1], goals1, goals2)
        else:
            draw(teamResults, match[0], goals1, goals2)
            draw(teamResults, match[1], goals1, goals2)
    return matchResults, teamResults

def printResults(teamresults):
    print("\n{:^10s} {:^10s} {:^10s} {:^10s} {:^15s} {:^15s} {:^10s}".format("Equipa", "vitorias", "empates", "derrotas", "golos marcados", "golos sofridos", "pontos"))
    for i, k in enumerate(sorted(teamresults.items(), key=lambda item: item[1], reverse=True)):
        if i == 0:
            champion = k[0]
        print("{:^10s} {:^10d} {:^10d} {:^10d} {:^15d} {:^15d} {:^10d}".format(k[0], k[1][0], k[1][1], k[1][2], k[1][3], k[1][4], k[1][5]))
    print("\n ________________________\n/ {:^22s} \ \n\ is the new champion!!! /\n  ----------------------\n   \ \n    \ \n        .--.\n       |o_o |\n       |:_/ |\n      //   \ \ \n     (|     | )\n    /'\_   _/`\ \n    \___)=(___/\n".format(champion))

def main():
    teams = insertTeams()
    matches = allMatches(teams)
    matchresults, teamresults = results(matches)
    printResults(teamresults)
    
if __name__ == "__main__":
    main()
