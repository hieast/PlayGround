#"Stopwatch: The Game"
import simplegui
# define global variables
width = 300
hight = 200
font_size = 48

seconds = 0
success = 0
stoped = 0
running = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    if t >= 6000:
        return "Boommmmmm!"
    d = t%10
    remains = t//10
    bc = remains%60
    a = remains//60
    if bc < 10:
        string = string = str(a) + ":0" + str(bc) + "." + str(d)
    else:
        string = str(a) + ":" + str(bc) + "." + str(d)
    return string 
# define event handlers for buttons; "Start", "Stop", "Reset"

def start():
    global running
    running = True
    timer.start()

def stop():
    global running, success, stoped
    if running:
        success += (seconds%10) == 0
        stoped += 1
    running = False
    timer.stop()

def reset():
    global seconds, running, success, stoped
    seconds = 0
    success = 0
    stoped = 0
    if running:
        running = False
        timer.stop()
    
    
# define event handler for timer with 0.1 sec interval
def tick():
    global seconds
    seconds += 1

# define draw handler
def draw(canvas):
    canvas.draw_text(format(seconds), 
                     [0.5 * width - 1.5 * font_size, 0.5 * (hight + font_size)], 
                     font_size, "White")
    canvas.draw_text( str(success) + "/" + str(stoped), 
                     [width - font_size, 0.75 * font_size], 
                     font_size/2, "Red")

    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game", width, hight)


# register event handlers
frame.add_button("Start", start, 200)
frame.add_button("Stop", stop, 200)
frame.add_button("Reset", reset, 200)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100,tick)


# start frame
frame.start()

# Please remember to review the grading rubric
