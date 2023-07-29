from manim import *
import numpy as np
import random

CWHITE = "#fdfcdc"
CBLUE = "#008aab"
CBLUE2 = "#00afb9"
CRED = "#f07167"
CGREEN = "#49de64"
CBLACK = "#171d23"

FONT_R = "JetBrainsMono Nerd Font"

def Panel(obj, color=CWHITE, corner=0.2):
    return SurroundingRectangle(obj, color=color, buff=0.2, corner_radius=corner)

def setup(self):
        self.camera.background_color = "#171d23"

def create_nn(layer, r=0.2, vs = 1, hs = 0.7, line_color=CBLUE, dot_color=CWHITE, line_opacity=0.4):

    d = VGroup()

    for i in layer:
        temp_g = VGroup()
        for j in range(i):

            c = Circle(
                    radius = r,
                    color=dot_color,
                    fill_opacity=1,
                    )

            temp_g.add(c)

        temp_g.arrange(buff=vs, direction=[0., 1., 0.])
        d.add(temp_g)
    d.arrange(buff=hs)

    l = VGroup()
    for I in range(len(layer)-1):
        for i in range(len(d[I])-1, -1, -1):
            for j in range(len(d[I+1])-1, -1, -1):
                l.add(Line(d[I][i], d[I+1][j], color=line_color,stroke_opacity=line_opacity)) 

    return (d,l)

class ANN(Scene):
    def construct(self):
        setup(self)

        dup_speed = 0.5

        (d, l) = create_nn([2])
        self.play(Create(d))
        self.wait(1)

        (d2, l2) = create_nn([2, 3])
        self.play(Transform(d, d2, run_time=dup_speed))

        (d3, l3) = create_nn([2, 3, 3])
        self.play(Transform(d, d3, run_time=dup_speed))

        (d4, l4) = create_nn([2, 3, 3, 2])
        self.play(Transform(d, d4, run_time=dup_speed))

        (d5, l5) = create_nn([2, 3, 3, 3, 2])
        self.play(Transform(d, d5, run_time=dup_speed))

        self.wait(3)

        self.play(Create(l5, run_time=2))

        self.wait(5)

class ANN2(Scene):
    def construct(self):
        setup(self)

        (d5, l5) = create_nn([2, 3, 3, 3, 2])
        self.add(d5)
        self.add(l5)

        self.play(l5.animate.set_color(CWHITE), run_time=0.5)
        self.play(l5.animate.set_color(CBLUE2), run_time=0.5)
        self.wait(3)

class ANN3(Scene):
    def construct(self):
        setup(self)

        (d5, l5) = create_nn([2, 3, 3, 3, 2])
        self.add(d5)
        self.add(l5)

        self.wait(2)

        c1 = Panel(d5[0], CBLUE)
        c2 = Panel(VGroup(d5[1], d5[2], d5[3]), CWHITE)
        c3 = Panel(d5[4], CRED)

        t1 = Text("Input", font=FONT_R, font_size=30, color=CBLUE).next_to(c1, LEFT)
        t2 = Text("Hidden", font=FONT_R, font_size=30, color=CWHITE).next_to(c2, DOWN)
        t3 = Text("Output", font=FONT_R, font_size=30, color=CRED).next_to(c3, RIGHT)

        self.play(Create(c1), 
                  d5[0].animate.set_color(CBLUE),
                  Write(t1)
                  )
        self.wait(2)

        self.play(Create(c2), 
                  d5[0].animate.set_color(CWHITE),
                  Write(t2)
                  )
        self.wait(2)

        self.play(Create(c3), 
                  d5[4].animate.set_color(CRED),
                  Write(t3)
                  )
        self.wait(2)

class BigANN(Scene):
    def construct(self):
        setup(self)

        (d1, l1) = create_nn([5, 1,1], 0.1)
        t1 = Text("...", font=FONT_R, color=CWHITE, font_size=30).move_to(d1[0][1]).rotate(PI/2)
        t12 = Text("...", font=FONT_R, color=CWHITE, font_size=30).move_to(d1[1][0])
        t13 = Text("...", font=FONT_R, color=CWHITE, font_size=30).move_to(d1[2][0])
        t14 = Text("2500 nodes", font=FONT_R, color=CWHITE, font_size=30).next_to(d1[0][2], LEFT)

        d1[0][1] = t1
        d1[1][0] = t12
        d1[2][0] = t13

        self.play(Create(d1), Create(l1), Write(t14), run_time=2)
        self.wait(1)
        self.play(Unwrite(t14))
        self.wait(1)

        # second

        (d2, l2) = create_nn([5, 6, 6, 6, 6, 1], 0.1)

        t2 = Text("...", font=FONT_R, color=CWHITE, font_size=30).move_to(d2[0][1]).rotate(PI/2)
        t22 = Text("...", font=FONT_R, color=CWHITE, font_size=30).move_to(d2[5][0])

        d2[0][1] = t2
        d2[5][0] = t22

        self.play(Transform(d1, d2), Transform(l1, l2))
        self.wait(2)

        #third

        (d3, l3) = create_nn([5, 6, 6, 6, 6, 2], 0.1)

        t3 = Text("...", font=FONT_R, color=CWHITE, font_size=30).move_to(d3[0][1]).rotate(PI/2)

        d3[0][1] = t3

        self.play(Transform(d1, d3), Transform(l1, l3))
        self.wait(1)

        cat = Text("Cat", font=FONT_R, color=CBLUE , font_size=30).next_to(d3[5][0], RIGHT)
        dog = Text("Dog", font=FONT_R, color=CRED , font_size=30).next_to(d3[5][1], RIGHT)

        self.play(Write(cat), 
                  Write(dog), 
                  d3[5][0].animate.set_color(CBLUE),
                  d3[5][1].animate.set_color(CRED),
                  )

        self.wait(3)

