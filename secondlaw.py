from manim import *

class Falling(Scene):
    def construct(self):

        circle = Circle(.5, stroke_color = BLUE_D, fill_color = BLUE_B, fill_opacity = 0.4)
        arrow1 = Arrow(start = UP, end = DOWN)
        ground = Line(5 * LEFT, 5 * RIGHT)
        mass = MathTex(
            r"m = 2kg"
        )
        height = MathTex(
            r"y = 10m"
        )
        force = MathTex(
            r"\overrightarrow{F}_{g} = ?"
        )
        constantg = MathTex(
            r"\overrightarrow{a} = g = -9.81m/s^2"
        )
        eq1 = MathTex(
            r"\overrightarrow{F}_{net} =m\overrightarrow{a}"
        )
        eq2 = MathTex(
            r"\overrightarrow{F}_g =mg"
        )
        eq3 = MathTex(
            r"\overrightarrow{F}_g =2kg \cdot -9.81m/s^2"
        )
        eq4 = MathTex(
            r"\overrightarrow{F}_g = -19.62N"
        )
        text = Tex(
            "but why?"
        )

        diagram = VGroup(circle, arrow1, ground, height, mass, force)
        group1 = VGroup(eq1, eq2)
        group2 = VGroup(eq1, eq2, eq3)
        group3 = VGroup(eq1, eq2, eq3, eq4)

        ground.shift(DOWN * 2.5)
        circle.to_corner(UP)
        mass.next_to(ground, DOWN)
        arrow1.next_to(circle, DOWN)
        force.next_to(arrow1, DOWN)
        height.to_corner(LEFT)
        constantg.to_corner(DOWN)

        self.wait(5)
        self.play(Create(ground))
        self.play(Create(circle))
        self.play(Create(mass))
        self.play(Create(height))
        self.wait(2)
        self.play(Create(arrow1))
        self.play(Create(force))
        self.wait(2)
        self.play(FadeOut(diagram, shift = DOWN))
        self.wait(2)
        self.play(Create(eq1))
        self.wait(2)
        self.play(Create(constantg))
        self.wait(7)
        self.play(FadeOut(constantg, shift = DOWN), Transform(eq1, eq2))
        self.wait(2)
        self.play(Transform(group1, eq3))
        self.wait(2)
        self.play(Transform(group2, eq4))
        self.wait(2)
        self.play(FadeOut(group3, shift = DOWN))
        self.wait(2)
        self.play(Create(text))
        self.wait(2)
        self.play(FadeOut(text, shift = DOWN))
        self.wait(2)

class NewtonProof(Scene):
    def construct(self):

        lawtext = Tex(
            "Newton's Second Law"
        )
        law1 = MathTex(
            r"\overrightarrow{F}_{net} \propto  \frac{\Delta \overrightarrow{p}}{\Delta t}"
        )
        law2 = MathTex(
            r"\overrightarrow{F}_{net} \propto  \frac{m(\overrightarrow{v_f} - \overrightarrow{v_i})}{\Delta t}"
        )
        law3 = MathTex(
            r"\overrightarrow{F}_{net} \propto  m\overrightarrow{a}"
        )
        law4 = MathTex(
            r"\overrightarrow{F}_{net} =  km\overrightarrow{a}"
        )
        law5 = MathTex(
            r"\overrightarrow{F}_{net} =  m\overrightarrow{a}"
        )

        group1 = VGroup(law1, law2)
        group2 = VGroup(law1, law2, law3)
        group3 = VGroup(law1, law2, law3, law4)
        group4 = VGroup(law1, law2, law3, law4 ,law5)

        self.wait(2)
        self.play(Create(lawtext))
        self.wait(2)
        self.play(lawtext.animate(run_time = 2).to_corner(UP))
        self.wait(2)
        self.play(Create(law1))
        self.wait(4)
        self.play(Transform(law1, law2))
        self.wait(6)
        self.play(Transform(group1, law3))
        self.wait(4)
        self.play(Transform(group2, law4))
        self.wait(4)
        self.play(Transform(group3, law5))
        self.wait(4)
        self.play(FadeOut(group4, shift = DOWN), FadeOut(lawtext, shift = UP))
        self.wait(2)

