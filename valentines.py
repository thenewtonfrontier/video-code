from manim import *
import math

class Heart(Scene):
    def construct(self):

        text = Text(
            "Cartesian Coordinate System"
        )
        eq1 = MathTex(
            r"f(x) = \sqrt{2 \cdot \sqrt{x^2} - x^2}"
        )
        eq2 = MathTex(
            r" g(x) = -2.14\sqrt{\sqrt{2} - \sqrt{\left| x \right|}}"
        )
        axes = Axes(
            x_range = [-3, 3, 1],
            y_range = [-4, 4, 1],
            x_axis_config = {"numbers_with_elongated_ticks": np.arange(-2, 2, 1)},
            x_length = 6,
            tips = True,
        )
        func1 = axes.plot(lambda x: math.sqrt(2 * math.sqrt(x ** 2) - x **2), x_range = [-2, 2], color = PINK)
        func2 = axes.plot(lambda x: -2.14 * math.sqrt(math.sqrt(2) - math.sqrt(abs(x))), x_range = [-2, 2], color = PINK)

        graph = VGroup(axes, func1, func2)
        eq1.to_corner(LEFT)
        eq2.to_corner(RIGHT)

        self.wait(2)
        self.play(Create(text))
        self.wait(5)
        self.play(FadeOut(text, shift = DOWN))
        self.wait(2)
        self.play(Create(eq1))
        self.play(Create(eq2))
        self.wait(11)
        self.play(FadeOut(eq1, shift = LEFT), FadeOut(eq2, shift = RIGHT))
        self.wait(2)
        self.play(Create(axes))
        self.play(Create(func1))
        self.play(Create(func2))
        self.wait(19)
        self.play(FadeOut(graph, shift = DOWN))
        self.wait(2)


class HeartPolar(Scene):
    def construct(self):
        
        text = Text(
            "Polar Coordinate System"
        )
        eq1 = MathTex(
            r"r = \frac{sin(t)\sqrt{\left| cos(t) \right|}}{sin(t) + \frac{7}{5}} - 2sin(t) + 2"
        )
        domain = MathTex(
            r"\left[ -\pi , \pi\right]"
        )
        e = ValueTracker(-3.14)
        plane = PolarPlane()
        func1 = always_redraw(lambda : 
        ParametricFunction(lambda t: plane.polar_to_point(np.sin(t) * math.sqrt(abs(np.cos(t))) / (np.sin(t) + (7/5)) - 2 * np.sin(t) + 2, t),
        t_range = [-PI, e.get_value()],
        color = PINK)
        )
        dot1 = always_redraw(lambda : Dot(fill_color = RED, fill_opacity = 0.8).scale(0.5).move_to(func1.get_end()))

        eqs = VGroup(eq1, domain)
        domain.to_corner(DOWN)
        graph = VGroup(plane, func1)

        self.wait(2)
        self.play(Create(text))
        self.wait(11)
        self.play(FadeOut(text, shift = DOWN))
        self.wait(6)
        self.play(Create(eq1))
        self.play(Create(domain))
        self.wait(4)
        self.play(FadeOut(eqs, shift = DOWN))
        self.wait(6)
        self.play(LaggedStart(Write(plane)))
        self.add(func1, dot1)
        self.play(e.animate.set_value(PI), run_time = 3, rate_func = linear)
        self.remove(dot1)
        self.wait(7)
        self.play(FadeOut(graph, shift = DOWN))
        self.wait(2)

class VS(Scene):
    def construct(self):

        text = Text(
            "Polar vs. Cartesian"
        )

        self.wait(2)
        self.play(Create(text))
        self.wait(7)
        self.play(FadeOut(text, shift = DOWN))

class image(Scene):
    def construct(self):
        plane = PolarPlane()
        func1 = always_redraw(lambda : 
        ParametricFunction(lambda t: plane.polar_to_point(np.sin(t) * math.sqrt(abs(np.cos(t))) / (np.sin(t) + (7/5)) - 2 * np.sin(t) + 2, t),
        t_range = [-PI, PI],
        color = PINK)
        )

        self.add(plane)
        self.add(func1)
