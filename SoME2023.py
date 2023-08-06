from manim import *
import numpy as np
import random
import math

CWHITE = "#fdfcdc"
CBLUE = "#008aab"
CBLUE2 = "#00afb9"
CRED = "#f07167"
CGREEN = "#49de64"
CBLACK = "#171d23"

FONT_R = "JetBrainsMono Nerd Font"
FONT_SIZE = 18

def CreateBox(self, tb, run_time=1):
    center = tb.get_center()
    circle = RoundedRectangle(width=0.01, height=0.01, corner_radius=0.01, color=tb[0].get_color()).move_to(center)

    self.add(circle)
    self.play(ReplacementTransform(circle, tb[0]), run_time=run_time/2)
    self.play(Create(tb[1]), run_time=run_time/2)

def Panel(obj, color=CWHITE, corner=0.15):
    return SurroundingRectangle(obj, color=color, buff=0.2, corner_radius=corner)

def CText(text, color=CWHITE, font_size=FONT_SIZE):
    t = Text(text, color=color, font_size=font_size, font=FONT_R)
    return t

def TextBox(text,color=CBLUE,text_color=CWHITE, text_size=FONT_SIZE, fill_opacity=1, corner=0):
    if isinstance(text, str):
        t = CText(text, text_color, text_size)
    else:
        t = text.set_color(text_color)
    box = SurroundingRectangle(t, fill_opacity=fill_opacity, color=color, buff=0.2, corner_radius=corner)
    return VGroup(box, t)

def CArrow(direction, color=CWHITE, is_oposite=False, size=1):
    size *= 1.1
    if is_oposite:
        if direction[1] == 1:
            arr = MathTex(r"\big\uparrow", color=color).scale(size)
        elif direction[1] == -1:
            arr = MathTex(r"\big\downarrow", color=color).scale(size)
        elif direction[0] == -1:
            arr = MathTex(r"\leftarrow", color=color).scale(size)
        elif direction[0] == 1:
            arr = MathTex(r"\rightarrow", color=color).scale(size)
    else:
        if direction[1] == -1:
            arr = MathTex(r"\big\uparrow", color=color).scale(size)
        elif direction[1] == 1:
            arr = MathTex(r"\big\downarrow", color=color).scale(size)
        elif direction[0] == 1:
            arr = MathTex(r"\leftarrow", color=color).scale(size)
        elif direction[0] == -1:
            arr = MathTex(r"\rightarrow", color=color).scale(size)

    return arr

def ArrowTo(obj, direction, color=CWHITE):
    arr = CArrow(direction, color, False).next_to(obj, direction)
    return arr

def ArrowFrom(obj, direction, color=CWHITE):
    arr = CArrow(direction, color, True).next_to(obj, direction)
    return arr

def Label(text, obj, direction, color=CWHITE, text_size=FONT_SIZE, oppo=False):
    arr = CArrow(direction, color, oppo).next_to(obj, direction, 0.2)
    if isinstance(text, str):
        t = CText(text, color, text_size).next_to(arr, direction) 
    else:
        t = text.set_color(color).next_to(arr, direction) 

    return VGroup(arr, t)

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

        arr2 = MathTex(r"\big\uparrow", color=CWHITE, font_size=18).next_to(eq1[18], DOWN)
        bias = Text("(Bias)", font=FONT_R, color=CGREEN, font_size=14).next_to(arr2, DOWN)

        for i in range(6):
            self.play(Create(eq1[mm[i]]), run_time=0.1)
        for i in range(6, 12):
            self.play(Create(eq1[mm[i]]), run_time=0.1)

        self.wait(1)

        for i in range(12, 17):
            self.play(Create(eq1[mm[i]]), run_time=0.1)

        self.wait(2)
        self.play(Create(eq1[mm[17]]), Create(eq1[18]), Create(arr2), Create(bias), run_time=0.1)
        self.wait(1)
        self.play(Create(z), run_time=0.5)
        self.wait(2)

        self.play(Create(eq2[1]), Create(eq2[2]), Create(eq2[3]))
        self.wait()
        self.play(Create(arr), Create(act_func))
        self.wait()
        self.play(Create(eq2[0]))
        self.wait(2)

class BiasIsThere(Scene):
    def construct(self):
        setup(self)

        eq = MathTex(r"output = \sigma(", "input", "\cdot","weight", "+","bias",")", color=CWHITE)
        eq.move_to([0,2.5,0])
        eq[1].set_color(CBLUE)
        eq[3].set_color(CRED)
        eq[5].set_color(CGREEN)

        ax = Axes(
            x_range=[-5, 5, 1],
            y_range=[-2, 2, 1],
            tips=False,
            axis_config={
                "include_numbers": False,
                "color": "#3e4d5c",
            },
        )

        def func(x):
            return ((np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x)))

        # graph = ax.plot(lambda x: ((np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))) + b.get_value(), x_range=[-5, 5], color=CWHITE, use_smoothing=True)
        graph = ax.plot(func, x_range=[-5, 5], color=CWHITE)

        g = VGroup(ax, graph)
        g.move_to([0,-1,0])
        g.scale(0.7)

        arr = MathTex(r"\big\uparrow", color=CWHITE, font_size=18).next_to(eq[5], DOWN)
        bv = DecimalNumber(0.0, font_size=20, color=CGREEN).next_to(arr, DOWN)

        self.play(Create(eq), Create(ax), run_time=1.3)
        self.play(Create(graph), Create(arr), Create(bv),run_time=2)

        self.wait(1)
        self.play(graph.animate.move_to([-0.87,-1,0]), ChangeDecimalToValue(bv, 1), run_time=1.5)
        self.play(graph.animate.move_to([0.87,-1,0]), ChangeDecimalToValue(bv, -1),run_time=1.5)
        self.play(graph.animate.move_to([0,-1,0]), ChangeDecimalToValue(bv, 0), run_time=1.5)
        self.wait(2)

class WeightAndBias(Scene):
    def construct(self):
        setup(self)

        eq = MathTex(r"output = \sigma(", "input", "\cdot","weight", "+","bias",")", color=CWHITE)
        eq.move_to([0,1.5,0])
        eq[1].set_color(CBLUE)
        eq[3].set_color(CRED)
        eq[5].set_color(CGREEN)

        c1 = Panel(eq[3], color=CRED)
        c2 = Panel(eq[5], color=CGREEN)

        (d, l) = create_nn([2, 3, 3, 2], 0.1)
        (d2, l2) = create_nn([2, 3, 3, 2], 0.05, dot_color=CGREEN)

        d.move_to([0, -0.8, 0])
        d2.move_to([0, -0.8, 0])
        l.move_to([0, -0.8, 0])

        self.add(eq)

        self.play(Create(l), Create(d))

        self.play(
                Create(c1), l.animate.set_color(CRED),
                  )
        self.play(
                Create(c2),
                d.animate.set_color("#28313b"),
                FadeIn(d2[1:]),
                  )

        self.wait(1)

        self.play(
                Uncreate(c1), l.animate.set_color(CBLUE),
                )
        self.play(
                Uncreate(c2),
                d.animate.set_color(CWHITE),
                FadeOut(d2[1:]),
                )

        self.wait(1)

