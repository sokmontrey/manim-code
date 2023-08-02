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
FONT_SIZE = 18

def CreateBox(self, tb):
    center = tb.get_center()
    circle = RoundedRectangle(width=0.01, height=0.01, corner_radius=0.01, color=tb[0].get_color())

    self.add(circle)
    self.play(ReplacementTransform(circle, tb[0]))
    self.play(Create(tb[1]))

def Panel(obj, color=CWHITE, corner=0.2):
    return SurroundingRectangle(obj, color=color, buff=0.2, corner_radius=corner)

def CText(text, color=CWHITE, font_size=FONT_SIZE):
    t = Text(text, color=color, font_size=font_size, font=FONT_R)
    return t

def TextBox(text,color=CBLUE,text_color=CWHITE, text_size=FONT_SIZE, fill_opacity=1, corner=0):
    t = CText(text, text_color, text_size)
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
    arr = CArrow(direction, color, oppo).next_to(obj, direction, 0.8)
    t = CText(text, color, text_size).next_to(arr, direction)

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
        self.play(graph.animate.move_to([0.87,-1,0]), ChangeDecimalToValue(bv, 1), run_time=1.5)
        self.play(graph.animate.move_to([-0.87,-1,0]), ChangeDecimalToValue(bv, -1),run_time=1.5)
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

def LB(color=CWHITE):
    return MathTex(r"\left[\begin{matrix} \, \\ \, \end{matrix}\right.", color=color)
def RB(color=CWHITE):
    return MathTex(r"\left.\begin{matrix} \, \\ \, \end{matrix}\right]", color=color)
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