class LagrangianProof(Scene):
    def construct(self):

        text1 = Text(
            "Lagrangian Mechanics"
        )
        circle = Circle(.5, stroke_color = BLUE_D, fill_color = BLUE_B, fill_opacity = 0.4)
        arrow1 = Arrow(start = UP, end = DOWN)
        ground = Line(5 * LEFT, 5 * RIGHT)
        mass = MathTex(
            r"m = 2kg"
        )
        height = MathTex(
            r"y = 10m"
        )
        force = MathTex(
            r"\overrightarrow{F}_{g} = ?"
        )
        lagrange1 = MathTex(
            r"\mathscr{L} = KE - PE"
        )
        lagrange2 = MathTex(
            r"\mathscr{L} = T - V"
        )
        KE = MathTex(
            r"T = \frac{1}{2}m\dot{y}^2"
        )

        PE = MathTex(
            r"V = mgy"
        )
        lagrange3 = MathTex(
            r"\mathscr{L} = \frac{1}{2}m\dot{y} - mgy"
        )
        eulerlagrange = MathTex(
            r"\frac{d }{dt}\frac{\partial\mathscr{L}}{\partial\dot{y}} - \frac{\partial\mathscr{L}}{\partial y} = 0"
        )
        partial1 = MathTex(
            r"\frac{\partial\mathscr{L}}{\partial y} = 0 - mg"
        )
        partial2 = MathTex(
            r"\frac{d }{dt}\frac{\partial\mathscr{L}}{\partial\dot{y}} = \frac{d}{dt}(m\dot{y} - 0)"
        )
        partial3 = MathTex(
            r"\frac{d }{dt}\frac{\partial\mathscr{L}}{\partial\dot{y}} = m\ddot{y}"
        )
        lagrange4 = MathTex(
            r"m\ddot{y} + mg = 0"
        )
        lagrange5 = MathTex(
            r"\overrightarrow{F}_{net} + mg = 0"
        )
        lagrange6 = MathTex(
            r"\overrightarrow{F}_g = -mg"
        )
        lagrange7 = MathTex(
            r"\overrightarrow{F}_g = -2kg \cdot -9.81m/s^2 "
        )
        lagrange8 = MathTex(
            r"\overrightarrow{F}_g = -19.62N "
        )
        text2 = Text(
            "so what?"
        )

        diagram = VGroup(circle, arrow1, ground, height, mass, force)
        group1 = VGroup(lagrange1, lagrange2)
        group2 = VGroup(KE, PE)
        group3 = VGroup(lagrange1, lagrange2, lagrange3, eulerlagrange)
        group4 = VGroup(partial2, partial3)
        group5 = VGroup(lagrange5)
        group6 = VGroup(lagrange5, lagrange6)
        group7 = VGroup(lagrange5, lagrange6, lagrange7)


        ground.shift(DOWN * 2.5)
        circle.to_corner(UP)
        mass.next_to(ground, DOWN)
        arrow1.next_to(circle, DOWN)
        force.next_to(arrow1, DOWN)
        height.to_corner(LEFT)
        lagrange1.to_corner(UP)
        lagrange2.to_corner(UP)
        PE.to_corner(DOWN)
        lagrange3.to_corner(UP)
        partial1.to_corner(RIGHT)
        partial2.to_corner(LEFT)
        partial3.to_corner(LEFT)
        lagrange4.to_corner(DOWN)


        self.wait(2)
        self.play(Create(text1))
        self.wait(2)
        self.play(FadeOut(text1, shift = DOWN))
        self.wait(2)
        self.play(Create(diagram))
        self.wait(3)
        self.play(FadeOut(diagram, shift = DOWN))
        self.wait(2)
        self.play(Create(lagrange1))
        self.wait(3)
        self.play(Transform(lagrange1, lagrange2))
        self.wait(3)
        self.play(Create(KE))
        self.play(Create(PE))
        self.wait(17)
        self.play(Transform(group1, lagrange3), FadeOut(group2, shift = DOWN))
        self.wait(2)
        self.play(Create(eulerlagrange))
        self.wait(15)
        self.play(Create(partial1))
        self.wait(2)
        self.play(Create(partial2))
        self.wait(2)
        self.play(Transform(partial2, partial3))
        self.wait(19)
        self.play(Create(lagrange4))
        self.wait(2)
        self.play(FadeOut(group3, shift = UP), FadeOut(group4, shift = LEFT), FadeOut(partial1, shift = RIGHT))
        self.play(lagrange4.animate(run_time = 2).to_corner(UP))
        self.wait(2)
        self.play(Create(lagrange5))
        self.wait(2)
        self.play(Transform (group5, lagrange6), FadeOut(lagrange4, shift = UP))
        self.wait(2)
        self.play(Transform(group6, lagrange7))
        self.wait(2)
        self.play(Transform(group7, lagrange8))
        self.wait(6)
        self.play(FadeOut(group7, shift = DOWN), FadeOut(lagrange8, shift = DOWN))
        self.wait(2)
        self.play(Create(text2))
        self.wait(2)
        self.play(FadeOut(text2, shift = DOWN))
        self.wait(2)

class Bigger(Scene):
    def construct(self):

        text = Text(
            "The Bigger Picture"
        )

        self.wait(2)
        self.play(Create(text))
        self.wait(2)
        self.play(FadeOut(text, shift = DOWN))

class ImageEuler(Scene):
    def construct(self):

        eulerlagrange = MathTex(
            r"\frac{d }{dt}\frac{\partial\mathscr{L}}{\partial\dot{y}} - \frac{\partial\mathscr{L}}{\partial y} = 0"
        )

        self.add(eulerlagrange)

class ImageNewton(Scene):
    def construct(self):

        law5 = MathTex(
            r"\overrightarrow{F}_{net} =  m\overrightarrow{a}"
        )

        self.add(law5)   