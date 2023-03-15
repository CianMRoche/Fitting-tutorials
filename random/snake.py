import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from random import randint

# not quite working yet, some bugs, feel free to fix :)

# initialize the curses library
stdscr = curses.initscr()
curses.curs_set(0)

# set the dimensions of the screen
sh, sw = stdscr.getmaxyx()
w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)
w.timeout(100)

# initialize the snake
# initialize the snake
snake_x = int(sw/4)
snake_y = int(sh/2)
snake = [    [snake_y, snake_x],
    [snake_y, snake_x-1],
    [snake_y, snake_x-2]
]


# initialize the food
# initialize the food
food = [int(sh/2), int(sw/2)]
w.addch(food[0], food[1], '*')


key = KEY_RIGHT

while True:
    # check if the snake has collided with the wall or itself
    if (snake[0][0] in [0, sh] or snake[0][1] in [0, sw] or snake[0] in snake[1:]):
        curses.endwin()
        quit()

    # check if the snake has eaten the food
    if snake[0] == food:
        food = None
        while food is None:
            # create a new food item
            nf = [
                randint(1, sh-1),
                randint(1, sw-1)
            ]
            food = nf if nf not in snake else None
        w.addch(food[0], food[1], '*')
    else:
        # move the snake by popping the last element and inserting it at the front
        tail = [int(x) for x in snake.pop()]
        w.addch(tail[0], tail[1], ' ')


    # get the next key pressed by the user
    event = w.getch()
    key = key if event == -1 else event

    # ignore input that would cause the snake to move in the opposite direction
    if key == KEY_RIGHT and snake[0][1] < snake[1][1]:
        key = KEY_LEFT
    elif key == KEY_LEFT and snake[0][1] > snake[1][1]:
        key = KEY_RIGHT
    # elif key == KEY_DOWN and snake[0][0] > snake[1][0]:
    #     key = KEY_UP
    # elif key == KEY_UP and snake[0][0] < snake[1][0]:
    #     key = KEY_DOWN

    # move the snake in the appropriate direction
    if key == KEY_RIGHT:
        new_head = [snake[0][0], snake[0][1]+1]
    elif key == KEY_LEFT:
        new_head = [snake[0][0], snake[0][1]-1]
    elif key == KEY_UP:
        new_head = [snake[0][0]-1, snake[0][1]]
    elif key == KEY_DOWN:
        new_head = [snake[0][0]+1, snake[0][1]]

    snake.insert(0, new_head)
    w.addch(snake[0][0], snake[0][1], '#')