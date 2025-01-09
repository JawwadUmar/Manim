from manim import *

class Project1(Scene):
    def construct(self):
        a = axes = Axes(
            x_range=(-12, 12, 1),
            y_range=(0, 14, 1),
        )

        axes.add_coordinates()

        quadratic = a.plot(lambda x: x*x-3*x+9, color = BLUE)
        linear = a.plot(lambda x: 2*x +3, color = RED)

        quadratic_equation_label = MathTex("y = x^2 - 3x + 9", color=WHITE)
        quadratic_equation_label.to_corner(UL)

        self.play(FadeIn(quadratic_equation_label))
        self.play(Create(axes, run_time = 3))
        self.play(Write(quadratic, run_time = 3))
        
        linear_equation_label = MathTex("y = 2x + 3", color=WHITE)
        linear_equation_label.next_to(quadratic_equation_label, DOWN)
        self.play(FadeIn(linear_equation_label))
        self.play(Write(linear, run_time = 3))



