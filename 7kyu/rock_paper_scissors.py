def rps(p1, p2):
    if p1 == "scissors":
        if p2 == "scissors":
            return "Draw!"
        if p2 == "paper":
            return "Player 1 won!"
        if p2 == "rock":
            return "Player 2 won!"
    if p1 == "paper":
        if p2 == "paper":
            return "Draw!"
        if p2 == "scissors":
            return "Player 2 won!"
        if p2 == "rock":
            return "Player 1 won!"
    if p1 == "rock":
        if p2 == "rock":
            return "Draw!"
        if p2 == "scissors":
            return "Player 1 won!"
        if p2 == "paper":
            return "Player 2 won!"

def rps(p1, p2):
    beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    if beats[p1] == p2:
        return "Player 1 won!"
    if beats[p2] == p1:
        return "Player 2 won!"
    return "Draw!"