from manim import *


def f(x):
    return (1.02 * x) + 0.3


class Gray(Scene):
    def construct(self):
        text = Text("Gray Code", color=BLUE)
        self.play(Write(text))
        self.wait()
        self.play(Unwrite(text))
        #######################################

        # yes yes i know, for loops and while loops exists, but i really wasn't in the mood to use them

        self.play(Write(Text("0").shift(UP * 3.8).shift(LEFT * 2.5)))
        self.play(Write(Text("0000").shift(UP * 3.8)))
        self.play(Write(Text("1").shift(UP * 3.2).shift(LEFT * 2.5)))
        self.play(Write(Text("0001").shift(UP * 3.2)))
        self.play(Write(Text("2").shift(UP * 2.6).shift(LEFT * 2.5)))
        self.play(Write(Text("0011").shift(UP * 2.6)))
        self.play(Write(Text("3").shift(UP * 2).shift(LEFT * 2.5)))
        self.play(Write(Text("0010").shift(UP * 2)))
        self.play(Write(Text("4").shift(UP * 1.4).shift(LEFT * 2.5)))
        self.play(Write(Text("0110").shift(UP * 1.4)))
        self.play(Write(Text("5").shift(UP * 0.8).shift(LEFT * 2.5)))
        self.play(Write(Text("0111").shift(UP * 0.8)))
        self.play(Write(Text("6").shift(UP * 0.2).shift(LEFT * 2.5)))
        self.play(Write(Text("0101").shift(UP * 0.2)))
        self.play(Write(Text("7").shift(UP * -0.4).shift(LEFT * 2.5)))
        self.play(Write(Text("0100").shift(UP * -0.4)))
        self.play(Write(Text("8").shift(UP * -1).shift(LEFT * 2.5)))
        self.play(Write(Text("1100").shift(UP * -1)))
        self.play(Write(Text("9").shift(UP * -1.6).shift(LEFT * 2.5)))
        self.play(Write(Text("1101").shift(UP * -1.6)))
        self.play(Write(Text("10").shift(UP * -2.2).shift(LEFT * 2.5)))
        self.play(Write(Text("1111").shift(UP * -2.2)))

        self.play(
            Write(
                Text(
                    "As you can see only one digit\nchanges when the number changes"
                ).shift(UP * -3)
            )
        )
        self.wait()