class ThatIt(Scene):
    def construct(self):
        setup(self)

        (d1, l1) = create_nn([1, 1])
        d1[1].set_color(CBLUE)
        l1.set_color(CBLUE)

        (d2, l2) = create_nn([1, 1, 1])
        d2[1].set_color(CBLUE)
        l2[0].set_color(CBLUE)
        d2[2].set_color(CRED)
        l2[1].set_color(CRED)

        (d3, l3) = create_nn([1, 2, 1])
        d3[1].set_color(CBLUE)
        l3[0].set_color(CBLUE)
        l3[1].set_color(CBLUE)
        d3[2].set_color(CRED)
        l3[2:].set_color(CRED)

        (d4, l4) = create_nn([1, 1, 1, 1])
        d4[1].set_color(CBLUE)
        l4[0].set_color(CBLUE)
        d4[2].set_color(CRED)
        l4[1].set_color(CRED)
        d4[3].set_color(CGREEN)
        l4[2].set_color(CGREEN)

        v1 = 1
        d1.move_to([0,v1, 0])
        d2.move_to([0,v1, 0])
        d3.move_to([0,v1, 0])
        d4.move_to([0,v1, 0])
        l1.move_to([0,v1, 0])
        l2.move_to([0,v1, 0])
        l3.move_to([0,v1, 0])
        l4.move_to([0,v1, 0])

        # (d4, l4) = create_nn([2, 3, 2])
        # d4[1].set_color(CBLUE)
        # d4[2].set_color(CRED)
        # l4[0:6].set_color(CBLUE)
        # l4[6:].set_color(CRED)

        eq1 = MathTex("output = \sigma(", "i", "w + b)",
            font_size=60,
             color=CBLUE)
        eq1[1].set_color(CWHITE)

        eq2 = MathTex("output = \sigma_2(", "\sigma_1(", "i", "w_1+b_1)", "w_2 + b_2)",
            font_size=60,
             color=CRED)
        eq2[1].set_color(CBLUE)
        eq2[3].set_color(CBLUE)
        eq2[2].set_color(CWHITE)

        eq3 = MathTex("output = \sigma_3(", "\sigma_2(", "\sigma_1(", "i", "w_1+b_1)", "w_2 + b_2)", "w_3 + b_3)",
            font_size=50,
             color=CGREEN)
        eq3[1].set_color(CRED)
        eq3[5].set_color(CRED)
        eq3[2].set_color(CBLUE)
        eq3[4].set_color(CBLUE)
        eq3[3].set_color(CWHITE)

        eq4 = MathTex("output = \sigma_2(" ,
                      "\sigma_1(", "i", "w_1 + b1)",
                      "w_3 +",
                      "\sigma_1(", "i", "w_2 + b2)",
                      "w_4 + b_3 )",
                      font_size=40, color=CRED)
        eq4[1].set_color(CBLUE)
        eq4[3].set_color(CBLUE)
        eq4[5].set_color(CBLUE)
        eq4[7].set_color(CBLUE)
        eq4[2].set_color(CWHITE)
        eq4[6].set_color(CWHITE)

        v2 = -1
        eq1.move_to([0,v2,0])
        eq2.move_to([0,v2,0])
        eq3.move_to([0,v2,0])
        eq4.move_to([0,v2,0])

        w = 1
        self.play(Create(l1), Create(d1))
        self.play(Write(eq1))
        self.wait(w)

        self.play(Transform(l1, l2), Transform(d1, d2))
        self.play(Transform(eq1, eq2))
        self.wait(w)

        self.play(Transform(l1, l4), Transform(d1, d4))
        self.play(Transform(eq1, eq3))
        self.wait(w)

        self.play(Transform(l1, l3), Transform(d1, d3))
        self.play(Transform(eq1, eq4))
        self.wait(w)

class ForwardPass(Scene):
    def construct(self):
        setup(self)

        (d, l) = create_nn([5, 6, 6, 6, 5, 2], 0.1)

        l2 = l.copy()
        l3 = VGroup()

        l3.add(VGroup(*[l2[i] for i in create_matrix(5,6)]))
        l3.add(VGroup(*[l2[i+30] for i in create_matrix(6,6)]))
        l3.add(VGroup(*[l2[i+66] for i in create_matrix(6,6)]))
        l3.add(VGroup(*[l2[i+102] for i in create_matrix(6,5)]))
        l3.add(VGroup(*[l2[i+132] for i in create_matrix(5,2)]))

        t = Text("...", font=FONT_R, color=CWHITE, font_size=30).move_to(d[0][1]).rotate(PI/2)

        d[0][1] = t

        d.scale(0.6)
        d.set_color("#546575")
        l3.scale(0.6)
        l3.move_to([0, -0.5, 0])
        d.move_to([0, -0.5, 1])

        t = Text("Forward Propagation", font=FONT_R, color=CWHITE, font_size=20).move_to([0, 2, 0])

        self.play(Create(d))
        self.play(d[0].animate.set_color(CWHITE), run_time=1)
        self.play(Create(l3[0]), d[1].animate.set_color(CWHITE), run_time=1)
        self.play(Create(l3[1]), d[2].animate.set_color(CWHITE), Write(t), run_time=1)
        self.play(Create(l3[2]), d[3].animate.set_color(CWHITE), run_time=1)
        self.play(Create(l3[3]), d[4].animate.set_color(CWHITE), run_time=1)
        self.play(Create(l3[4]), d[5].animate.set_color(CWHITE), run_time=1)

        self.wait(1)

        self.play(l3.animate.move_to([-3, -0.5, 0]), d.animate.move_to([-3, -0.5, 1]))


        eq = MathTex(r"\begin{bmatrix} \;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\; \\ \;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\; \end{bmatrix}", font_size=42, color=CWHITE).move_to([3.5, -0.5, 0])
        eq1 = MathTex(r"output_1(I, W, B)", font_size=40, color=CRED).move_to([3.5, -0.2, 0])
        eq2 = MathTex(r"output_2(I, W, B)", font_size=40, color=CBLUE).move_to([3.5, -0.8, 0])

        func = MathTex(r"ANN(I, W, B)=", font_size=40, color=CWHITE).next_to(eq, LEFT)

        gg = VGroup(eq, eq1, eq2, func).scale(0.7)

        arr = MathTex(r"\big\uparrow", color=CWHITE, font_size=18).next_to(func, DOWN)
        tt1 = Text("I: every model inputs", font=FONT_R, color=CWHITE, font_size=15).next_to(arr, DOWN)
        tt2 = Text("W: every weights", font=FONT_R, color=CWHITE, font_size=15).next_to(tt1, DOWN).shift(LEFT * 0.37)
        tt3 = Text("B: every biases", font=FONT_R, color=CWHITE, font_size=15).next_to(tt2, DOWN).shift(LEFT*0.08)
        tg = VGroup(tt1, tt2, tt3)

        self.play(Create(gg), run_time=2)
        self.wait()
        self.play(Create(arr), Create(tg), run_time=2)

        self.wait(5)

class RandomModelParam(Scene):
    def construct(self):
        setup(self)

        (d, l1) = create_nn([2, 3, 3, 2], 0.1)
        d.move_to([-4, 0, 0])
        l1.move_to([-4, 0, 0])

        l1.set_opacity(1)
        l2 = l1.copy()
        l3 = l1.copy()
        l4 = l1.copy()

        for i in l1:
            color = interpolate_color(CRED, CBLUE, random.uniform(0, 1))
            i.set_color(color)
            i.set_opacity(random.uniform(0.05, 1))
        for i in l2:
            color = interpolate_color(CBLUE, CWHITE, random.uniform(0, 1))
            i.set_color(color)
            i.set_opacity(random.uniform(0.1, 1))
        for i in l3:
            color = interpolate_color(CWHITE, CGREEN, random.uniform(0, 1))
            i.set_color(color)
            i.set_opacity(random.uniform(0.2, 1))
        for i in l4:
            color = interpolate_color(GREEN, CGREEN, random.uniform(0, 1))
            i.set_color(color)
            i.set_opacity(random.uniform(0.3, 1))

        err_cal = TextBox("Error Calculator", CRED)
        arr1 = ArrowTo(err_cal, LEFT, CRED)
        arr2 = ArrowFrom(err_cal, RIGHT, CRED)

        self.play(Create(l1), Create(d), run_time=0.5)
        CreateBox(self, err_cal)
        self.play(Create(arr1), Create(arr2), run_time=0.3)
        self.play(Transform(l1, l2), run_time=1.7, rate_func=rate_functions.linear)
        self.play(Transform(l1, l3), run_time=1.8, rate_func=rate_functions.linear)
        self.play(Transform(l1, l4), run_time=1.6, rate_func=rate_functions.linear)
        self.wait(2)

class ErrorFuncIntro(Scene):
    def construct(self):
        setup(self)

        err_cal = TextBox("Error Calculator", CRED)

        n11 = MathTex(r"Error(", "prediction", ", target", ")", color=CWHITE)#!/usr/bin/env python
        n11[1].set_color(CRED)
        n11[2].set_color(CGREEN)

        n12 = MathTex(r"E(", "y", ", \hat{y}", ")", color=CWHITE, fill_opacity=0.5).next_to(n11, DOWN)
        n12[1].set_color(CRED)
        n12[2].set_color(CGREEN)

        n2 = MathTex(r"C(", "y", ", \hat{y}", ")", color=CWHITE, fill_opacity=0.7).next_to(n12, DOWN)
        n2[1].set_color(CRED)
        n2[2].set_color(CGREEN)
        t2 = Label("(Cost)", n2, RIGHT, CWHITE)

        n3 = MathTex(r"L(", "y", ", \hat{y}", ")", color=CWHITE, fill_opacity=0.7).next_to(n2, DOWN)
        n3[1].set_color(CRED)
        n3[2].set_color(CGREEN)
        t3 = Label("(Loss)", n3, RIGHT, CWHITE)

        tt1 = VGroup(MathTex(r"y", color=CRED), CText(": prediction")).arrange(buff=0.05)
        tt1.move_to([-5, -3, 0])
        tt2 = VGroup(MathTex(r"\hat{y}", color=CGREEN), CText(": target")).arrange(buff=0.05).next_to(tt1, RIGHT)

        # self.add(n11, n12, n2, t2, n3, t3, tt1, tt2)
        self.wait()
        CreateBox(self, err_cal)
        self.wait(2)

        self.play(FadeOut(err_cal), Create(n11), Create(n12))
        self.wait(2)
        self.play(Create(tt1), Create(tt2))

        self.play(Create(n2), Create(t2))

        self.play(Create(n3), Create(t3))

        self.wait(2)

        self.play(FadeOut(n3), FadeOut(t3))
        self.play(FadeOut(n2), FadeOut(t2))
        self.play(n12.animate.move_to(n11.get_center()).set_opacity(1), FadeOut(n11), VGroup(tt1, tt2).animate.next_to(n11, DOWN))
        self.wait(2)

