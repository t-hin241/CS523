import turtle
scr = turtle.Turtle()
scr.speed(1)


def visualize(root):
    def height(root):
        return 1 + max(height(root.left), height(root.right)) if root else -1
    
    def jumpto(x, y):
        scr.penup()
        scr.goto(x,y)
        scr.pendown()

    def draw(node, x, y, dx):
        if node:
            scr.goto(x,y)
            jumpto(x,y-20)
            scr.write(node.value, align='center',font=('Arial', 10, 'normal'))
            draw(node.left, x-dx, y-60, dx/2)
            jumpto(x, y-20)
            draw(node.right, x+dx, y-60, dx/2)


    h = height(root)
    jumpto(0, 30*h)
    draw(root, 0, 30*h, 40*h)
    scr.hideturtle()
    turtle.mainloop()