class NothingSpecific(Scene):
    def construct(self):
        setup(self)

        t1 = MathTex(r"f(x)", color=CWHITE ,font_size=60).shift(RIGHT * 4)
        t2 = MathTex(r"f(x_1, x_2)", color=CWHITE ,font_size=60).shift(RIGHT * 4)
        t3 = MathTex(r"f(x_1, x_2, x_3)", color=CWHITE ,font_size=60).shift(RIGHT * 4)
        t4 = MathTex(r"f(x_1, x_2, x_3, ..., x_n)", color=CWHITE ,font_size=60).shift(RIGHT * 4)

        self.play(Write(t1))
        self.wait()

        self.play(Transform(t1, t2))
        self.play(Transform(t1, t3))
        self.play(Transform(t1, t4))

        self.wait(2)

class NothingSpecific2(Scene):
    def construct(self):
        self.camera.background_color = CWHITE

        (d1, l1) = create_nn([1, 1], 0.2, dot_color=CBLUE)
        (d2, l2) = create_nn([2, 3, 2], 0.2, dot_color=CBLUE)
        (d3, l3) = create_nn([3, 4, 4, 2], 0.2, dot_color=CBLUE)
        (d4, l4) = create_nn([5, 6, 6, 6, 6, 2], 0.2, dot_color=CBLUE)

        d1.shift(LEFT * 4)
        d2.shift(LEFT * 4)
        d3.shift(LEFT * 4).scale(0.8)
        d4.shift(LEFT * 4).scale(0.6)

        l1.shift(LEFT * 4)
        l2.shift(LEFT * 4)
        l3.shift(LEFT * 4).scale(0.8)
        l4.shift(LEFT * 4).scale(0.6)

        t = Text("...", font=FONT_R, color=CBLUE, font_size=20).move_to(d4[0][1]).rotate(PI/2)

        d4[0][1] = t

        self.play(Create(d1), Create(l1))
        self.wait()

        self.play(Transform(d1, d2), Transform(l1, l2))
        self.play(Transform(d1, d3), Transform(l1, l3))
        self.play(Transform(d1, d4), Transform(l1, l4))

        self.wait(2)

def create_matrix(a, b):
    elements = np.arange(a * b)
    matrix = elements.reshape((a, b)).T

    return matrix.flatten()

class ToCalculateThisOutputNode(Scene):
    def construct(self):
        setup(self)

        (d, l) = create_nn([5, 6, 6, 6, 6, 2], 0.1)

        l2 = l.copy()
        l3 = VGroup()

        l3.add(*[l2[i] for i in create_matrix(5,6)])
        l3.add(*[l2[i+30] for i in create_matrix(6,6)])
        l3.add(*[l2[i+66] for i in create_matrix(6,6)])
        l3.add(*[l2[i+102] for i in create_matrix(6,6)])
        l3.add(*[l2[i+138] for i in create_matrix(6,2) if i % 2 == 0])

        t = Text("...", font=FONT_R, color=CWHITE, font_size=30).move_to(d[0][1]).rotate(PI/2)

        d[0][1] = t
        self.add(l, d)

        self.play(
            d[0].animate.set_color("#4d5c6b"),
            d[1].animate.set_color("#4d5c6b"),
            d[2].animate.set_color("#4d5c6b"),
            d[3].animate.set_color("#4d5c6b"),
            d[4].animate.set_color("#4d5c6b"),
            d[5][0].animate.set_color("#4d5c6b"),
            # l.animate.set_color("#2d3740"),
            Uncreate(l)
            )

        self.play(ScaleInPlace(d[5][1], scale_factor=1.7))

        self.wait(1)

        self.play(
            d[0].animate.set_color("#fdfcdc"),
                )

        self.play(
                Create(l3),
                d[1].animate.set_color("#fdfcdc"),
                d[2].animate.set_color("#fdfcdc"),
                d[3].animate.set_color("#fdfcdc"),
                d[4].animate.set_color("#fdfcdc"),
                run_time=4
                )

        self.wait(2)