class VarietyOfError(Scene):
    def construct(self):
        setup(self)

        color1 = CWHITE
        color2 = CBLUE 

        screen_width = config.frame_width
        rectangle_width = screen_width / 2

        rectangle1 = Rectangle(width=rectangle_width, height=config.frame_height, color=color1, fill_opacity=1).move_to([-3.5,0,0])
        rectangle2 = Rectangle(width=rectangle_width, height=config.frame_height, color=color2, fill_opacity=1).next_to(rectangle1, RIGHT, buff=0)

        self.add(rectangle1, rectangle2)

        cla = CText("Classification", color=CBLACK).move_to(rectangle1).scale(1.5).shift(UP * 2)
        res = CText("Regression", color=CWHITE).move_to(rectangle2).scale(1.5).shift(UP * 2)

        self.wait()
        self.play(Create(cla), Create(res))
        self.wait()

        a1 = CText("Cross-Entropy Loss", CBLACK).move_to(rectangle1)
        a2 = CText("Hinge Loss", CBLACK).move_to(rectangle1).next_to(a1, UP)
        a3 = CText("Sparse Categorical Cross-Entropy Loss", CBLACK).move_to(rectangle1).next_to(a1, DOWN)

        self.play(Create(a1), Create(a2), Create(a3))

        b1 = CText("Mean Squared Error", CWHITE).move_to(rectangle2)
        b2 = CText("Mean Absolute Error", CWHITE).move_to(rectangle1).next_to(b1, UP)
        b3 = CText("Huber Loss", CWHITE).move_to(rectangle1).next_to(b1, DOWN)

        self.play(Create(b1), Create(b2), Create(b3))
        self.wait(2)

class WrongPrediction(Scene):
    def construct(self):
        setup(self)

        (d, l) = create_nn([5, 6, 6, 6, 5, 2], 0.1)
        d.scale(0.6)
        l.scale(0.6)
        d.move_to([-1.5, 0,0])
        l.move_to([-1.5, 0,0])

        l2 = l.copy()
        l3 = VGroup()

        l3.add(VGroup(*[l2[i] for i in create_matrix(5,6)]))
        l3.add(VGroup(*[l2[i+30] for i in create_matrix(6,6)]))
        l3.add(VGroup(*[l2[i+66] for i in create_matrix(6,6)]))
        l3.add(VGroup(*[l2[i+102] for i in create_matrix(6,5)]))
        l3.add(VGroup(*[l2[i+132] for i in create_matrix(5,2)]))

        t = Text("...", font=FONT_R, color=CWHITE, font_size=30).move_to(d[0][1]).rotate(PI/2)

        d[0][1] = t
        d[5][1].set_color(CRED)
        d[5][0].set_color(CBLUE)
        l3.set_color(CWHITE)

        b1 = MathTex(r" \begin{bmatrix} \;\;\; \\ \;\;\;\;\; \\ \end{bmatrix}", color=CWHITE)
        p1 = MathTex(r"0.8", color=CRED).next_to(d[5][1], RIGHT, buff=0.8)
        p2 = MathTex(r"0.2", color=CBLUE).next_to(d[5][0], RIGHT, buff=0.8)
        b1.move_to(VGroup(p1, p2).get_center())

        b2 = MathTex(r" \begin{bmatrix} \;\;\; \\ \;\;\;\;\; \\ \end{bmatrix}", color=CGREEN)
        t1 = MathTex(r"0.0", color=CRED).next_to(p1, RIGHT, buff=1.5)
        t2 = MathTex(r"1.0", color=CBLUE).next_to(p2, RIGHT, buff=1.5)
        b2.move_to(VGroup(t1, t2).get_center())

        pre = Label("Prediction", b1, UP, color=CWHITE)
        tar = Label("Target", b2, UP, color=CGREEN)

        equal = MathTex(r"=", color=CWHITE).scale(0.7).next_to(b1, LEFT)
        but = MathTex(r"but", color=CGREEN).scale(0.7).next_to(b2, LEFT)

        # self.add(l3, d, p1, p2, b1, pre, t1, t2, b2, tar)
        self.wait(2)
        self.play(Create(l), Create(d))
        self.wait()

        self.play(Create(l3), run_time=1)
        self.play(FadeOut(l), Create(p1), Create(p2), Create(b1), Create(pre), Create(equal))
        self.wait()
        self.play(Create(t1), Create(t2), Create(b2), Create(tar), Create(but))
        self.wait(2)

def LB(color=CWHITE, n=2):
    return MathTex(r"\left[\begin{matrix} \," + (r"\\ \,") * (n-1) + r"\end{matrix}\right.", color=color)
def RB(color=CWHITE, n=2):
    return MathTex(r"\left.\begin{matrix} \," + (r"\\ \,") * (n-1) + r"\end{matrix}\right]", color=color)
def M(t1, t2, color=CWHITE):
    return MathTex(r"\begin{matrix}" + t1 + r"\\" + t2 + r"\end{matrix}", color=color)
def HL(obj, color):
    return obj.animate.set_color(color).set_opacity(1)

class WillUseMSE(Scene):
    def construct(self):
        setup(self)

        mse = CText("Mean Squared Error (MSE)", color=CWHITE).scale(1.3)
        f = MathTex(r"E(y, \hat{y}) = ", 
                    r"\frac{1}{n}", 
                    r"\sum_{i=1}^n", 
                    r"(", 
                    r"y_i-", 
                    r"\hat{y}_i", 
                    ")^2", color=CWHITE)

        self.wait()
        self.play(Write(mse), run_time=0.8)
        self.play(mse.animate.move_to([0, 3.1, 0]))
        self.play(Create(f))
        self.wait()
        self.play(f.animate.move_to([0, 1.8, 0]).set_opacity(0.4).scale(0.6))

        eq1 = VGroup(LB(), M("0.8", "0.2"), RB()).arrange(RIGHT)
        eq2 = VGroup(LB(CGREEN), M("0", "1", CGREEN), RB(CGREEN)).arrange(RIGHT)
        minus = MathTex("-", color=WHITE)
        minus2 = M("-", "-", CWHITE)

        eq1.next_to(minus, LEFT, buff=0.5)
        eq2.next_to(minus, RIGHT, buff=0.5)

        pre = Label("prediction", eq1, DOWN, color=CWHITE)
        tar = Label("target", eq2, DOWN, color=CGREEN)

        self.play(Create(eq1), Create(eq2), Create(tar), Create(pre))
        self.wait()
        self.play(Uncreate(pre), Uncreate(tar))
        self.wait()
        self.play(Create(minus), HL(f[4], CWHITE), HL(f[5], CGREEN))
        self.wait()
        self.play(FadeOut(minus), FadeOut(eq2[0]), Transform(eq1[2], minus2))

        open_b = M("(", "(", CBLUE)
        close_b = M(")^2", ")^2", CBLUE)

        self.wait()
        self.play(
                eq1[1].animate.next_to(minus2, LEFT, buff=0.3),
                eq2[1].animate.next_to(minus2, RIGHT, buff=0.3))

        open_b.next_to(eq1[1], LEFT, buff=0.3)
        close_b.next_to(eq2[1], RIGHT, buff=0.3)

        self.play(Create(open_b), Create(close_b), HL(f[3], CBLUE), HL(f[6], CBLUE))

        plus = MathTex(r"+", color=CRED).next_to(open_b, LEFT)

        self.play(FadeOut(eq1[0]), FadeOut(eq2[2]))
        self.wait()
        self.play(Create(plus), HL(f[2], CRED))

        eq3 = VGroup(
                MathTex("(", color=CBLUE),
                MathTex("0.8", color=CWHITE),
                MathTex("-", color=CWHITE),
                MathTex("0", color=CGREEN),
                MathTex(")^2", color=CBLUE),
            ).arrange(RIGHT, buff=0.3)

        eq4 = VGroup(
                MathTex("(", color=CBLUE),
                MathTex("0.2", color=CWHITE),
                MathTex("-", color=CWHITE),
                MathTex("1", color=CGREEN),
                MathTex(")^2", color=CBLUE),
            ).arrange(RIGHT, buff=0.3)

        geq = VGroup(eq3, eq4).arrange(DOWN, buff=0.15)

        plus2 = MathTex("+", color=CRED)

        self.wait()
        self.play(
                Transform(plus, plus2), 
                Create(geq),
                eq3.animate.next_to(plus2, LEFT),
                eq4.animate.next_to(plus2, RIGHT),
                FadeOut(eq1[1]), 
                FadeOut(eq2[1]), 
                FadeOut(eq1[2]),
                FadeOut(open_b),
                FadeOut(close_b),
                )

        frac = Line([-3.2, -0.4, 0], [3.2, -0.4, 0], color=CWHITE)
        deno = MathTex("2", color=CWHITE).next_to(frac, DOWN, buff=0.2)

        self.wait()
        self.play(Create(frac), Create(deno), HL(f[1], CWHITE))

        re = MathTex(r"= 0.64", color=CRED)
        re.next_to(frac, RIGHT, buff=0.2)

        self.wait()
        self.play(Create(re), HL(f[0], CRED))

        self.wait(2)

        self.play(
                FadeOut(frac),
                FadeOut(deno),
                FadeOut(eq3),
                FadeOut(eq4),
                FadeOut(plus),
                FadeOut(f),
                )

        err = MathTex(r"E", color=CRED).move_to([-0.8, 0,0])
        self.play(Create(err), re.animate.next_to(err, RIGHT, buff=0.2))

        sca = Label("A single scalar value", re, DOWN)
        self.wait()
        self.play(Create(sca))

        self.wait(2)

