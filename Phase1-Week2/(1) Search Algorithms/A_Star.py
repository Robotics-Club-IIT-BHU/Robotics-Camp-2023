from pyamaze import maze,agent,COLOR,textLabel
from queue import PriorityQueue


def aStar(m,start):
    return searchPath,aPath,fwdPath



if __name__=='__main__':

    
# 10 , 15 is dimension of maze
    myMaze=maze(10,15)

# (6,4) is goal cell
    myMaze.CreateMaze(6,4,loopPercent=100)

#     uncomment this to show your path
# # (1,12) is start cell
#     searchPath,aPath,fwdPath=aStar(myMaze,(1,12))


#     a=agent(myMaze,1,12,footprints=True,color=COLOR.blue,filled=True)
#     b=agent(myMaze,6,4,footprints=True,color=COLOR.yellow,filled=True,goal=(1,12))
#     c=agent(myMaze,1,12,footprints=True,color=COLOR.red,goal=(6,4))
#     myMaze.tracePath({a:searchPath},delay=50)
#     myMaze.tracePath({b:aPath},delay=50)

#     myMaze.tracePath({c:fwdPath},delay=50)

#     l=textLabel(myMaze,'A Star Path Length',len(fwdPath)+1)
#     l=textLabel(myMaze,'A Star Search Length',len(searchPath))

    myMaze.run()