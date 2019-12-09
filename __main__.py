from GameMaster import *
from PlayerAI import *

if __name__ == "__main__":
    scoreList: List[int] = []
    iteration: int = 1000

    for i in range(iteration):
        gameMaster = GameMaster(playersNum=4, playerAI=AlwaysPlaysFirstCard())
        print(f" ===== ===== iteration {i} start ===== =====")
        scoreList.append(gameMaster.start())
        print(f" ===== ===== iteration {i} end   ===== =====")

    # print(scoreList)
    averageScore: float = sum(scoreList) / iteration
    print(f'average score is: {averageScore}')
