from manim import *

class Revolution(ThreeDScene):
    def construct(self):

        #constructs axes
        axes = ThreeDAxes()

        #creates initial 1/x graph
        g1 = axes.plot(lambda x: 1/x, x_range = [0.1, 10], color = BLUE_D)
        g2 = axes.plot(lambda x : 1/x, x_range = [-10, -0.1], color = BLUE_D)
        func = VGroup(g1, g2)
        g3 = axes.plot(lambda x: 1/x, x_range = [1, 10], color = BLUE_D)

        #creates parametric surface
        surface = ParametricSurface(
             lambda u, v: np.array([
                u, (1/u)*np.cos(v), (1/u)*np.sin(v)
            ]),
            u_range = [1, 10],
            v_range = [0, 0.001],
            checkerboard_colors = [BLUE_B, BLUE_D],
            fill_color = BLUE_D,
            stroke_color = BLUE_D
        )

        #plays animation
        self.wait(4)
        self.play(Write(axes))
        self.wait(4)
        self.play(Write(func))
        self.wait(4)
        self.play(Uncreate(g1), Uncreate(g2), Write(g3))
        self.wait()
        self.move_camera(0.8 * np.pi/2, -0.45 * np.pi)
        self.remove(g3)
        self.play(Write(surface))
        self.begin_ambient_camera_rotation(rate = 0.04)
        self.play(
            UpdateFromAlphaFunc(surface, self.update_surface),
            rate_func=linear,
            run_time=2
        )
        self.wait(5)
        self.play(Uncreate(axes))
        self.play(surface.animate(run_time = 2).center())
        self.wait(5)
        self.stop_ambient_camera_rotation()
        self.wait(5)
        self.play(FadeOut(surface, shift = DOWN))

    #static function which revolves parametric surface
    def update_surface(self, c, dt):
        a = interpolate(0.1, 2*PI, dt)
        s = ParametricSurface(
            lambda u, v: np.array([
                u, (1/u)*np.cos(v), (1/u)*np.sin(v)
            ]),
            u_range = [1, 10],
            v_range = [0, a],
            checkerboard_colors=[BLUE_B, BLUE_D],
            color = BLUE_D,
            fill_color = BLUE_D,
        )
        c.become(s)

class VolumeProof(Scene):
    def construct(self):
        
        #opening heading
        header = Tex("Volume Of Gabriel's Horn")
        transform_header = Tex("Volume:")

        #creates circle with radius
        circle = Circle(3, stroke_color = BLUE_D, fill_color = BLUE_B, fill_opacity = 0.4)
        radius = Line(
            start = circle.get_center(), 
            end =circle.get_top(), 
            stroke_color = BLUE_D, 
            stroke_width = 5
        )
        radiustext = MathTex(
            r"r = \frac{1}{x}"
        )

        #declares LaTeX equations
        equation1 = MathTex(
            r'V &= \int_{a}^{b}\pi r^{2}dx'
        )
        equation2 = MathTex(
            r'&=\int_{1}^{\infty}\pi (\frac{1}{x})^{2}dx'
        )
        equation3 = MathTex(
            r'&=\lim_{b \to \infty} \int_{1}^{b}\pi(\frac{1}{x})^{2}dx'
        )
        equation4 = MathTex(
            r'&=\pi\lim_{b \to \infty} \int_{1}^{b}(\frac{1}{x})^{2}dx'
        )
        equation5 = MathTex(
            r'&=\pi\lim_{b \to \infty}\left[ \frac{-1}{x} \right]_{1}^{b}'
        )
        equation6 = MathTex(
            r'&=\pi\left[ \frac{-1}{x} \right]_{1}^{\infty}'
        )
        equation7 = MathTex(
            r'&=\pi\left( 1 -\frac{1}{\infty} \right)'
        )
        equation8 = MathTex(
            r'V &=\pi'
        )

        #creates VGroups for animation
        firsteq = VGroup(equation1, equation2)
        secondeq = VGroup(equation3, equation4, equation5, equation6)
        drawing = VGroup(circle, radius)

        #positioning text
        transform_header.to_corner(UP + LEFT)
        equation4.to_corner(UP)
        equation3.to_corner(DOWN)
        equation7.to_corner(DOWN)
        radiustext.next_to(drawing, LEFT)

        #plays animation
        self.play(Write(header), run_time = 2)
        self.wait(3)
        self.play(Transform(header, transform_header))
        self.wait()
        self.play(Create(circle))
        self.wait()
        self.play(Create(radius), run_time = 1.5)
        self.play(Create(radiustext))
        self.wait()
        self.play(FadeOut(drawing, shift = DOWN))
        self.play(radiustext.animate(run_time = 2).to_corner(LEFT))
        self.wait(4)
        self.play(Create(equation1))
        self.wait(1)
        self.play(equation1.animate(run_time = 2).to_corner(UP))
        self.wait(1)
        self.play(Create(equation2))
        self.wait(2)
        self.play(Create(equation3))
        self.wait(2)
        self.play(FadeOut(firsteq, shift = UP), FadeOut(radiustext, shift = LEFT))
        self.wait(1)
        self.play(Transform(equation3, equation4))
        self.wait(2)
        self.play(Create(equation5))
        self.wait(2)
        self.play(Transform(equation5, equation6))
        self.wait(2)
        self.play(Create(equation7))
        self.wait(2)
        self.play(FadeOut(secondeq, shift = UP))
        self.wait(2)
        self.play(Transform(equation7, equation8))
        self.wait(2)
    
