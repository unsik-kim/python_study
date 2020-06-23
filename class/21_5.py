import turtle as t
import time


t.shape('turtle')

vertext, length = map(int, input().split())
angle = int(360/vertext)



for i in range(vertext) :
    t.forward(length)
    t.right(angle*2)
    t.forward(length)
    t.left(angle)

time.sleep(10)