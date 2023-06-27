# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

steps = {}

def join(move):
  return "".join(move)

def player(prev_play, opponent_history=[]):
  if(prev_play != ""):
      opponent_history.append(prev_play)
  n = 4
  guess = "R"
  if(len(opponent_history) > n):
    pattern = join(opponent_history[-n:])
    steps[join(opponent_history[-(n+1):])] = steps.get(join(opponent_history[-(n+1):]), 0) + 1

    next = [pattern + "R", pattern + "S", pattern + "P"]
    for i in next:
      if(i not in steps.keys()):
        steps[i] = 0

    predict = max(next, key = lambda key: steps[key])

    if(predict[-1] == "P"):
      guess = "S"
    elif(predict[-1] == "R"):
      guess = "P"
    else:
      guess = "R"

  return guess