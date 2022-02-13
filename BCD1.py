from manim import *


class WriteBinary(Scene):
    def construct(self):
        # write binary coded deciaml and uncreate it
        text = Text("Binary Coded Decimal Code or BCD")
        text.set_color(BLUE)
        self.play(Write(text))
        self.wait()
        self.play(Unwrite(text))
        self.wait()
        ###############################

        #  Write 748 in BCD and each digit is a number
        text = MathTex("(748)_{10}").shift(2.2 * UP)

        n7 = Text("7").shift(1.2 * UP).shift(2.5 * LEFT)
        n4 = Text("4").shift(1.2 * UP)
        n8 = Text("8").shift(1.2 * UP).shift(2.5 * RIGHT)

        self.play(Write(text))
        self.wait()

        self.play(Write(n7), Write(n4), Write(n8))
        self.wait()

        ###############################

        n78 = Text("8").shift(0.4 * UP).shift(3.5 * LEFT)
        n74 = Text("4").shift(0.4 * UP).shift(3 * LEFT)
        n72 = Text("2").shift(0.4 * UP).shift(2.5 * LEFT)
        n71 = Text("1").shift(0.4 * UP).shift(2 * LEFT)

        self.play(Write(n78), Write(n74), Write(n72), Write(n71))
        self.wait()

        ###############################

        # show how binary 7 is decoded
        u4 = Underline(n74)
        u2 = Underline(n72)
        u1 = Underline(n71)
        self.play(
            Animation(n78),
            Animation(n74),
            Animation(n71),
            Write(u4),
            Write(u2),
            Write(u1),
        )
        self.wait()

        ###############################
        # write didgits beneath the number
        self.play(
            Write(Text("0").shift(0.25 * DOWN).shift(3.5 * LEFT)),
            Write(Text("1").shift(0.25 * DOWN).shift(3 * LEFT)),
            Write(Text("1").shift(0.25 * DOWN).shift(2.5 * LEFT)),
            Write(Text("1").shift(0.25 * DOWN).shift(2 * LEFT)),
        )
        self.wait()

        ###############################
        # show how binary 4 is decoded

        n48 = Text("8").shift(0.4 * UP).shift(0.7 * LEFT)
        n44 = Text("4").shift(0.4 * UP).shift(0.2 * LEFT)
        n42 = Text("2").shift(0.4 * UP).shift(0.3 * RIGHT)
        n41 = Text("1").shift(0.4 * UP).shift(0.8 * RIGHT)

        self.play(Write(n48), Write(n44), Write(n42), Write(n41))
        self.wait()

        ###############################
        u4 = Underline(n44)
        self.play(
            Animation(n44),
            Write(u4),
        )
        self.wait()

        ###############################
        self.play(
            Write(Text("0").shift(0.25 * DOWN).shift(0.7 * LEFT)),
            Write(Text("1").shift(0.25 * DOWN).shift(0.2 * LEFT)),
            Write(Text("0").shift(0.25 * DOWN).shift(0.3 * RIGHT)),
            Write(Text("0").shift(0.25 * DOWN).shift(0.8 * RIGHT)),
        )
        self.wait()

        ###############################
        # show how binary 8 is decoded

        n88 = Text("8").shift(0.4 * UP).shift(1.9 * RIGHT)
        n84 = Text("4").shift(0.4 * UP).shift(2.4 * RIGHT)
        n82 = Text("2").shift(0.4 * UP).shift(2.9 * RIGHT)
        n81 = Text("1").shift(0.4 * UP).shift(3.4 * RIGHT)

        self.play(Write(n88), Write(n84), Write(n82), Write(n81))
        self.wait()

        ###############################
        u8 = Underline(n88)
        self.play(
            Animation(n88),
            Write(u8),
        )
        self.wait()

        ###############################
        self.play(
            Write(Text("1").shift(0.25 * DOWN).shift(1.9 * RIGHT)),
            Write(Text("0").shift(0.25 * DOWN).shift(2.4 * RIGHT)),
            Write(Text("0").shift(0.25 * DOWN).shift(2.9 * RIGHT)),
            Write(Text("0").shift(0.25 * DOWN).shift(3.4 * RIGHT)),
        )
        self.wait()

        ###############################
        # show the final output
        mText = MathTex("(748)_{10} = (011101001000)_{2}").shift(1.5 * DOWN)
        self.play(Write(mText))
        self.wait()
        self.wait()