class ToFindThisNode(Scene):
    def construct(self):
        setup(self)

        (d, l) = create_nn([5, 6, 6, 6, 6, 2], 0.1)

        l2 = l.copy()
        l3 = VGroup()

        l3.add(*[l2[i] for i in create_matrix(5,6)])
        l3.add(*[l2[i+30] for i in create_matrix(6,6)])
        l3.add(*[l2[i+66] for i in create_matrix(6,6)])
        l3.add(*[l2[i+102] for i in create_matrix(6,6)])
        l3.add(*[l2[i+138] for i in create_matrix(6,2) if i % 2 == 0])

        t = Text("...", font=FONT_R, color=CWHITE, font_size=30).move_to(d[0][1]).rotate(PI/2)

        d[0][1] = t

        prev = d[2]
        this = d[3][3]
        conn = l3[66 + 12:102 - 18]

        self.add(l3, d)

        self.wait(2)

        self.play(
            d.animate.set_color("#323b45"),
            l3.animate.set_color("#2d3740")
        )
        self.play(
            this.animate.set_color("#fdfcdc")
        )

        self.wait(2)

        self.play(
            prev.animate.set_color("#00afb9"),
            conn.animate.set_color("#f07167")
        )

        ng = VGroup(prev.copy(), this.copy(), conn.copy())
        self.add(ng)

        self.wait(2)
        self.play(FadeOut(l3), FadeOut(d), ng.animate.move_to([-4.3,0,0]))
        self.wait(2)

        prev = ng[0]
        conn = ng[2]
        this = ng[1]

        lab1 = Text(" (hidden layer 3)", font=FONT_R, color=CBLUE , font_size=14).next_to(ng, LEFT)
        lab2 = Text(" (weight layer 3)", font=FONT_R, color=CRED, font_size=14).next_to(conn, RIGHT)
        lab3 = Text(" (hidden layer 4)", font=FONT_R, color=CWHITE, font_size=14).next_to(this, RIGHT)

        ll1 = MathTex("i", color=CBLUE).next_to(lab1, DOWN)
        ll2 = MathTex("w", color=CRED).next_to(lab2, DOWN)
        ll3 = MathTex("output", color=CWHITE).next_to(lab3, UP).scale(0.8)

        self.play(
                Write(lab1),
                Write(lab2),
                Write(lab3),
                Write(ll1),
                Write(ll2),
                Write(ll3)
                )

        self.wait(2)

        eq1 = MathTex(
                "i_{1}", 
                "w_{1}", 
                "+",
                "i_{2}", 
                "w_{2}", 
                "+",
                "i_{3}", 
                "w_{3}", 
                "+",
                "i_{4}", 
                "w_{4}", 
                "+",
                "i_{5}", 
                "w_{5}", 
                "+",
                "i_{6}", 
                "w_{6}", 
                "+",
                "b"
                ).scale(0.6)
        eq1.move_to([3.4,1,0])

        mm = create_matrix(6, 3)
        for i in range(6):
            eq1[mm[i]].set_color("#00afb9")
        for i in range(6, 12):
            eq1[mm[i]].set_color(CRED)
        for i in range(12, 18):
            eq1[mm[i]].set_color("#839096")
        eq1[18].set_color(CGREEN)

        z = MathTex(r"z \; = \;").set_color(CGREEN).scale(0.6).next_to(eq1, LEFT)

        eq2 = MathTex("output\;=\;", "\sigma (", "z", ")").set_color(CWHITE).move_to([0.7, 0, 0]).scale(0.6)
        eq2[2].set_color(CGREEN)

        arr = MathTex(r"\big\uparrow", color=CWHITE, font_size=18).next_to(eq2[1], DOWN)
        act_func = Text("(Activation Function)", font=FONT_R, color=CWHITE, font_size=15).next_to(arr, DOWN)

        for i in range(6):
            self.play(Create(eq1[mm[i]]), run_time=0.1)
        for i in range(6, 12):
            self.play(Create(eq1[mm[i]]), run_time=0.1)

        self.wait(1)

        for i in range(12, 17):
            self.play(Create(eq1[mm[i]]), run_time=0.1)

        self.wait(2)
        self.play(Create(eq1[mm[17]]), Create(eq1[18]), run_time=0.1)
        self.wait(1)
        self.play(Create(z), run_time=0.5)
        self.wait(2)

        self.play(Create(eq2[1]), Create(eq2[2]), Create(eq2[3]))
        self.wait()
        self.play(Create(arr), Create(act_func))
        self.wait()
        self.play(Create(eq2[0]))
        self.wait(2)



