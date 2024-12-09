from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_height = 16.0  # Aspect ratio height
config.frame_width = 9.0    

class HighlightLHSHRS(MovingCameraScene):
    def construct(self):

        logo = ImageMobject("logo.png")
        logo.move_to(ORIGIN)  # Center the logo
        logo.set_opacity(0.1)
        self.add(logo)
        # Define the equation
        equation = MathTex("x^2 - 3x + 9", "=", "2x + 3")
        equation.scale(1.5)  # Scale up for visibility
        self.play(Write(equation))
        self.wait(1)

        # Curly braces for LHS and RHS
        lhs_brace = Brace(equation[0], UP, color=YELLOW)
        rhs_brace = Brace(equation[2], UP, color=GREEN)

        # Labels under LHS and RHS
        lhs_label = lhs_brace.get_text("LHS")
        rhs_label = rhs_brace.get_text("RHS")

        # Animate braces and labels
        self.play(
            Create(lhs_brace),
            Write(lhs_label)
        )
        self.wait(0.5)

        self.play(
            Create(rhs_brace),
            Write(rhs_label)
        )
        self.wait(1)

        # Fade out braces and labels
        self.play(
            FadeOut(lhs_brace, lhs_label),
            FadeOut(rhs_brace, rhs_label)
        )

        equation.scale(0.75)
        self.play(equation.animate.to_edge(UP + LEFT, buff=1.5), run_time=2)
        
        equation[0].set_color(GREEN)
        
        quadratic_equation_label = MathTex("y = x^2 - 3x + 9", color=GREEN)
        quadratic_equation_label.scale(1.2)
        quadratic_equation_label.next_to(equation, DOWN, buff=1)

        self.play(
            Write(quadratic_equation_label)
        )

        rectangle2 = SurroundingRectangle(quadratic_equation_label, color=WHITE, buff=0.2)
        self.play(Create(rectangle2))

        equation[2].set_color(RED)
        linear_equation_label = MathTex("y = 2x + 3", color=RED)
        linear_equation_label.scale(1.2)
        linear_equation_label.next_to(quadratic_equation_label, DOWN, buff=0.8)

        self.play(
            Write(linear_equation_label)
        )

        rectangle1 = SurroundingRectangle(linear_equation_label, color=WHITE, buff=0.2)
        self.play(Create(rectangle1))

        self.play(
            FadeOut(equation)
        )

        group = VGroup(quadratic_equation_label, rectangle2, linear_equation_label, rectangle1)
        self.play(
            group.animate.to_edge(UP + LEFT, buff=1),
            run_time=2
        )
        

        a = axes = Axes(
            x_range=(-12, 12, 1),
            y_range=(0, 14, 1),
        )
        a.scale(1.5)
        axes.add_coordinates()
        a.move_to(ORIGIN + DOWN*2)

        quadratic = a.plot(lambda x: x*x-3*x+9, color = GREEN)

        # quadratic = quadratic.copy().clip_to_rectangle(axes.get_top() + DOWN * 2, axes.get_bottom() + UP * 2)
        # quadratic = axes.plot(lambda x: np.clip(x*x - 3*x + 9, 0, 25), color=GREEN)
        linear = a.plot(lambda x: 2*x +3, color = RED)

        self.play(Create(axes, run_time = 1))

        self.play(Write(quadratic, run_time = 3))
        self.play(Write(linear, run_time = 3))

        point1 = Dot(axes.c2p(2, 7), color=YELLOW)
        point1_label = MathTex("(2,7)")
        point1_label.next_to(point1, RIGHT)


        point2 = Dot(axes.c2p(3, 9), color=YELLOW)
        point2_label = MathTex("(3,9)")
        point2_label.next_to(point2, RIGHT)

        point_group = VGroup(point1, point2, point1_label, point2_label)

        self.play(
            Create(point1),
            Write(point1_label),

            Create(point2),
            Write(point2_label)
        )

        self.camera.frame.save_state()

        self.play(
            self.camera.frame.animate.set(width = point_group.width*2).move_to(point_group),
        )


        self.wait(3)
