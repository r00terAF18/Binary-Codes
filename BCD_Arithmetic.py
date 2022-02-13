from manim import *
from pyparsing import col


class Add(Scene):
    def construct(self):
        text = Text("BCD Arithmetic")
        text.set_color(BLUE)
        self.play(Write(text))
        self.wait()
        self.play(Unwrite(text))
        self.wait()
        ###############################

        text = (
            MathTex("(", "1", "8", "4", ")_{10}", "+", "(", "5", "7", "6", ")_{10}")
            .arrange(buff=0.2)
            .shift(LEFT * 4)
            .shift(UP * 3)
        )

        # Upper Numbera
        self.play(Write(text))
        self.wait()
        textbcd1 = (
            MathTex("0001", "1000", " 0100")
            .arrange(buff=0.23)
            .shift(RIGHT * 2)
            .shift(UP * 3)
        )
        self.play(Write(textbcd1))
        fr1 = SurroundingRectangle(text[1], buff=0.1)
        fr8 = SurroundingRectangle(text[2], buff=0.1)
        fr4 = SurroundingRectangle(text[3], buff=0.1)

        fr21 = SurroundingRectangle(textbcd1[0], buff=0.1)
        fr28 = SurroundingRectangle(textbcd1[1], buff=0.1)
        fr24 = SurroundingRectangle(textbcd1[2], buff=0.1)
        self.play(Create(fr1), Create(fr8), Create(fr4))
        self.wait()
        self.play(
            ReplacementTransform(fr1, fr21),
            ReplacementTransform(fr8, fr28),
            ReplacementTransform(fr4, fr24),
        )
        self.wait()
        ##################################

        # Lower Numbers
        textbcd2 = (
            MathTex("+0101", "0111", " 0110")
            .arrange(buff=0.23)
            .shift(RIGHT * 1.8)
            .shift(UP * 2)
        )
        self.play(Write(textbcd2))
        self.wait()

        fr5 = SurroundingRectangle(text[7], buff=0.1)
        fr7 = SurroundingRectangle(text[8], buff=0.1)
        fr6 = SurroundingRectangle(text[9], buff=0.1)

        fr25 = SurroundingRectangle(textbcd2[0], buff=0.1)
        fr27 = SurroundingRectangle(textbcd2[1], buff=0.1)
        fr26 = SurroundingRectangle(textbcd2[2], buff=0.1)
        self.play(Create(fr5), Create(fr7), Create(fr6))
        self.wait()
        self.play(
            ReplacementTransform(fr5, fr25),
            ReplacementTransform(fr7, fr27),
            ReplacementTransform(fr6, fr26),
        )
        self.wait()

        self.play(
            Uncreate(fr21),
            Uncreate(fr28),
            Uncreate(fr24),
            Uncreate(fr25),
            Uncreate(fr27),
            Uncreate(fr26),
        )

        d1 = Dot([0, 2, 0])
        d2 = Dot([4, 2, 0])

        self.play(
            Create(
                Line(d1, d2)
                # .stretch(4, 1)
                .shift(DOWN * 0.5)
            )
        )

        ###############################
        # calculate the addition
        textbcd3 = (
            MathTex("0111", "10000", "1010")
            .arrange(buff=0.2)
            .shift(RIGHT * 2)
            .shift(UP * 1)
        )
        self.play(Write(textbcd3))
        self.wait()
        result1 = SurroundingRectangle(textbcd3, buff=0.1, color=RED)
        self.play(Create(result1))
        txt1 = Text("1010 and 10000 are >= then 1010").shift(DOWN * 2)
        txt2 = Text("Thus we have to add 0110 to them").shift(DOWN * 2.8)
        self.play(Write(txt1))
        self.play(Write(txt2))

        self.play(Uncreate(result1))

        ###############################

        textbcd4 = (
            MathTex("+0000", "0110", "0110")
            .arrange(buff=0.22)
            .shift(RIGHT * 1.8)
            .shift(DOWN * 0.2)
        )
        self.play(Write(textbcd4))
        self.wait()
        result1 = SurroundingRectangle(textbcd4, buff=0.1, color=BLUE)
        self.play(Create(result1))
        self.play(Unwrite(txt1), Unwrite(txt2), Uncreate(result1))

        d1 = Dot([0, 0, 0])
        d2 = Dot([4, 0, 0])

        self.play(
            Create(
                Line(d1, d2)
                # .stretch(4, 1)
                .shift(DOWN * 0.5)
            )
        )

        ##############################
        # write result
        textbcd5 = (
            MathTex("0111", "0110", "0000")
            .arrange(buff=0.2)
            .shift(RIGHT * 2)
            .shift(DOWN * 1.3)
        )
        self.play(Write(textbcd5))
        self.wait()
        result1 = SurroundingRectangle(textbcd5, buff=0.1, color=GREEN)
        self.play(Create(result1))
        self.wait()

        ##############################
        # write final result

        text = (
            MathTex(
                "(",
                "1",
                "8",
                "4",
                ")_{10}",
                "+",
                "(",
                "5",
                "7",
                "6",
                ")_{10}",
                "=",
                "760",
            )
            .arrange(buff=0.1)
            .shift(LEFT * 1.2)
            .shift(DOWN * 2.3)
        )

        # Upper Numbera
        self.play(Write(text))
        self.wait()
        self.wait()