def randomize_weight(obj, color1=CBLUE, color2=CRED):
    for i in obj:
        color = interpolate_color(color1, color2, random.uniform(0, 1))
        i.set_color(color)
        i.set_opacity(random.uniform(0.1, 1))

class NewParameter(Scene):
    def construct(self):
        setup(self)

        (d, l1) = create_nn([2, 3, 3, 2], 0.1)
        d.move_to([0, 1, 0])
        l1.move_to([0, 1, 0])

        l1.set_opacity(1)
        l2 = l1.copy()

        err = DecimalNumber(1.0, color=CRED).scale(0.8)
        t = VGroup(CText("Error: ", color=CRED), err).arrange(RIGHT).move_to([0,-1.5, 0])

        self.add(t)

        randomize_weight(l1, CBLUE, CRED)
        self.add(d, l1)

        self.wait()

        randomize_weight(l2, CBLUE, CWHITE)
        self.play(ReplacementTransform(l1, l2), ChangeDecimalToValue(err, 0.83))
        
        randomize_weight(l1, CGREEN, CRED)
        self.play(ReplacementTransform(l2, l1), ChangeDecimalToValue(err, 0.66))

        randomize_weight(l2, CBLUE, CRED)
        self.play(ReplacementTransform(l1, l2), ChangeDecimalToValue(err, 0.507))
        
        randomize_weight(l1, CGREEN, CRED)
        self.play(ReplacementTransform(l2, l1), ChangeDecimalToValue(err, 0.347))

        randomize_weight(l2, CBLUE, CWHITE)
        self.play(ReplacementTransform(l1, l2), ChangeDecimalToValue(err, 0.187))
        
        randomize_weight(l1, CGREEN, CBLUE)
        self.play(ReplacementTransform(l2, l1), ChangeDecimalToValue(err, 0.0))

        self.wait(2)

class CommonWayError(Scene):
    def construct(self):
        setup(self)

        model_b = TextBox("ANN Function", color=CBLUE)
        error_b = TextBox("Error Function", color=CRED)
        mid_arr = CArrow(LEFT, color=CBLUE)

        VGroup(model_b, mid_arr, error_b).arrange(RIGHT).move_to([0, 2.5, 0])

        inp = Label("Input", model_b, LEFT, color=CBLUE)
        par = Label("Parameters", model_b, DOWN, color=CBLUE)
        tar = Label("Target", error_b, DOWN, color=CGREEN)
        err = Label("Error", error_b, RIGHT, color=CRED, oppo=True)

        g = VGroup(mid_arr, inp, par, tar, err)

        self.wait()
        CreateBox(self,model_b,0.5)
        CreateBox(self,error_b, 0.5)
        self.play(Create(g), run_time=1)

        params = MathTex("w_1", "w_2", "w_3", "...", "w_n", "b_1", "...", "b_n", color=CBLUE).scale(0.8).arrange(DOWN).next_to(par, DOWN, 0.3)
        params[0:5].set_color(CWHITE)

        one_par = params[1].copy()

        self.wait()
        self.play(Create(params))

        self.wait()

        self.wait()
        self.play(one_par.animate.move_to([0, 0,0]))
        self.play(one_par.animate.scale(1.5).set_color(CBLUE2))
        self.wait()
        self.play(one_par.animate.move_to(params[1].get_center()), FadeOut(params[1]))
        # self.play(Uncreate(params), Uncreate(g), Uncreate(model_b), Uncreate(error_b))

        rt = 0.15
        self.play(inp.animate.set_color(CWHITE), run_time=rt)

        self.play(model_b[0].animate.set_color(CWHITE), run_time=rt)
        self.play(inp.animate.set_color(CBLUE), run_time=rt)

        self.play(mid_arr.animate.set_color(CWHITE), run_time=rt)
        self.play(model_b[0].animate.set_color(CBLUE), run_time=rt)

        self.play(error_b[0].animate.set_color(CWHITE), run_time=rt)
        self.play(mid_arr.animate.set_color(CBLUE), run_time=rt)

        self.play(err.animate.set_color(CWHITE), run_time=rt)
        self.play(error_b[0].animate.set_color(CRED), run_time=rt)

        self.play(err.animate.set_color(CRED), run_time=rt)

        new_err = Label("New Error", error_b, RIGHT, color=CWHITE, oppo=True)
        self.play(Transform(err, new_err))

        self.wait(2)

class WhatToDo(Scene):
    def construct(self):
        setup(self)

        w = MathTex(r"w_2", color=CWHITE).scale(2.5)
        w.move_to([-3.2, 0,0])
        arr1 = CArrow(DOWN, CGREEN).next_to(w, RIGHT)

        de = MathTex(r"\Delta E", color=CRED).scale(2.5)
        de.move_to([2.2, 0,0])
        arr21 = CArrow(DOWN, CGREEN).next_to(de, RIGHT)
        arr22 = CArrow(UP, CRED).next_to(de, RIGHT)

        l = Label("change in error", de, DOWN, CWHITE)

        mid_arr = CArrow(LEFT, CWHITE).set_opacity(0.8).shift(LEFT *0.3)

        # self.play(w, arr1, de, arr21, arr22, mid_arr)
        self.wait()

        self.play(Create(w), Create(mid_arr), Create(de), Create(arr1), Create(l))
        self.wait()

        self.play(Create(arr21), l.animate.set_opacity(0.3))
        self.wait()
        self.play(w.animate.set_color(CRED).scale(0.7), run_time=0.9)
        self.wait(2)

        self.play(Transform(arr21, arr22), run_time=0.9)
        self.wait(1)

        self.play(w.animate.set_color(CBLUE2).scale(2), run_time=0.9)
        self.wait(2)

class BasicallyError(Scene):
    def construct(self):
        setup(self)

        bas = CText("Basically", color=CBLUE).move_to([0, 2, 0]).scale(3)
        eq = MathTex(r"\theta_{\texttt{new}} =", r"\theta_{\texttt{old}}", r"-", r"\Delta E", color=CRED).scale(1.5)
        eq[0].set_color(CWHITE)
        eq[1].set_color(CBLUE2)

        l = MathTex(r"\theta: \texttt{Trainable parameters (weights and biases)}", color=CWHITE).scale(0.6).move_to([0, -2, 0])
        l2 = MathTex(r"\Delta E:", r"\texttt{Change in Error when } \theta \texttt{ is increased by a small amount}", color=CWHITE).scale(0.6).move_to([0, -2, 0])
        l2[0].set_color(CRED)
        l2.next_to(l, DOWN)

        self.add(bas, eq[3])
        self.wait(2)
        self.play(Create(eq[1]), Create(eq[2]))
        self.wait()
        self.play(Create(eq[0]))
        self.play(Create(l), Create(l2))
        self.wait(2)

        but = CText("BUT!", color=CRED).scale(5)
        self.remove(bas, eq[0], eq[1], eq[2], eq[3], l, l2)
        self.add(but)
        self.wait(2)

def random_arr_matrix(row=3, col=3):
    re = VGroup()
    for i in range(row):
        temp = VGroup()

        for j in range(col):
            if random.uniform(0, 1) > 0.5:
                temp.add(MathTex(r"\uparrow"))
            else:
                temp.add(MathTex(r"\downarrow"))

        temp.arrange(RIGHT)
        re.add(temp)

    re.arrange(DOWN)
    return re