class SurfaceArea(Scene):
    def construct(self):

        #opening heading
        header = Tex("Surface Area Of Gabriel's Horn")
        transform_header = Tex("Surface Area:")

        #declares LaTeX equations
        equation1 = MathTex(
            r"SA = \int_{b}^{a}\pi f(x)\sqrt[]{1 + [f'(x)]^2}dx"
        )
        equation2 = MathTex(
            r"&= \int_{1}^{\infty}2\pi(\frac{1}{x})\sqrt[]{1 +[-\frac{1}{x^2}]^2}dx"
        )
        equation3 = MathTex(
            r"&= \int_{1}^{\infty}2\pi(\frac{1}{x})\sqrt[]{1 +\frac{1}{x^4}}dx"
        )
        equation4 = MathTex(
            r" &= ???"
        )
        equation5 = MathTex(
            r"\text{Domain }f(x) = [1, \infty]"
        )
        equation6 = MathTex(
            r"\int_{1}^{\infty}\frac{1}{x}dx=\infty"
        )
        equation7 = MathTex(
            r"(\frac{1}{x})\sqrt[]{1 +\frac{1}{x^4}} > \frac{1}{x} \text{ on } [1, \infty]"
        )
        equation8 = MathTex(
            r"\int_{1}^{\infty}(\frac{1}{x})\sqrt[]{1 +\frac{1}{x^4}}dx =\infty"
        )
        equation9 = MathTex(
            r"&= 2\pi\int_{1}^{\infty}(\frac{1}{x})\sqrt[]{1 +\frac{1}{x^4}}dx"
        )
        equation10 = MathTex(
            r"&= 2\pi\infty"
        )
        equation11 = MathTex(
            r"SA &= \infty"
        )

        #creates VGroups for animation
        firsteq = VGroup(equation2, equation3)
        secondeq = VGroup(equation6, equation7, equation8)
        thirdeq = VGroup(equation2, equation3, equation9)
        fourtheq = VGroup(equation2, equation3, equation9, equation10)

        #positioning text
        transform_header.to_corner(UP + LEFT)
        equation4.to_corner(DOWN)
        equation5.to_corner(LEFT)
        equation7.to_corner(DOWN)
        equation9.to_corner(UP)
        equation10.to_corner(UP)

        #plays animation
        self.play(Write(header), run_time = 2)
        self.wait(2)
        self.play(Transform(header, transform_header))
        self.wait(2)
        self.play(Create(equation1))
        self.wait(2)
        self.play(equation1.animate(run_time = 2).to_corner(UP))
        self.play(Create(equation2))
        self.wait(2)
        self.play(Transform(equation2, equation3))
        self.wait(2)
        self.play(Create(equation4))
        self.wait(2)
        self.play(FadeOut(equation1, shift = UP), FadeOut(equation4, shift = DOWN))
        self.play(firsteq.animate(run_time = 2).to_corner(UP))
        self.wait(2)
        self.play(Create(equation5))
        self.wait(2)
        self.play(Create(equation6))
        self.wait(2)
        self.play(FadeOut(equation5, shift = LEFT))
        self.play(Create(equation7))
        self.wait(2)
        self.play(Transform(equation6, equation8))
        self.wait(2)
        self.play(Transform(firsteq, equation9))
        self.wait(2)
        self.play(FadeOut(secondeq, shift = DOWN))
        self.wait(2)
        self.play(Transform(thirdeq, equation10))
        self.wait(2)
        self.play(FadeOut(fourtheq, shift = UP), Create(equation11))
        self.wait(2)

class VolumeAndSurface(Scene):
    def construct(self):

        #opening heading
        header = Text("Volume And Surface Area of Gabriel's Horn")
        
        #declares LaTeX equations
        equation1 = MathTex(
            r"V &= \pi"
        )
        equation2 = MathTex(
            r"SA &= \infty"
        )

        #creates text question and paradox text
        question = Text("wait what?")
        paradox = Text("Painter's Paradox")

        #positioning text
        header.to_corner(UP)
        equation1.to_corner(LEFT)
        equation2.to_corner(RIGHT)

        #plays animation
        self.wait(2)
        self.play(Create(header))
        self.wait(2)
        self.play(Create(equation1))
        self.wait(2)
        self.play(Create(equation2))
        self.wait(4)
        self.play(Create(question))
        self.wait(3)
        self.play(FadeOut(equation1, shift = LEFT), FadeOut(equation2, shift = RIGHT), FadeOut(header, shift = UP), FadeOut(question, shift = DOWN))
        self.wait(2)
        self.play(Create(paradox))
        self.wait(4)
        self.play(FadeOut(paradox, shift = DOWN))
        self.wait(2)
