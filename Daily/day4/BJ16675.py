hands = input().split()
MS = hands[:2]
TK = hands[2:4]

if 'R' in MS and 'R' in TK:
    if 'P' in MS and TK[0] == 'R' and TK[1] == 'R': # R P, R R
        winner = 'MS'
    elif 'P' in TK and MS[0] == 'R' and MS[1] == 'R':  # R R , R P
        winner = 'TK'
    else: # R S R S
        winner = '?'

if 'S' in MS and 'S' in TK:
    if 'R' in MS and TK[0] == 'S' and TK[1] == 'S': # S R S S
        winner = 'MS'
    elif 'R' in TK and MS[0] == 'S' and MS[1] == 'S': # S S S R
        winner = 'TK'
    else:
        winner = '?'

if 'P' in MS and 'P' in TK:
    if 'S' in MS and TK[0] == 'P' and TK[1] == 'P':
        winner = 'MS'
    elif 'S' in TK and MS[0] == 'P' and MS[1] == 'P':
        winner = 'TK'
    else:
        winner = '?'
if 'S' in MS and TK[0] == 'P' and TK[1] == 'P':
    winner = 'MS'
if 'P' in MS and TK[0] == 'R' and TK[1] == 'R':
    winner = 'MS'
if 'R' in MS and TK[0] == 'S' and TK[1] == 'S':
    winner = 'MS'

if 'S' in TK and MS[0] == 'P' and MS[1] == 'P':
    winner = 'TK'
if 'P' in TK and MS[0] == 'R' and MS[1] == 'R':
    winner = 'TK'
if 'R' in TK and MS[0] == 'S' and MS[1] == 'S':
    winner = 'TK'

print(winner)

