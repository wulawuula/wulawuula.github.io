import time
import curses 
from random import Random
import a_star

textChord = {
    'wall':'墙',
    'player':'＠',
    'bean':'·',
    'monster':'M'
}

_maps = [
    [
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,1],
        [1,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,1],
        [1,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,1],
        [1,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,1],
        [1,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,1],
        [1,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,1],
        [1,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,1],
        [1,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,1],
        [1,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,2,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1],
        [1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1],
        [1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1],
        [1,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1],
        [1,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    ],
    [
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,1,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1,1,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,2,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1],
        [1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    ]
]



class Player(object):#玩家
    def __init__(self,_location) :
        self.score = 0
        self.location = _location
        self.direction=''
    
class Bean(object):#豆子初始位置
    def __init__(self,location):
        self.location=location

    def randomBean(x,y):
        _x=Random().randint(0,x)#实例化的时候会获取系统时间，才能产生伪随机数
        _y=Random().randint(0,y)
        return Bean([_x,_y])


class Monster(object):
    def __init__(self,location):
        self.location=location
    def monster_location(x,y):
        _x=Random().randint(0,x)
        _y=Random().randint(0,y)
        return Monster([_x,_y])



class Interface(object):#界面
    def _print(stdscr,beans,player,level,monsters):#打印地图，显示玩家位置

        for lines in range(len(_maps[level])):#line是行，纵坐标
            for rows in range(len(_maps[level][lines])):
                if _maps[level][lines][rows] == 1:
                    stdscr.addstr(lines, 2*rows,textChord['wall'])#纵坐标，横坐标，输出墙
                else:
                    stdscr.addstr(lines, 2*rows,'  ')#空格是有的
        
        stdscr.addstr(player.location[1],2 * player.location[0],textChord['player'])#玩家位置输出@
        for i in beans:
            stdscr.addstr(i.location[1],2 * i.location[0],textChord['bean'])#豆子位置输出点点
        for n in monsters:
            stdscr.addstr(n.location[1],2*n.location[0],textChord['monster'])#怪物位置输出M
        stdscr.refresh()#立即刷新显示界面

    def clear(stdscr):
        stdscr.clear()#stdscr内部的clear是将所有的输出换成空格符
        stdscr.move(0,0)#将光标移至（0，0）

