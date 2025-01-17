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

        highlighted_part1 = problemDescripton[21:27]
        highlighted_part2 = problemDescripton[49:62]
        highlighted_part3 = problemDescripton[66:71]


        # PROBLEM = VGroup(problemDescripton, background_rectangle_1, background_rectangle_2, background_rectangle_3)
        
        self.play(
            problemDescripton.animate.move_to(UP*3),
            FadeOut(title)
        )

        background_rectangle_1 = BackgroundRectangle(highlighted_part1, color=YELLOW, fill_opacity=0.2)
        

        background_rectangle_2 = BackgroundRectangle(highlighted_part2, color=YELLOW, fill_opacity=0.2)
        

        background_rectangle_3 = BackgroundRectangle(highlighted_part3, color=YELLOW, fill_opacity=0.2)

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

        triangle.z_index = -1


        # Add labels
        label_A = MathTex("A").next_to(A, UP)
        label_B = MathTex("B").next_to(B, LEFT)
        label_C = MathTex("C").next_to(C, RIGHT)
        label_D = MathTex("D").next_to(D, DOWN)
        label_E = MathTex("E").next_to(E, RIGHT)
        pointD = Dot(point=D, color=YELLOW)
        pointE = Dot(point=E, color=YELLOW)
        AD_bisector = Line(A, D)
        AB_Side = Line(A, B, color=RED)
        CD_Side = Line(C, D, color=RED)
        BC_side = Line(B, C)
        AE_side = Line(A, E)

        angleA = Angle.from_three_points(C, A, B, other_angle=True)
        angleB = Angle.from_three_points(A, B, C, other_angle=True)
        angleC = Angle.from_three_points(B, C, A, other_angle=True)
        angle_BAD = Angle.from_three_points(D, A, B, other_angle=True)
        angle_DAC = Angle.from_three_points(C, A, D, other_angle=True)
        angle_ABE = Angle.from_three_points(A, B, E, other_angle=True)
        angle_EBC = Angle.from_three_points(E, B, C, other_angle=True)
        angle_EDC = Angle.from_three_points(E, D, C, other_angle = True)
        angle_ADE = Angle.from_three_points(A, D, E, other_angle = True)
        angle_ADC = Angle.from_three_points(A, D, C, other_angle = True)


        BE_bisector = Line(B, E, color=GREEN)
        EC_side = Line(E, C, color = GREEN)
        DE_side = Line(D, E, color=BLUE)

        triangleCED = Polygon(
            C, E, D, color=WHITE
        ).set_fill(TEAL, opacity=1.0)

        triangleCED.z_index = -1

        triangleABE = Polygon(
            A, E, B, color=WHITE
        ).set_fill(TEAL, opacity=1.0)

        triangleABE.z_index = -1

        triangleCBE = Polygon(
            C, E, B, color=WHITE
        ).set_fill(TEAL, opacity=1.0)

        triangleCBE.z_index = -1

        triangleADE = Polygon(
            A, E, D, color=WHITE
        ).set_fill(TEAL, opacity=1.0)

        triangleADE.z_index = -1

        triangleADC = Polygon(A, D, C, color = WHITE).set_fill(TEAL, opacity=1.0)
        triangleADC.z_index = -1

        groupTriangleAndLabels = VGroup(triangle, label_A, label_B, label_C, label_D, pointD, angleA, angleB, angleC, AD_bisector, AB_Side, CD_Side, angle_BAD, angle_DAC, label_E, pointE, BE_bisector, angle_ABE, angle_EBC, EC_side, BC_side, DE_side, AE_side, triangleCED, triangleABE, triangleCBE, angle_EDC, triangleADE, angle_ADE, angle_ADC, triangleADC)

        groupTriangleAndLabels.move_to(ORIGIN + DOWN)

        self.play(Create(triangle))
        self.play(Write(label_A), Write(label_B), Write(label_C))

        LetangleCbex = MathTex("x")
        LetangleCbex.z_index = 2

        angleBbe2x = MathTex("2x")
        angleBbe2x.z_index = 2

        angleBADText = MathTex("y")
        angleBADText.z_index = 2

        angleDACText = MathTex("y")
        angleDACText.z_index = 2
        angleBADText.next_to(angle_BAD, DOWN)
        angleDACText.next_to(angle_DAC, DOWN +RIGHT)

        angleABEText = MathTex("x")
        angleABEText.z_index = 2
        angleEBCText = MathTex("x")
        angleEBCText.z_index = 2
        angleABEText.next_to(angle_ABE.point_from_proportion(0.5) + 0.4*UP)
        angleEBCText.next_to(angle_EBC)

        angleADCText = MathTex("3y")
        angleADCText.next_to(angle_ADC, RIGHT)
        
        LetangleCbex.next_to(angleC, 1.4*LEFT + 0.2*UP)

        angleBbe2x.next_to(angleB, RIGHT + 0.3*UP)

        downText1 = Text("∠B = 2∠C", line_spacing=1.5).next_to(triangle, 3.5*DOWN)
        downText1.scale(0.5)

        downText2 = Text("Let ∠C = x, then ∠B = 2x").next_to(downText1, DOWN)
        downText2.scale(0.5)

        self.play(
            Create(background_rectangle_1)
        )

        self.play(
            Write(downText1)
        )

        self.play(
            Write(downText2)
        )

        # self.play(
        #     Create(background_rectangle_1),
        #     Write(downText1),
        #     Write(downText2),
        #     Create(angleC),
        #     Create(angleB),
        #     Write(LetangleCbex),
        #     Write(angleBbe2x),
        #     run_time=4,
        # )
        self.play(
            Create(angleC),
            Create(angleB),
            Write(LetangleCbex),
            Write(angleBbe2x),
            run_time=2,
        )

        self.wait(1)

        self.remove(downText2, downText1)

        downText1 = Text("AD bisects ∠BAC", line_spacing=1.5).next_to(triangle, 3.5*DOWN)
        downText1.scale(0.5)

        self.play(
            Create(background_rectangle_2)
        )

        self.play(Write(downText1))

        # self.play(
        #     Create(background_rectangle_2),
        #     Write(downText1),
        #     Create(pointD),
        #     Write(label_D),
        #     Create(AD_bisector),
        #     Create(angle_BAD),
        #     Create(angle_DAC),
        #     Write(angleDACText),
        #     Write(angleBADText),
        #     run_time=4

        # )
        self.play(
            Create(pointD),
            Write(label_D),
            Create(AD_bisector),
            Create(angle_BAD),
            Create(angle_DAC),
            Write(angleDACText),
            Write(angleBADText),
            run_time=3

        )

        self.wait(1)
        self.remove(downText2, downText1)

        downText1 = Text("AB = CD", line_spacing=1.5).next_to(triangle, 3.5*DOWN)
        downText1.scale(0.5)

        self.play(
            Create(background_rectangle_3),
            Write(downText1),
            Create(AB_Side),
            Create(CD_Side),
            run_time=2
        )
        
        self.wait(2)
        self.remove(downText2, downText1)

        downText1 = Text("In △ABC\n 2x+(y+y)+x = 180°", line_spacing=1.5).next_to(triangle, 3.5*DOWN)
        downText1.scale(0.5)

        self.play(
            triangle.animate.set_fill(TEAL, opacity=1),
            Write(downText1),
            runt_time = 3

        )

        self.wait(1)

        self.play(triangle.animate.set_fill(opacity=0))

        self.play(FadeOut(downText1))
        Equation_1 = Text("3x + 2y = 180°").next_to(triangle, 3.5*DOWN)
        Equation_1.scale(0.5)

        self.play(FadeIn(Equation_1))

        self.wait(1)


        self.play(
            Equation_1.animate.move_to(ORIGIN + 2*UP + 2*RIGHT)
        )

        self.wait()

        downText1 = Text("Construction: Draw the angle bisector of ∠B").next_to(triangle, 3.5*DOWN)
        downText1.scale(0.5)

        self.play(Write(downText1))

        self.play(
            Create(BE_bisector),
            Create(pointE), 
            Write(label_E),
            FadeOut(angleBbe2x),
            run_time=3
        )
        

        self.add(angle_ABE, angle_EBC)
        self.remove(angleB)

        self.play(
            Write(angleABEText),
            Write(angleEBCText)
        )

        self.wait(1)

        self.remove(downText1)
        downText1 = Text("In △BEC").next_to(triangle, 3.5*DOWN)
        downText1.scale(0.5)

        downText2 = Text("∠B =∠C= x, so, side BE = EC").next_to(downText1, 0.75*DOWN)
        downText2.scale(0.5)

        EC_side.z_index = 1
        self.play(Write(downText1))
        self.play(Create(triangleCBE))
        self.play(Write(downText2))
        self.play(Create(EC_side))

        self.wait(1)
        
        self.remove(triangleCBE, downText2, downText1)
        

        downText1 = Text("Construction: Connect D and E").next_to(triangle, 3.5*DOWN)
        downText1.scale(0.5)

        self.play(Write(downText1),)

        self.play(
            Create(DE_side), 
            run_time = 2
        )

        self.wait(1)
        self.remove(downText1)


        downText1 = Text("In △CED and △BEA").next_to(triangle, 3.5*DOWN)
        downText1.scale(0.5)

        downText2 = Text(" CD = AB \n CE = BE \n∠DCE = ∠ABE \nHence, △CED≅△BEA (SAS)\n", line_spacing=1.5).next_to(downText1, 0.75*DOWN)
        downText2.scale(0.5)

        

        self.play(
            Write(downText1),
            Create(triangleCED),
            Create(triangleABE),
            run_time = 3
        )

        self.wait(1)

        self.play(
            Write(downText2),
            run_time = 6
        )

        self.wait(1)
        
        self.play(FadeOut(triangleCED, triangleABE, downText1, downText2))

        downText1 = Text("Since, △CED≅△BEA,\n DE = AE (Blue) and ∠CDE = ∠BAE = 2y", line_spacing=1.5).next_to(triangle, 3.5*DOWN)
        downText1.scale(0.5)

        angle_EDC_text = MathTex("2y")
        angle_EDC_text.next_to(angle_EDC, RIGHT)

        self.play(
            Write(downText1)
        )

        self.play(
            AE_side.animate.set_color(BLUE),
            Create(angle_EDC),
            Write(angle_EDC_text),
            run_time = 4
        )

        self.wait(1)
        self.remove(downText1)

        downText1 = Text("Now in, △ADE", line_spacing=1.5).next_to(triangle, 3.5*DOWN)
        downText1.scale(0.5)

        self.play(
            Write(downText1),
            Create(triangleADE),
            run_time = 2
        )

        downText2 = Text("AE = DE, therefore ∠DAE = ∠EDA = y", line_spacing=1.5).next_to(downText1, DOWN)
        downText2.scale(0.5)

        angle_ADE_text = MathTex("y")
        angle_ADE_text.next_to(angle_ADE, UP)

        self.play(
            Write(downText2)
        )

        self.play(Create(angle_ADE),
            Write(angle_ADE_text),)
        
        self.wait(1)

        self.remove(triangleADE)

        self.wait(1)

        self.play(
            FadeOut(angle_EDC),
            FadeOut(angle_EDC_text),
            FadeOut(angle_ADE),
            FadeOut(angle_ADE_text),
        )

        self.remove(downText2, downText1)


        downText1 = Text("∠ADC = 3y", line_spacing=1.5).next_to(triangle, 3.5*DOWN)
        downText1.scale(0.5)

        self.play(Create(angle_ADC), Create(angleADCText), Write(downText1))

        self.wait()

        self.remove(downText1)

        downText1 = Text("In △ADC").next_to(triangle, 3.5*DOWN)
        downText1.scale(0.5)

        downText2 = Text("y + 3y + x = 180° ", line_spacing=1.5).next_to(downText1, DOWN)
        downText2.scale(0.5)

        self.play(
            Create(triangleADC),
            Write(downText1),
            run_time = 2
        )

        self.wait(1)

        self.play(
            Write(downText2)
        )

        self.wait(1)

        Equation_2 = Text("4y + x = 180° ", line_spacing=1.5).next_to(downText1, DOWN)
        Equation_2.scale(0.5)

        self.play(
            FadeOut(downText2),
            FadeOut(downText1)
        )

        self.play(FadeIn(Equation_2))
        self.wait(1)

        # point_temp = Equation_1.get_center + DOWN

        self.play(Equation_2.animate.move_to(Equation_1.get_center() + 0.5*DOWN))

        equations = VGroup(Equation_1, Equation_2)

        self.camera.frame.save_state()

        self.play(
            self.camera.frame.animate.set(width = equations.width*2).move_to(equations),
        )

        downText1 = Text("Solving the equations, we get -").next_to(equations, DOWN)
        downText1.scale(0.3)
        self.play(Write(downText1))

        downText2 = Text("x = 36°, y = 36°").next_to(downText1, DOWN)
        downText2.scale(0.5)
        self.play(Write(downText2))

        surroundingRec = SurroundingRectangle(downText2, color=WHITE)
        self.play(Create(surroundingRec))

        self.play(Restore(self.camera.frame))

        downText1 = Text("∠BAC = 2y").next_to(triangle, 3.5*DOWN)
        downText1.scale(0.5)

        downText2 = Text("∠BAC = 2 × 36 = 72°", line_spacing=1.5).next_to(downText1, DOWN)
        downText2.scale(0.5)

        self.play(
            Write(downText1)
        )

        self.play(
            Write(downText2)
        )

        self.play(
            FadeOut(downText2),
            FadeOut(downText1)
        )

        downText1 = Text("∠BAC = 72°").next_to(triangle, 3.5*DOWN)
        downText1.scale(0.5)

        self.play(
            Write(downText1)
        )

        surroundingRec = SurroundingRectangle(downText1, color=YELLOW)
        self.play(Create(surroundingRec))
        
        self.wait(5)