def weight_matrix(row=3, col=3):
    re = VGroup()
    for i in range(row):
        temp = VGroup()

        for j in range(col):
            temp.add(MathTex(r"w_{" + str(i+1) + str(j+1) + "}"))

        temp.arrange(RIGHT)
        re.add(temp)

    re.arrange(DOWN, buff=0.5)
    return re

def bias_matrix(row=3, col=3):
    re = VGroup()
    for i in range(row):
        temp = VGroup()

        for j in range(col):
            temp.add(MathTex(r"b_{" + str(i+1) + "}"))

        temp.arrange(RIGHT)
        re.add(temp)

    re.arrange(DOWN)
    return re

def randomize_matrix(matrix, obj1, obj2):
    v = matrix[1]
    for i in range(len(v)):
        for j in range(len(v[i])):
            if random.random() > 0.5:
                v[i][j]= obj1.copy().move_to(v[i][j].get_center())
            else:
                v[i][j]= obj2.copy().move_to(v[i][j].get_center())

def questionize_matrix(matrix):
    v = matrix[1]
    for i in range(len(v)):
        for j in range(len(v[i])):
            v[i][j] = MathTex(r"?", color=v[i][j].get_color()).move_to(v[i][j].get_center())

def randomize_scale_matrix(matrix, scale1, scale2):
    v = matrix[1]
    for i in range(len(v)):
        for j in range(len(v[i])):
            if random.random() > 0.5:
                v[i][j].scale(scale1)
            else:
                v[i][j].scale(scale2)

class HowMuch(Scene):
    def construct(self):
        setup(self)

        (d, l) = create_nn([2, 3, 3 ,2], 0.2)
        d.move_to([0, 2.1, 0]).scale(0.7).set_opacity(0.2)
        l.move_to([0, 2.1, 0]).scale(0.7).set_color(CBLUE).set_opacity(0.3)

        d2 = d.copy()
        d2[0].set_opacity(0)
        for i in range(1, len(d2)):
            for j in d2[i]:
                j.scale(0.5).set_color(CRED).set_opacity(1)

        eq = MathTex(r"\theta_{\texttt{new}} =", r"\theta_{\texttt{old}}", r"-", r"\Delta E", color=CRED).scale(0.8).set_opacity(1)
        eq[0].set_color(CWHITE)
        eq[1].set_color(CBLUE2)

        eq2 = MathTex(r"\theta_{\texttt{new}} =", r"\theta_{\texttt{old}}", r"-", r"? \Delta E", color=CRED).scale(0.8).set_opacity(1)
        eq2[0].set_color(CWHITE)
        eq2[1].set_color(CBLUE2)

        eq.move_to([0, -2, 0])
        eq2.move_to([0, -2, 0])

        scale = 0.7

        params = VGroup(
                VGroup(
                    LB(color=CBLUE, n=3),
                    weight_matrix(3, 2).set_color(CBLUE).scale(scale),
                    RB(color=CBLUE, n=3),
                ).arrange(RIGHT, buff=0.05),

                VGroup(
                    LB(color=CRED, n=3),
                    bias_matrix(3, 1).set_color(CRED).scale(scale),
                    RB(color=CRED, n=3),
                ).arrange(RIGHT, buff=0.05),

                VGroup(
                    LB(color=CBLUE, n=3),
                    weight_matrix(3, 3).set_color(CBLUE).scale(scale),
                    RB(color=CBLUE, n=3),
                ).arrange(RIGHT, buff=0.05),

                VGroup(
                    LB(color=CRED, n=3),
                    bias_matrix(3, 1).set_color(CRED).scale(scale),
                    RB(color=CRED, n=3)
                ).arrange(RIGHT, buff=0.05),

                VGroup(
                    LB(color=CBLUE, n=2),
                    weight_matrix(2, 3).set_color(CBLUE).scale(scale),
                    RB(color=CBLUE, n=2),
                ).arrange(RIGHT, buff=0.05),

                VGroup(
                    LB(color=CRED, n=2),
                    bias_matrix(2, 1).set_color(CRED).scale(scale),
                    RB(color=CRED, n=2),
                ).arrange(RIGHT, buff=0.05),
            ).arrange(RIGHT).move_to([0, -0.5, 0])
        
        params2 = params.copy()
        params3 = params2.copy()

        for i in params2:
            randomize_matrix(i, MathTex(r"\uparrow").scale(0.8).set_color(CBLUE), MathTex(r"\downarrow").scale(0.8).set_color(CRED))

        for i in params3:
            questionize_matrix(i)
            randomize_scale_matrix(i, 0.5, 1.3)

        self.add(l, d, eq, d2, params)
        self.wait(2)
        self.play(Transform(params, params2))
        self.wait()
        self.play(Transform(params, params3), Transform(eq, eq2))

        p = Panel(eq2[3], CWHITE)
        self.play(Create(p))
        self.wait(0.5)
        self.play(Uncreate(p))
        self.wait(2)

class LearningRate(Scene):
    def construct(self):
        setup(self)

        eq = VGroup(
            MathTex(r"\theta_{\texttt{new}} = ", color=CWHITE),
            MathTex(r"\theta_{\texttt{old}}", color=CBLUE),
            MathTex(r"-", color=CGREEN),
            MathTex(r"\eta", color=CGREEN),
            MathTex(r"\Delta E", color=CRED),
        ).arrange(RIGHT)


        self.add(eq[4])
        self.wait(1)

        eq[3].next_to(eq[4], LEFT)
        l = Label("Learning Rate", eq[3], DOWN, color=CWHITE)
        self.play(Create(eq[3]), Create(l))

        self.wait()
        self.play(Create(eq[1]), Create(eq[2]))

        self.wait()
        self.play(Create(eq[0]))

        self.wait(2)

class Derivative(Scene):
    def construct(self):
        setup(self)

        f = VGroup(
            VGroup(
                MathTex(r"d"),
                MathTex(r"\frac{\;\;\;\;}{\;\;\;\;}"),
                MathTex(r"d", r"x")
            ).arrange(DOWN, buff=0.1).set_color(CWHITE),
            MathTex(r"f(", color=CWHITE),
            MathTex(r"x", color=CBLUE),
            MathTex(r")", color=CWHITE),
        ).arrange(RIGHT, buff=0.1)
        f[0][2][1].set_color(CBLUE)

        d = CText("Derivative", color=CBLUE).move_to([0, 3, 0])

        l1 = Label("Derivative of f(x)", f[0][0], UP, color=CWHITE)
        l2 = Label("With respect to ", f[0][2][0], DOWN, color=CWHITE)
        l2x = MathTex(r"x", color=CBLUE)
        l2x.next_to(l2[1], RIGHT)

        self.add(f[1], f[2], f[3])

        self.wait()
        self.play(Create(d))

        self.wait()
        self.play(Create(f[0][0]), Create(f[0][1]), Create(f[0][2][0]))
        self.play(Create(f[0][2][1]))
        self.wait()
        self.play(Create(l1))
        self.play(Create(l2), Create(l2x))
        self.wait(2)

