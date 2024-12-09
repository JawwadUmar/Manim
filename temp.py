from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_height = 16.0  # Aspect ratio height
config.frame_width = 9.0    

class SolveQuadraticEquation(Scene):
    def construct(self):
        logo = ImageMobject("logo.png")
        logo.move_to(ORIGIN)  # Center the logo
        logo.set_opacity(0.1)
        self.add(logo)
        

        title = Title("Solving an Equation")
        self.add(title)

        # Step 1: Create each line of math steps
        equation = MathTex("x^2 - 3x + 9", "=", "2x + 3")
        step1 = MathTex("x^2 - 3x - 2x + 9 - 3", "= 0")
        step2 = MathTex("x^2 - 5x + 6", "= 0")
        step3 = MathTex("(x - 2)(x - 3)", "= 0")
        step4 = MathTex("x - 2 = 0", "\\,\\,\\text{or}\\,\\,", "x - 3 = 0")
        step5 = MathTex("x = 2", "\\,\\,\\text{or}\\,\\,", "x = 3")

        # Step 2: Arrange all steps vertically
        steps_group = VGroup(
            equation,
            step1,
            step2,
            step3,
            step4,
            step5
        ).arrange(DOWN, center=True, aligned_edge=LEFT, buff=0.8)

        # Step 3: Play the animations for each step
        for step in steps_group:
            self.play(Write(step))
            self.wait(1)

        # Step 4: Highlight the final solution
        box = SurroundingRectangle(step5, color=YELLOW)
        self.play(Create(box))
        self.wait(1)

        # Fade out at the end
        self.play(FadeOut(box))
        self.wait(1)