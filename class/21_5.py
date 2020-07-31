import turtle as t

vertext, length = map(int, input().split())
angle = int(360 / vertext)

t.shape("turtle")

for i in range(vertext):
    t.forward(length)
    t.right(angle * 2)
    t.forward(length)
    t.left(angle)