class DerivativeOfError(MovingCameraScene):
    def construct(self):
        setup(self)

        axis = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 8, 1],
            tips=False,
            x_length = 5,
            y_length = 5,
            x_axis_config = {
                "tick_size": 0.02,
                "color": CBLUE,
                "stroke_opacity": 0.7
                },
            y_axis_config = {
                "tick_size": 0.02,
                "color": CRED,
                "stroke_opacity": 0.7,
                },
        )

        labels = axis.get_axis_labels(
            MathTex("w_2").scale(1).set_color(CBLUE),
            CText("Error").scale(1.35).set_color(CRED)
        )

        stretch = 0.25
        def func(x):
            x -= 5
            x *= stretch 
            return 0.3 * (pow(x, 5) - 8 * pow(x, 3) + 10 * x) + 5

        graph = axis.plot(func, x_range=[0, 10], use_smoothing=False, color=CRED, stroke_opacity=0.3)

        line1 = axis.get_lines_to_point(
                axis.c2p(3.9, func(3.9)),
                line_config={"dashed_ratio": 1,
                             "stroke_color":CWHITE,
                             "stroke_opacity": 0.4
                             }
                )
        d1 = Dot(axis.c2p(3.9, func(3.9)), radius=0.01, color=CWHITE)

        d2 = Dot(axis.c2p(4.1, func(4.1)), radius=0.01, color=CWHITE)
        line2 = axis.get_lines_to_point(
                axis.c2p(4.1, func(4.1)),
                line_config={"dashed_ratio": 1,
                             "stroke_color":CWHITE,
                             "stroke_opacity":0.4
                             }
                )

        sub = VGroup(d1, d2)

        self.wait()
        self.play(Create(axis), Create(graph), Create(labels), Create(line1), Create(d1))
        self.wait()

        self.camera.frame.save_state()

        self.play(
                self.camera.frame.animate.set(width=sub.width*3).move_to(sub),
                graph.animate.set_stroke_width(0.5),
                line1.animate.set_stroke(width=0.5),
            )
        line2.set_stroke(width=0.5),

        deri = VGroup(
            VGroup(
                MathTex(r"d"),
                MathTex(r"\frac{\;\;\;\;\;}{\;\;\;\;\;}"),
                MathTex(r"d", r"w_2")
            ).arrange(DOWN, buff=0.1).set_color(CWHITE),
            MathTex(r"E", color=CRED),
        ).arrange(RIGHT, buff=0.01).scale(0.05).next_to(sub, RIGHT, buff=0.01)
        deri[0][2][1].set_color(CBLUE)

        self.wait()
        self.play(Create(d2), ReplacementTransform(line1.copy(), line2))

        arr1 = Arrow(d1, [d1.get_x(), d2.get_y(), 0], color=CRED, max_tip_length_to_length_ratio=0.2).scale(1)
        arr2 = Arrow(d1, [d2.get_x(), d1.get_y(), 0], color=CBLUE, max_tip_length_to_length_ratio=0.2).scale(1)
        arr1l = CText("change in Error", color=CRED).scale(0.04).next_to(arr1,LEFT, buff=0.0)
        arr2l = CText("change in w2", color=CBLUE).scale(0.04).next_to(arr2, DOWN , buff=0.0)

        self.play(Create(deri))
        self.play(Create(arr1), Create(arr1l))
        self.play(Create(arr2), Create(arr2l))

        self.wait(2)

        de = MathTex(r"dE", color=CRED).next_to(axis, LEFT)
        de.move_to([de.get_center()[0], d1.get_y(), 0])
        dw = MathTex(r"dw_2", color=CBLUE).next_to(axis, DOWN)
        dw.move_to([d1.get_x(), dw.get_center()[1], 0])

        self.add(de, dw)

        self.play(
                Restore(self.camera.frame), 
                Transform(line2, line1.copy()), 
                Transform(d2, d1.copy()), 
                deri.animate.scale(10).shift(RIGHT),
                graph.animate.set_stroke_width(4),
                line2.animate.set_stroke_width(4),
                FadeOut(arr1l),
                FadeOut(arr2l)
        )

        self.wait(2)

class ElementaryFunction(MovingCameraScene):
    def construct(self):
        setup(self)
        self.camera.frame.shift(LEFT * 3)

        ele_func = VGroup(
            CText("Elementary Function Rules", color=CBLUE).scale(0.8),
            MathTex(r"\texttt{Power function: } \; (x^n)' = nx^{n-1}", color=CWHITE).scale(0.5),
            MathTex(r"\texttt{Trig function: } \; sin'(x) = cos(x), \; cos'(x) = -sin(x)", color=CWHITE).scale(0.5),
            MathTex(r"\texttt{Exponential function: } \; (e^x)' = e^x", color=CWHITE).scale(0.5),
            MathTex(r"\texttt{Logarithmic function: } \; ln'(x) = \frac{1}{x}", color=CWHITE).scale(0.5),

            CText("Comination of Functons Rules", color=CGREEN).scale(0.8),
            MathTex(r"\texttt{Sum Rule: } \; (f(x) + g(x))' = f'(x) + g'(x)", color=CWHITE).scale(0.5),
            MathTex(r"\texttt{Product Rule: } \; (f(x)\cdot g(x))' = f'(x)g(x) + g'(x)f(x)", color=CWHITE).scale(0.5),
            MathTex(r"\texttt{Chain Rule: } \; \frac{d}{dx} f(g(x)) = \frac{df(g(x))}{dg(x)}\cdot \frac{dg(x)}{dx}", color=CWHITE).scale(0.5),
        ).arrange(DOWN, aligned_edge=LEFT).shift(LEFT*6)

        self.wait()
        self.play(Create(ele_func))

        sigma = MathTex(r"\sigma(x) =", color=CWHITE)
        nomi = MathTex(r"1", color=CWHITE)
        frac = MathTex(r"\frac{\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;}{\;}", color=CWHITE)
        deno1 = MathTex(r"1", r"+", r"e^{-1}", color=CWHITE)
        deno1[0].set_color(CRED)
        deno1[1].set_color(CWHITE)
        deno1[2].set_color(CGREEN)
        lb = MathTex(r"(", color=CBLUE).set_opacity(0)
        rb = MathTex(r")^{1}", color=CBLUE).set_opacity(0)
        rb2 = MathTex(r")^{-1}", color=CBLUE)

        f = VGroup(
            sigma,
            VGroup(
                nomi,
                frac,
                VGroup(
                    lb,
                    deno1,
                    rb,
                ).arrange(RIGHT)
            ).arrange(DOWN)
        ).arrange(RIGHT)
        rb.shift(UP*0.03)

        self.wait()
        self.play(Create(f))
        self.remove(lb, rb)
        rb.set_opacity(1)
        lb.set_opacity(1)
        self.wait()
        self.play(Create(lb), Create(rb))
        self.wait()
        self.play(
                FadeOut(nomi),
                FadeOut(frac),
                f[1][2].animate.next_to(sigma, RIGHT)
                )
        rb2.next_to(deno1, RIGHT)
        rb2.shift(UP*0.03)
        self.play(
                Transform(f[1][2][2], rb2),
                )
        self.wait(1)

        L1 = Panel(deno1[2], CGREEN)
        L2 = Panel(deno1[0], CRED)
        g2 = VGroup(lb, deno1, rb2).arrange(RIGHT).next_to(f[0], RIGHT)
        L3 = Panel(g2, CBLUE)

        l1 = Label("Exponential Function", L1, DOWN, color=CGREEN)
        l2 = Label("Constant", L2, UP, color=CRED)
        l3 = Label("Power Function", L3, UP, color=CBLUE).shift(RIGHT * 1)

        self.play(Create(L1), Create(L2), Create(L3))
        self.play(Create(l1), Create(l2), Create(l3))
        self.wait(2)

def derivative(func, variable, color=CBLUE, color2=CRED, color3=CWHITE, buff=0.2, partial=False):
    if partial == True:
        n = MathTex(r"\partial", color=color3)
        d = MathTex(r"\partial", variable, color=color3)
    else:
        n = MathTex(r"d", color=color3)
        d = MathTex(r"d", variable, color=color3)
    d[1].set_color(color)
    line = Line([0,0, 0], [d.get_width(),0 ,0], color=color3)
    g1 = VGroup(n, line ,d).arrange(DOWN, buff=buff)
    g2 = VGroup(g1, func).arrange(RIGHT, buff=buff)
    return g2

