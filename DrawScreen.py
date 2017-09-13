import tdl
from ConsoleConstants import *
import ConsoleClasses

root = tdl.init(SCREEN_WIDTH,SCREEN_HEIGHT,"Main Window",fullscreen=False)

ConMain = tdl.Console(MAP_WIDTH,MAP_HEIGHT)
ConStat = tdl.Console(STAT_WIDTH,STAT_HEIGHT)
ConItem = tdl.Console(ITEM_WIDTH,ITEM_HEIGHT)

myHero = ConsoleClasses.myObjects()

def Draw_Now():
    global STAT_DATA
    msg_counter = 2

    myList = ("Class","level","hitPoints")
    for each in myList:
        valueLine = "myHero."+each
        text_line = valueLine
        ConStat.draw_str(5 ,msg_counter,text_line,bg=None,fg=(255,255,255))
        msg_counter +=1


    ConMain.draw_frame(0 ,0 ,MAP_WIDTH,MAP_HEIGHT,None,bg=(255,0,0))
    ConStat.draw_frame(0 ,0 ,STAT_WIDTH,STAT_HEIGHT ,None,bg=(20,255,0))
    ConItem.draw_frame(0 ,0 ,ITEM_WIDTH ,ITEM_HEIGHT,None,bg=(0,0,255))

    root.blit(ConMain,0 ,0,MAP_WIDTH,MAP_HEIGHT)
    root.blit(ConStat,MAP_WIDTH ,0,STAT_WIDTH,STAT_HEIGHT)
    root.blit(ConItem,MAP_WIDTH ,STAT_WIDTH ,STAT_WIDTH,STAT_HEIGHT)