def loop(stdscr,player:Player,level):#游戏主循环
    beans:list[Bean]=[]#把豆子坐标放进列表，，类型声明，看起来方便
    monsters:list[Monster]=[]#生成怪物
    router = a_star.AStar(_maps[level], (0,0), (0,0))

    def beans_spawn(player:Player):#结豆子
        while (len(beans) < 7):
            _bean = Bean.randomBean(len(_maps[level][0]) -1,len(_maps[level])-1)
            if _bean in beans:
                continue
            if _maps[level][_bean.location[1]][_bean.location[0]] == 1:
                continue
            if _bean.location == player.location:
                continue
            if _bean.location in [a.location for a in monsters]:
                continue
            beans.append(_bean)
    beans_spawn(player)
  
    def monsters_spawn(player:Player):#怪物生成
        while (len(monsters)<3):
            _monster=Monster.monster_location(len(_maps[level][0]) -2,len(_maps[level]) -2 )
            if _monster in monsters:
                continue
            if _maps[level][_monster.location[1]][_monster.location[0]]==1:
                continue
            if (player.location[0]-2<=_monster.location[0]<=player.location[0]+2
                 and player.location[1]-2<=_monster.location[1]<=player.location[1]+2):
                continue
            if _monster.location in [i.location for i in beans]:
                continue
            monsters.append(_monster)

    def monsters_move():#通过改变概率使怪物一定程度上能够追踪玩家
        for i in range(len(monsters)):
            router.start = a_star.findWayPoint(router.points, monsters[i].location[0], monsters[i].location[1])
            router.setend(player.location[0], player.location[1])
            line = [[j.x,j.y] for j in router.yieldPath()]
            monsters[i].location = line[1] if len(line) >= 2 else monsters[i].location

            
    monsters_spawn(player)
    
    while True:#玩家方向控制
        lasttime = time.time()
        c = -1
        while (time.time() - lasttime < 0.3):
            _c  = stdscr.getch()#立即获取输入，返回值为int类型
            if (_c != -1):#有输入是返回的是ASCII编码值，无输入则是-1
                c = _c
        
        if c!=-1:
            
            if c==curses.KEY_UP:#curese中的KEY开头的字符都对应一个ASCII值
                player.direction='w'
            elif c==curses.KEY_DOWN:
                player.direction='s'
            elif c==curses.KEY_LEFT:
                player.direction='a'
            elif c==curses.KEY_RIGHT:
                player.direction='d'
            elif c==32:
                flag = False
                while True:
                    c = stdscr.getch()
                    if (c == 27):
                        flag = True
                        break
                    elif (c == -1):
                        time.sleep(0.001)
                    else:break
                if (flag):break
            elif c== 27: # Escape
                break
            else:
                ...

        if player.direction=='':
            ...
        elif player.direction=='w':
            player.location[1] -= 1
        elif player.direction=='s':
            player.location[1]+=1
        elif player.direction=='a':
            player.location[0]-=1
        else :
            player.location[0]+=1
            
        if player.location in [i.location for i in beans]:#把豆子坐标抽出来做成列表，单行for语句
            player.score+=1
            for i in beans:
                if i.location == player.location:
                    beans.remove(i)
            beans_spawn(player)#吃掉豆子，再结一个

        monsters_move()

        if _maps[level][player.location[1]][player.location[0]] == 1:
            break

        if player.location in [m.location for m in monsters]:
            break

        for m in monsters:
            if _maps[level][m.location[1]][m.location[0]]==1:
                monsters.remove(m)
                monsters_spawn(player)
        
        Interface.clear(stdscr)#删掉上一帧
        Interface._print(stdscr,beans,player,level,monsters)#输出下一帧

def main(stdscr):           #stdscr不需要用户传入实参，调用函数时模块直接赋予初值
    stdscr.nodelay(True)    #防止玩家没有输入时卡在getch（）函数（True不等，False等）
    curses.noecho()         #不显示用户输入的东西
    curses.curs_set(False)  #隐藏光标（True显示，False隐藏）     
    stdscr.keypad(True)     #允许非字符输入


    stdscr.addstr('按 任 意 键 开 始 游 戏')#在光标处输出
    stdscr.refresh()        #加了才能打印上面的
    while (stdscr.getch() == -1):...
    
    while True:
        _time = time.time()
        stdscr.clear()
        stdscr.refresh()
        stdscr.addstr(0,0,"请 输 入 关 卡 [%d~%d],Esc退 出 :" % (0,len(_maps) - 1))
        while True:
            _level = stdscr.getch()
            if _level != -1 and (_level==27 or _level in [i + 48 for i in range(len(_maps))]):
                break
        
        if _level == 27: # Esc
            break
        elif 48 <= _level <= 49:#0到9关，虽然没有这么多关
            _level -= 48
        
        for item in _maps[_level]:
            if 2 in item:
                init_location=[item.index(2),_maps[_level].index(item)]#玩家初始位置，横坐标和纵坐标

        player=Player(init_location)
        loop(stdscr,player,_level)

        stdscr.clear()
        stdscr.refresh()

        stdscr.addstr(0,0,"你 当 前 的 分 数 是:%d" % player.score)
        stdscr.addstr(1,0,"你 的 游 戏 时 间 是:%ss" % str(time.time()-_time))
        stdscr.addstr(2,0,"按 任 意 键 继 续:")

        while (stdscr.getch() == -1):...

stdscr = curses.initscr()#把控制台上之前的东西全都弄掉，创建一个新的界面
main(stdscr)
