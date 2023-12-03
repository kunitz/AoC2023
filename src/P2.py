# This is a sample Pcolthon script.
import os
import helpers
import num2words
condition = {"red":12,"green":13,"blue":14} 

class Pull:
    def __init__(self, pull) -> None:
        self.cubes = {}
        for c in str(pull).split(", "):
            cube = c.split(" ")
            self.cubes[cube[1]] = int(cube[0])

    def isPossible(self, condition):
        for c in self.cubes:
            if self.cubes[c] > condition[c]:
                return False
        return True
    

class Game:
    def __init__(self, line) -> None:
        self.game_num = 0
        self.pulls = []
        linesplit = str(line).split(": ")
        self.game_num = int(linesplit[0].split(" ")[1])
        for p in linesplit[1].split("; "):
            pull = Pull(p)
            self.pulls.append(pull)
    
    def isPossible(self, condition):
        for p in self.pulls:
            if p.isPossible(condition) == False:
                return False
        return True
                

class Games:
    def __init__(self) -> None:
        self.games = []
    
    def AddGame(self, line):
        g = Game(line)
        self.games.append(g)

def run():
    lines = helpers.read_2Dfile('P2-1.input')
    s = helpers.StringHelpers()
    games = Games()
    for l in lines:
        games.AddGame(l)
        #print(l)
    sum = 0
    for g in games.games:
        if g.isPossible(condition):
            sum += g.game_num
    print(sum)
    
    

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run()