class SimplyGiveAnotherFunction(Scene):
    def construct(self):
        setup(self)

        eq1 = derivative(
            VGroup(
                MathTex(r"E(...,", color=CRED),
                MathTex(r"w_2", color=CBLUE),
                MathTex(r", ...)", color=CRED), 
            ).arrange(RIGHT), r"w_2"
        )
        eq2 = VGroup(
                MathTex(r"= \;E'(...,", color=CGREEN),
                MathTex(r"w_2", color=CBLUE),
                MathTex(r", ...)", color=CGREEN), 
            ).arrange(RIGHT)
        g = VGroup(eq1, eq2).arrange(RIGHT)
        self.wait(0.5)
        self.add(eq1)
        self.wait()
        self.play(Create(eq2))
        self.wait()

        self.play(g.animate.move_to([0, 2, 0]))
        self.wait()

        e = CText("(Example from before)").scale(1).move_to([0, 1, 0])
        eq3 = MathTex(r"\sigma(x) = \frac{1}{1+ e^{-x}}").scale(0.8)
        eq32 = MathTex(r"\sigma(x) = (1+e^{-x})^{-1}", color=CBLUE).scale(0.8)

        eq4f = MathTex(r"\Rightarrow \sigma '(x) =").scale(0.8)
        g2 = VGroup(eq3, eq4f).arrange(DOWN).move_to([0, -1, 0])

        eq41 = MathTex(r"\Rightarrow \sigma '(x) =-1(1+e^{-x})^{-2}", color=CRED).scale(0.8)
        eq42 = MathTex(r"\Rightarrow \sigma '(x) =-1(1+e^{-x})^{-2} \cdot (1+e^{-x})'", color=CRED).scale(0.8)
        eq43 = MathTex(r"\Rightarrow \sigma '(x) =-1(1+e^{-x})^{-2} \cdot (-e^{-x})", color=CRED).scale(0.8)
        eq44 = MathTex(r"\Rightarrow \sigma '(x) =\frac{- (-e^{-x})}{(1+e^{-x})^2}", color=CRED).scale(0.8)
        eq45 = MathTex(r"\Rightarrow \sigma '(x) =\frac{e^{-x}}{(1+e^{-x})^2}", color=CGREEN).scale(0.8)

        VGroup(eq3, eq41).arrange(DOWN).move_to([0, -1, 0])
        VGroup(eq3, eq42).arrange(DOWN).move_to([0, -1, 0])
        VGroup(eq3, eq43).arrange(DOWN).move_to([0, -1, 0])
        VGroup(eq3, eq44).arrange(DOWN).move_to([0, -1, 0])
        VGroup(eq3, eq45).arrange(DOWN).move_to([0, -1, 0])

        eq41l = Label("(Power Rule)", eq41, RIGHT, color=CWHITE).set_opacity(1)
        eq42l = Label("(Chain Rule)", eq42, RIGHT, color=CWHITE).set_opacity(1)
        eq43l = Label("(Exponential Rule)", eq43, RIGHT, color=CWHITE).set_opacity(1)
        eq44l = Label("(Simplify)", eq44, RIGHT, color=CWHITE).set_opacity(1)
        eq45l = Label("", eq45, RIGHT, color=CGREEN).set_opacity(0)

        self.play(Create(e))
        self.play(Create(eq3))
        self.wait()
        self.play(Transform(eq3, eq32))
        self.wait()
        self.play(Create(eq4f))

        self.wait()
        self.play(ReplacementTransform(eq4f, eq41))
        self.play(Create(eq41l))
        self.wait()
        self.play(Transform(eq41, eq42), Transform(eq41l, eq42l))
        self.wait()
        self.play(Transform(eq41, eq43), Transform(eq41l, eq43l))
        self.wait()
        self.play(Transform(eq41, eq44), Transform(eq41l, eq44l))
        self.wait()
        self.play(Transform(eq41, eq45), Transform(eq41l, eq45l))
        self.wait()

        eq5 = derivative(MathTex(r"E", color=CRED), "w_2")
        eq52 = derivative(MathTex(r"E", color=CRED), "w_2", partial=True)
        eq53 = derivative(MathTex(r"E(..., w_2, ...)", color=CRED), "w_2", partial=True)

        eq5l = Label("(partial derivative)", eq52, LEFT, color=CWHITE)

        self.play(
                FadeOut(eq41), FadeOut(e),
                FadeOut(eq3),
                FadeOut(eq2),
                Transform(eq1, eq5),
                )
        self.wait()
        self.play(Transform(eq1, eq52))
        self.play(Create(eq5l))
        self.wait()
        self.play(Transform(eq1, eq53), eq5l.animate.next_to(eq53, LEFT))
        self.wait(2)

class ToUpdateAll(Scene):
    def construct(self):
        setup(self)

        lb = LB(n=10)
        rb = RB(n=10)

        g = VGroup(lb.copy(),
            VGroup(
                derivative(MathTex(r"E", color=CRED), "w_1", color="#00AFB9",color3="#00AFB9", partial=True),
                derivative(MathTex(r"E", color=CRED), "w_2", color="#12BBA4",color3="#12BBA4",  partial=True),
                derivative(MathTex(r"E", color=CRED), "w_3", color="#25C78F",color3="#25C78F",  partial=True),
                derivative(MathTex(r"E", color=CRED), "w_{...}", color="#37D279", color3="#37D279",  partial=True),
                derivative(MathTex(r"E", color=CRED), "w_n", color="#49DE64",color3="#49DE64",  partial=True),
                derivative(MathTex(r"E", color=CRED), "b_1", color="#FDFCDC",color3="#FDFCDC",  partial=True),
                derivative(MathTex(r"E", color=CRED), "b_2", color="#FAD9BF",color3="#FAD9BF",  partial=True),
                derivative(MathTex(r"E", color=CRED), "b_3", color="#F7B7A2",color3="#F7B7A2",  partial=True),
                derivative(MathTex(r"E", color=CRED), "b_{...}", color="#F39484",color3="#F39484",  partial=True),
                derivative(MathTex(r"E", color=CRED), "b_n", color="#F07167",color3="#F07167",  partial=True),
            ).scale(0.4).arrange(DOWN, buff=0.1),
            rb.copy()
        ).arrange(RIGHT, buff=0.1)

        n = MathTex(r"- \eta" ,color=CGREEN).shift(RIGHT)

        old_g= VGroup(lb.copy().set_color(CBLUE),
            VGroup(
                MathTex(r"w_{\texttt{old1}}", color="#00AFB9"),
                MathTex(r"w_{\texttt{old2}", color="#12BBA4"),
                MathTex(r"w_{\texttt{old3}", color="#25C78F"),
                MathTex(r"w_{...}", color="#37D279"),
                MathTex(r"w_{\texttt{oldn}", color="#49DE64"),
                MathTex(r"b_{\texttt{old1}", color="#FDFCDC"),
                MathTex(r"b_{\texttt{old2}", color="#FAD9BF"),
                MathTex(r"b_{\texttt{old3}", color="#F7B7A2"),
                MathTex(r"b_{...}", color="#F39484"),
                MathTex(r"b_{\texttt{oldn}", color="#F07167"),
            ).scale(0.5).arrange(DOWN, buff=0.4),
            rb.copy().set_color(CBLUE)
        ).arrange(RIGHT, buff=0.1)

        new_g= VGroup(lb.copy().set_color(CGREEN),
            VGroup(
                MathTex(r"w_{\texttt{new1}}", color="#00AFB9"),
                MathTex(r"w_{\texttt{new2}", color="#12BBA4"),
                MathTex(r"w_{\texttt{new3}", color="#25C78F"),
                MathTex(r"w_{...}", color="#37D279"),
                MathTex(r"w_{\texttt{newn}", color="#49DE64"),
                MathTex(r"b_{\texttt{new1}", color="#FDFCDC"),
                MathTex(r"b_{\texttt{new2}", color="#FAD9BF"),
                MathTex(r"b_{\texttt{new3}", color="#F7B7A2"),
                MathTex(r"b_{...}", color="#F39484"),
                MathTex(r"b_{\texttt{newn}", color="#F07167"),
            ).scale(0.5).arrange(DOWN, buff=0.4),
            rb.copy().set_color(CGREEN)
        ).arrange(RIGHT, buff=0.1)

        old_g.next_to(n, LEFT)
        equal = MathTex(r"=", color=CGREEN).next_to(old_g, LEFT)
        new_g.next_to(equal, LEFT)

        eq0 = derivative(MathTex(r"E(..., w_2, ...)", color=CRED), "w_2", partial=True)
        eq1 = g[1][1].copy()

        self.add(eq0)
        self.wait()
        self.play(Transform(eq0, eq1))
        self.wait()
        self.play(Create(g))
        self.remove(eq0)
        self.wait()
        self.play(Create(n), g.animate.next_to(n, RIGHT))
        self.wait()
        self.play(Create(old_g))
        self.wait()
        self.play(Create(equal), Create(new_g))
        self.wait()

