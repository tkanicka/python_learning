def recursion_depth(x):
        print(x,end=","),(recursion_depth(x+1))
recursion_depth(1)


'''def rd(x=0):
    try:rd(x+1)
    except:print(x)     # s napovedou jsem si potom nasla jak funguje try a except a udelala to elegantneji
rd(0)'''


