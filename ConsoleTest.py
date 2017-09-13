import tdl
import textwrap
import ConsoleConstants
import ConsoleClasses
import DrawScreen

while not tdl.event.is_window_closed():
    DrawScreen.Draw_Now()
    tdl.flush()
