from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_height = 16.0  # Aspect ratio height
config.frame_width = 9.0 

class DrawTriangle(MovingCameraScene):
    def construct(self):
        
        title = Title("Can you solve this ?")
        title.move_to(DOWN*2)
        self.add(title)

        problemDescripton = Text(
            "ABC is a triangle in which ∠B = 2∠C.\n"
            "D is a point on BC such that AD bisects ∠BAC,\n"
            "and AB = CD.\nFind ∠BAC.", font_size=36, width=7
        )

        self.add(problemDescripton)
        self.wait(2)

        

        self.play(
            problemDescripton.animate.move_to(UP*3),
            FadeOut(title)
        )

        logo = ImageMobject("logo.png")
        logo.move_to(ORIGIN)  # Center the logo
        logo.set_opacity(0.1)
        self.add(logo)

        
        angle_A = 72  # degrees
        angle_B = 72  # degrees
        angle_C = 36  # degrees

        #Base is BC
        BC = 6

        # Calculate the other points using trigonometry
        B = np.array([0, 0, 0])  # Point B at the origin
        C = np.array([BC, 0, 0])  # Point C on the x-axis

        # Calculate coordinates of A
        angle_B_rad = np.radians(angle_B)
        angle_C_rad = np.radians(angle_C)

        # Height and horizontal offset of point A
        height = (BC * np.tan(angle_B_rad) * np.tan(angle_C_rad))/(np.tan(angle_B_rad) + np.tan(angle_C_rad))
        offset = height/np.tan(angle_B_rad)

        A = np.array([offset, height, 0])  # Point A

        AB = np.linalg.norm(A-B)
        AC = np.linalg.norm(A-C)

        BD = (AB*BC)/(AB + AC)
        

        D = np.array([BD, 0, 0])

        Ex = (AB*C[0] + BC*A[0])/(AB+BC)
        Ey = (AB*C[1] + BC*A[1])/(AB+BC)

        E = np.array([Ex, Ey, 0])

        # Create the triangle
        # triangle = Polygon(
        #     A, B, C, color=WHITE
        # ).set_fill(TEAL, opacity=0.5)
        triangle = Polygon(
            A, B, C, color=WHITE
        )


        # Add labels
        label_A = MathTex("A").next_to(A, UP)
        label_B = MathTex("B").next_to(B, LEFT)
        label_C = MathTex("C").next_to(C, RIGHT)
        label_D = MathTex("D").next_to(D, DOWN)
        label_E = MathTex("E").next_to(E, RIGHT)
        pointD = Dot(point=D, color=YELLOW)
        pointE = Dot(point=E, color=YELLOW)
        AD_bisector = Line(A, D, color=YELLOW)
        AB_Side = Line(A, B, color=RED)
        CD_Side = Line(C, D, color=RED)

        angleA = Angle.from_three_points(C, A, B, other_angle=True)
        angleB = Angle.from_three_points(A, B, C, other_angle=True)
        angleC = Angle.from_three_points(B, C, A, other_angle=True)
        angle_BAD = Angle.from_three_points(D, A, B, other_angle=True)
        angle_DAC = Angle.from_three_points(C, A, D, other_angle=True)
        angle_ABE = Angle.from_three_points(A, B, E, other_angle=True)
        angle_EBC = Angle.from_three_points(E, B, C, other_angle=True)


        BE_bisector = Line(B, E, color=GREEN)
        EC_side = Line(E, C, color = GREEN)

        groupTriangleAndLabels = VGroup(triangle, label_A, label_B, label_C, label_D, pointD, angleA, angleB, angleC, AD_bisector, AB_Side, CD_Side, angle_BAD, angle_DAC, label_E, pointE, BE_bisector, angle_ABE, angle_EBC)

        groupTriangleAndLabels.move_to(ORIGIN + DOWN)

        self.play(Create(triangle))
        self.play(Write(label_A), Write(label_B), Write(label_C))

        LetangleCbex = MathTex("x")
        angleBbe2x = MathTex("2x")

        angleBADText = MathTex("y")
        angleDACText = MathTex("y")
        angleBADText.next_to(angle_BAD, DOWN)
        angleDACText.next_to(angle_DAC, DOWN +RIGHT)

        angleABEText = MathTex("x")
        angleEBCText = MathTex("x")
        angleABEText.next_to(angle_ABE.point_from_proportion(0.5) + 0.3*UP)
        angleEBCText.next_to(angle_EBC)
        
        self.play(Create(angleC))
        LetangleCbex.next_to(angleC, 1.4*LEFT + 0.2*UP)
        self.play(Write(LetangleCbex))

        self.play(Create(angleB))
        angleBbe2x.next_to(angleB, RIGHT + 0.3*UP)
        self.play(Write(angleBbe2x))

        
        self.play(Create(pointD))
        self.play(Write(label_D))

        
        self.play(Create(AD_bisector))

        self.play(Create(angle_BAD), Create(angle_DAC))
        self.play(Write(angleDACText), Write(angleBADText))

        self.play(
            Create(AB_Side),
            Create(CD_Side),
        )
        

        
        
        self.play(Create(BE_bisector))
        self.play(Create(pointE))
        self.play(Write(label_E))

        self.play(FadeOut(angleBbe2x))

        self.add(angle_ABE, angle_EBC)
        self.remove(angleB)

        self.play(
            Write(angleABEText),
            Write(angleEBCText)
        )

        groupOppositeAnglesAndSide_EBC = VGroup(angle_EBC, angleEBCText, )

        self.wait(5)
