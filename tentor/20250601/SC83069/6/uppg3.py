series = {
    '2025-05-12': {'winner': 'Buslätt SK', 'loser': 'Normlösa BK'},
    '2025-05-13': {'loser': 'Rambo AIS', 'winner': 'Köttkulla SBK'},
    '2025-05-14': {'loser': 'Normlösa BK', 'winner': 'Aplungsåsen BOIS'},
    '2025-05-15': {'loser': 'Köttkulla SBK', 'winner': 'Buslätt SK'},
    '2025-05-16': {'winner': 'Aplungsåsen BOIS', 'loser': 'Rambo AIS'}
}

def get_wins_by(team, matches):
    wins = []
    for date, result in matches.items():
        if result["winner"] == team:
            wins.append(date)
    return wins
