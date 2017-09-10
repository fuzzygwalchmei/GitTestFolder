import tdl
import textwrap

#Screen Dimensions
SCREEN_WIDTH = 150;SCREEN_HEIGHT=100

#Dimensions for each Frame
MAP_WIDTH=100;MAP_HEIGHT=100
STAT_WIDTH=50;STAT_HEIGHT=50
ITEM_WIDTH=50;ITEM_HEIGHT=50

STAT_DATA={"Class":"Hero","Lvl":1,"HP":15}



root = tdl.init(SCREEN_WIDTH,SCREEN_HEIGHT,"Main Window",fullscreen=False)

ConMain = tdl.Console(MAP_WIDTH,MAP_HEIGHT)
ConStat = tdl.Console(STAT_WIDTH,STAT_HEIGHT)
ConItem = tdl.Console(ITEM_WIDTH,ITEM_HEIGHT)

msg_counter = 2
for each in STAT_DATA:
    text_line = each + ": " + str(STAT_DATA[each])
    ConStat.draw_str(5 ,msg_counter,text_line,bg=None,fg=(255,255,255))
    msg_counter +=1


ConMain.draw_frame(0 ,0 ,MAP_WIDTH,MAP_HEIGHT,None,bg=(255,0,0))
ConStat.draw_frame(0 ,0 ,STAT_WIDTH,STAT_HEIGHT ,None,bg=(20,255,0))
ConItem.draw_frame(0 ,0 ,ITEM_WIDTH ,ITEM_HEIGHT,None,bg=(0,0,255))

root.blit(ConMain,0 ,0,MAP_WIDTH,MAP_HEIGHT)
root.blit(ConStat,MAP_WIDTH ,0,STAT_WIDTH,STAT_HEIGHT)
root.blit(ConItem,MAP_WIDTH ,STAT_WIDTH ,STAT_WIDTH,STAT_HEIGHT)

while not tdl.event.is_window_closed():
    tdl.flush()
