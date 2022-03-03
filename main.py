import turtle
import pandas

s = turtle.Screen()
s.screensize(600, 600)
s.title("India's State Game")
image = "map3.gif"
s.addshape(image)
s.bgpic(image)

data = pandas.read_csv("states.csv")
all_states = data.states.to_list()
answered_states = []

i = 0
while i <= len(all_states):

    answer = turtle.textinput(title=f'{i}/{len(all_states)}', prompt="Enter the name of state").title()
    if answer in all_states:
        answered_states.append(answer)
        s = data[data.states == answer]
        turtle.hideturtle()
        turtle.penup()
        turtle.goto(int(s.x), int(s.y))
        turtle.write(answer)

    if answer == "Exit":
        break
    i += 1

learn = [state for state in all_states+answered_states if state not in all_states or state not in answered_states]
to_learn = pandas.DataFrame(learn)
to_learn.to_csv("states_to_learn.csv")


#--------------------Normal file write but does not support list-----------------------------------
# with open("states_to_learn.csv", mode='w') as doc:
#     doc.write(learn)
#--------------------used this for co-ordinates of each state---------------------------------------
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#-----------------------------------------------------------
#turtle.mainloop()
