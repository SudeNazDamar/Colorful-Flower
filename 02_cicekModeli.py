import turtle as tr

sc = tr.Screen()

tr.setup(800,800)
sc.bgcolor("#262626")
tr.pencolor("#540d6e")
tr.speed(0)
tr.tracer(100)
tr.pensize(1)

colors = ("#a60590", "#fff66c", "#ff3480", "#aaff74")

for i in range(3):
    for n in range(400):
        tr.color(colors[n % 4])
        tr.circle(190 - n / 2,90)
        tr.left(90)
        tr.circle(190 - n / 2,90)
        tr.color(colors[n %  4])

    tr.left(30)

sc.exitonclick()