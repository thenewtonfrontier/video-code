from manim import *

class Limit(Scene):
    def construct(self):

        eq1 = MathTex(
            r"\lim_{x \to 0} \frac{ln(1-x)-sinx}{1-cos^2x}"
        )
        eq2 = MathTex(
            r"\lim_{x \to 0} \frac{0-0}{1-1}"
        )
        eq3 = MathTex(
            r"\lim_{x \to 0} \frac{0}{0} = ???"
        )
        text = Text(
            "L'Hôpital's Rule"
        )
        eq4 = MathTex(
            r"\lim_{x \to c} \frac{f(x)}{g(x)} = \lim_{x \to c} \frac{f'(x)}{g'(x)}"
        )
        eq5 = MathTex(
            r"\lim_{x \to 0} \frac{ln(1-x)-sinx}{1-cos^2x}"
        )
        eq6 = MathTex(
            r"sin^2x = 1 - cos^2x"
        )
        eq7 = MathTex(
            r"\lim_{x \to 0} \frac{ln(1-x)-sinx}{sin^2x}"
        )
        eq8 = MathTex(
            r"\lim_{x \to 0} \frac{\frac{-1}{1-x}-cosx}{2sinxcosx}"
        )
        eq9 = MathTex(
            r"\lim_{x \to 0} \frac{-1-1}{2(0)(1)}"
        )
        eq10 = MathTex(
            r"\lim_{x \to 0} \frac{-2}{0}"
        )
        eq11 = MathTex(
            r"\lim_{x \to 0^-} \frac{-2}{-0.0000000001...}"
        )
        eq12 = MathTex(
            r"\lim_{x \to 0^-} \frac{-2}{-0.0000000001...}=\infty "
        )
        eq13 = MathTex(
            r"\lim_{x \to 0^+} \frac{-2}{0.0000000001...}"
        )
        eq14 = MathTex(
            r"\lim_{x \to 0^+} \frac{-2}{0.0000000001...}=-\infty"
        )
        eq15 = MathTex(
            r"\lim_{x \to 0^-}\not= \lim_{x \to 0^+}"
        )
        DNE = Text(
            "DNE"
        )
        
        eq6.to_corner(DOWN)
        eq12.to_corner(DOWN)
        eq14.to_corner(DOWN)
        g1 = VGroup(eq1, eq2, eq3)
        g2 = VGroup(eq5, eq7)
        g3 = VGroup(eq5, eq7, eq8)
        g4 = VGroup(eq9, eq10)
        g5 = VGroup(eq11, eq12)
        g6 = VGroup(eq13, eq14)
        

        self.wait(2)
        self.play(Create(eq1))
        self.wait(11)
        self.play(eq1.animate(run_time = 2).to_corner(UP))
        self.wait(5)
        self.play(Create(eq2))
        self.wait(2)
        self.play(Transform(eq2, eq3))
        self.wait(2)
        self.play(FadeOut(g1, shift = UP))
        self.wait(8)
        self.play(Create(text))
        self.wait(2)
        self.play(FadeOut(text, shift = DOWN))
        self.wait(2)
        self.play(Create(eq4))
        self.wait(14)
        self.play(FadeOut(eq4, shift = UP))
        self.wait(2)
        self.play(Create(eq5))
        self.wait(8)
        self.play(Create(eq6))
        self.wait(2)
        self.play(FadeOut(eq6, shift = DOWN), Transform(eq5, eq7))
        self.wait(24)
        self.play(Transform(g2, eq8))
        self.wait(2)
        self.play(g3.animate(run_time = 2).to_corner(UP))
        self.wait(8)
        self.play(Create(eq9))
        self.wait(2)
        self.play(Transform(eq9, eq10))
        self.wait(7)
        self.play(FadeOut(g4, shift = DOWN))
        self.wait(2)
        self.play(Create(eq11))
        self.wait(11)
        self.play(Create(eq12))
        self.wait(2)
        self.play(FadeOut(g5, shift = DOWN))
        self.wait(14)
        self.play(Create(eq13))
        self.wait(2)
        self.play(Create(eq14))
        self.wait(2)
        self.play(FadeOut(g6, shift = DOWN))
        self.wait(2)
        self.play(Create(eq15))
        self.wait(2)
        self.play(FadeOut(g3, shift = UP), FadeOut(eq15, shift = DOWN))
        self.wait(11)
        self.play(Create(DNE))
        self.wait(2)
        self.play(FadeOut(DNE, shift = DOWN))
        self.wait(2)