class GradientDescent(Scene):
    def construct(self):
        setup(self)

        lb = LB(n=10)
        rb = RB(n=10)

        g = VGroup(lb.copy(),
            VGroup(
                derivative(MathTex(r"E", color=CRED), "w_1", color="#00AFB9",color3="#00AFB9", partial=True),
                derivative(MathTex(r"E", color=CRED), "w_2", color="#12BBA4",color3="#12BBA4",  partial=True),
                derivative(MathTex(r"E", color=CRED), "w_3", color="#25C78F",color3="#25C78F",  partial=True),
                derivative(MathTex(r"E", color=CRED), "w_{...}", color="#37D279", color3="#37D279",  partial=True),
                derivative(MathTex(r"E", color=CRED), "w_n", color="#49DE64",color3="#49DE64",  partial=True),
                derivative(MathTex(r"E", color=CRED), "b_1", color="#FDFCDC",color3="#FDFCDC",  partial=True),
                derivative(MathTex(r"E", color=CRED), "b_2", color="#FAD9BF",color3="#FAD9BF",  partial=True),
                derivative(MathTex(r"E", color=CRED), "b_3", color="#F7B7A2",color3="#F7B7A2",  partial=True),
                derivative(MathTex(r"E", color=CRED), "b_{...}", color="#F39484",color3="#F39484",  partial=True),
                derivative(MathTex(r"E", color=CRED), "b_n", color="#F07167",color3="#F07167",  partial=True),
            ).scale(0.4).arrange(DOWN, buff=0.1),
            rb.copy()
        ).arrange(RIGHT, buff=0.1)

        n = MathTex(r"- \eta" ,color=CGREEN).shift(RIGHT)
        g.next_to(n, RIGHT)

        self.add(g)

        self.wait()

        self.play(g.animate.move_to(ORIGIN))
        self.wait()

        gra = VGroup(
            MathTex(r"\nabla", color=CBLUE),
            MathTex(r"E", color=CRED)
        ).arrange(RIGHT, buff=0.1)
        gra2 = VGroup(
            MathTex(r"\nabla_{\theta}", color=CBLUE),
            MathTex(r"E", color=CRED)
        ).arrange(RIGHT, buff=0.1)


        l1 = Label("Gradient of the Error Function (For every input)", gra[0], DOWN, color=CWHITE)
        l2 = Label("Gradient of the Error Function (For every model parameter)", gra[0], DOWN, color=CBLUE)
        
        self.play(
            FadeOut(g[0]),
            FadeOut(g[2]),
            Transform(g[1], gra),
        )
        self.play(
            Create(l1),
        )
        self.wait()
        self.play(
            Transform(g[1], gra2),
            Transform(l1, l2)
        )
        self.wait()

        grad = VGroup(
            MathTex(r"\theta_{\texttt{new}} = ", color=CWHITE),
            MathTex(r"\theta_{\texttt{old}}", color=CBLUE),
            MathTex(r"- \nabla_{\theta} E", color=CRED)
        ).arrange(RIGHT, buff=0.08)

        self.play(
            FadeOut(l1)
        )
        self.play(Transform(g[1], grad[2]))
        self.play(Create(grad[0]), Create(grad[1]))

        l3 = CText("Gradient Descent", color=CWHITE).scale(2).shift(UP*1.5)

        self.wait()
        self.play(
            Create(l3)
        )

        l4 = Label("Directions for each of the parameters where the error is decreasing", grad[2], DOWN, color=CRED)
        self.wait()
        self.play(Create(l4))

        self.wait(2)

class AmongChainRule(Scene):
    def construct(self):
        setup(self)

        rule = VGroup(
            CText("Elementary Function Rules", color=CBLUE).scale(0.8),
            MathTex(r"\texttt{Power function: } \; (x^n)' = nx^{n-1}", color=CWHITE).scale(0.5),
            MathTex(r"\texttt{Trig function: } \; sin'(x) = cos(x), \; cos'(x) = -sin(x)", color=CWHITE).scale(0.5),
            MathTex(r"\texttt{Exponential function: } \; (e^x)' = e^x", color=CWHITE).scale(0.5),
            MathTex(r"\texttt{Logarithmic function: } \; ln'(x) = \frac{1}{x}", color=CWHITE).scale(0.5),

            CText("Comination of Functons Rules", color=CGREEN).scale(0.8),
            MathTex(r"\texttt{Sum Rule: } \; (f(x) + g(x))' = f'(x) + g'(x)", color=CWHITE).scale(0.5),
            MathTex(r"\texttt{Product Rule: } \; (f(x)\cdot g(x))' = f'(x)g(x) + g'(x)f(x)", color=CWHITE).scale(0.5),
            MathTex(r"\texttt{Chain Rule: } \; \frac{d}{dx} f(g(x)) = \frac{df(g(x))}{dg(x)}\cdot \frac{dg(x)}{dx}", color=CWHITE).scale(0.5),
        ).arrange(DOWN, aligned_edge=LEFT)

        self.wait()
        self.play(Create(rule))
        self.wait()
        ch = rule[8].copy()
        l = rule[5].copy()
        self.add(ch, l)
        self.play(FadeOut(rule))
        self.play(ch.animate.move_to(ORIGIN).scale(1.5), l.animate.move_to(ORIGIN+UP*1.3))

        self.wait(2)
       
class WhyChainRule(Scene):
    def construct(self):
        setup(self)

        f = TextBox("f(x)", color=CBLUE)

        x = Label("x", f, LEFT, color=CWHITE)
        y = Label("y", f, RIGHT, color=CBLUE2, oppo=True)
        y2 = Label(MathTex(r"\frac{dy}{dx}").scale(0.7), f, RIGHT, color=CBLUE2, oppo=False)

        c_arr = CurvedArrow(y2[1].get_center()+UP*0.5, x[1].get_center()+UP*0.2, color=CBLUE)

        CreateBox(self, f)
        self.play(Create(x), Create(y))
        self.wait()
        self.play(Transform(y, y2))
        self.wait()
        self.play(Create(c_arr), x[1].animate.scale(2).set_color(CGREEN))
        self.play(x[1].animate.scale(0.5).set_color(CWHITE))
        self.wait()

        e_f = TextBox(MathTex(r"E(y, \hat{y})"), color=CRED) 

        self.play(
            FadeOut(x), FadeOut(y), FadeOut(c_arr),
            Transform(f, e_f)
        )

        g1 = VGroup(
            TextBox("Sum\nFunction\n(wx + b)", color=CWHITE, text_color=CBLACK),
            CArrow(LEFT, color=CWHITE).scale(0.6),
            TextBox("Activation\nFunction\n(output)", color=CBLUE),
            CArrow(LEFT, color=CWHITE).scale(0.6),
            TextBox("Error\nFunction\n(MSE)", color=CRED),
            CArrow(LEFT, color=CWHITE).scale(0.6),
            CText("Error", color=CRED),
        ).scale(0.8).arrange(RIGHT)

        p = Label("Parameters (weights and biases)", g1[0], UP, color=CWHITE).scale(0.8)
        t = Label("Target", g1[4], UP, color=CGREEN).scale(0.8)

        pre_arr = CArrow(LEFT, color=CWHITE).scale(0.8).next_to(g1, LEFT)
        pre = TextBox("Activation\nFunction\n(hidden)", color=CBLUE).scale(0.8).set_opacity(0.5).next_to(pre_arr, LEFT)
        pre_arr2 = CArrow(LEFT, color=CWHITE).scale(0.8).next_to(pre, LEFT).set_opacity(0.5)

        # self.add(g1, p, t, pre_arr, pre, pre_arr2)
        self.wait()
        self.play(Transform(f, g1[4]))
        self.play(Create(t))
        CreateBox(self,g1[2])
        self.play(Create(g1[5]), Create(g1[6]), Create(g1[3]))
        CreateBox(self,g1[0])
        self.play(Create(g1[1]))
        self.play(Create(p), run_time=1.5)
        CreateBox(self,pre)
        self.play(Create(pre_arr), Create(pre_arr2))
        self.wait(2)
 
class CompositionOfFunction(Scene):
    def construct(self):
        setup(self)

        g1 = VGroup(
            TextBox("Sum\nFunction\n(wx + b)", color=CWHITE, text_color=CBLACK),
            CArrow(LEFT, color=CWHITE).scale(0.6),
            TextBox("Activation\nFunction\n(output)", color=CBLUE),
            CArrow(LEFT, color=CWHITE).scale(0.6),
            TextBox("Error\nFunction\n(MSE)", color=CRED),
            CArrow(LEFT, color=CWHITE).scale(0.6),
            CText("Error", color=CRED),
        ).scale(0.8).arrange(RIGHT)

        p = Label("Parameters (weights and biases)", g1[0], UP, color=CWHITE).scale(0.8)
        t = Label("Target", g1[4], UP, color=CGREEN).scale(0.8)

        pre_arr = CArrow(LEFT, color=CWHITE).scale(0.8).next_to(g1, LEFT)
        pre = TextBox("Activation\nFunction\n(hidden)", color=CBLUE).scale(0.8).set_opacity(0.5).next_to(pre_arr, LEFT)
        pre_arr2 = CArrow(LEFT, color=CWHITE).scale(0.8).next_to(pre, LEFT).set_opacity(0.5)

        g2 = VGroup(g1, p, t, pre_arr, pre, pre_arr2)
        self.add(g2)
        self.wait()
        self.play(g2.animate.shift(UP*1.5))
        self.wait(2)

        com = CText("Composition of Functions: f(g(x))", color=CWHITE).scale(1.5)

        self.play(Create(com))
        self.wait()

        ff = VGroup(
            MathTex(r"MSE(", color=CRED),
            MathTex(r"\sigma_{\texttt{out1}}(", color=CBLUE),
            MathTex(r"\texttt{Sum}(\sigma_{\texttt{h5}}(...), w_{\texttt{out1}}, b_{\texttt{out1}})", color=CWHITE),
            MathTex(r"),...", color=CBLUE),
            MathTex(r",\hat{y}", color=CGREEN),
            MathTex(r")", color=CRED),
        ).scale(0.8).arrange(RIGHT, buff=0.1).shift(DOWN)

        self.play(Create(ff))
        self.wait()

class Backpropagation(Scene):
    def construct(self):
        setup(self)

        

