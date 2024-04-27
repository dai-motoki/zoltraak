from manim import *

class FileStateTransition(Scene):
    def construct(self):
        # テキストを作成
        text_read = Text("プロンプト", color=RED, font_size=24)  # フォントサイズを24に変更
        text_req = Text("ドキュメント\n(自然言語)", color=BLUE, font_size=24)   # フォントサイズを24に変更
        text_lang = Text("プログラム\n(高級言語)", color=GREEN, font_size=24)  # フォントサイズを24に変更
        text_test = Text("システム\nテスト項目", color=ORANGE, font_size=24)  # テスト項目のテキストを追加

        # 丸と四角を作成
        circle_read = Circle(color=WHITE)
        circle_req = Circle(color=WHITE)
        circle_lang = Circle(color=WHITE)
        square_test = Square(color=WHITE)  # テスト項目の四角を追加

        # 丸と四角を横に並べる（間隔を狭める）
        shapes = VGroup(circle_read, circle_req, circle_lang, square_test).arrange(RIGHT, buff=1.5)

        # テキストを丸と四角の上に配置
        text_read.next_to(circle_read, UP)
        text_req.next_to(circle_req, UP)
        text_lang.next_to(circle_lang, UP)
        text_test.next_to(square_test, UP)  # テスト項目のテキストを四角の上に配置

        # 丸、四角、テキストを表示
        self.play(Create(shapes), Write(text_read), Write(text_req), Write(text_lang), Write(text_test))
        self.wait(1)

        # 赤色の丸を先に光らせる
        self.play(circle_read.animate.set_fill(RED, opacity=1))
        self.wait(1)

        # "zoltraakプロンプト.txt" コマンドを表示
        command1 = Text("zoltraakdocument -p prompt", font_size=24).next_to(circle_read, DOWN)
        self.play(Write(command1))
        self.wait(1)
        # self.play(FadeOut(command1))  # command1をフェードアウト

        # 矢印を作成し、コマンドと同時に表示
        arrow1 = Arrow(circle_read.get_right(), circle_req.get_left(), color=WHITE)
        self.play(Create(arrow1), run_time=1)
        self.play(
            circle_req.animate.set_fill(BLUE, opacity=1),
        )
        self.wait(1)

        # "zoltraakドキュメント" コマンドを表示
        command2 = Text("zoltraakdocument", font_size=24).next_to(circle_req, DOWN)
        self.play(
            FadeOut(command1),  # 前のコマンドを消す
            Write(command2)
        )
        self.wait(1)

        # 矢印を作成し、コマンドと同時に表示
        arrow2 = Arrow(circle_req.get_right(), circle_lang.get_left(), color=WHITE)
        self.play(Create(arrow2), run_time=1)
        self.play(
            circle_lang.animate.set_fill(GREEN, opacity=1),
        )
        self.wait(1)

        # プログラムからテスト項目への矢印を作成
        arrow3 = Arrow(circle_lang.get_right(), square_test.get_left(), color=WHITE)
        self.play(Create(arrow3), run_time=1)
        self.play(
            square_test.animate.set_fill(ORANGE, opacity=1),
        )
        self.wait(1)

        # テスト項目からドキュメントへの矢印を作成
        arrow4 = Arrow(square_test.get_right(), circle_req.get_right(), color=WHITE).shift(DOWN*1.7)  # 矢印の位置を上にずらす
        self.play(Create(arrow4), run_time=1)
        self.wait(1)

        # ドキュメントとプログラムの同期を表現
        sync_text = Text("テスト項目を網羅されるまで、ドキュメントとプログラムの再構築が進む", font_size=24).next_to(shapes, DOWN*1.7, buff=1)
        self.play(Write(sync_text))
        self.wait(1)  # 1秒待つ
        self.play(FadeOut(sync_text))  # sync_textを消す
        
        # ドキュメントとプログラムの間に双方向の矢印を追加
        
        sync_arrow1 = DoubleArrow(circle_req.get_bottom(), circle_lang.get_bottom(), color=YELLOW, buff=0.5)
        sync_arrow2 = DoubleArrow(circle_lang.get_bottom(), circle_req.get_bottom(), color=YELLOW, buff=0.5)
        # ドキュメントとプログラムの間に "Compile" というテキストを追加
        compile_text = Text("Compile", font_size=24).move_to(sync_arrow1.get_center() + UP*0.5)
        self.play(Write(compile_text))
        
        # "zoltraakドキュメント" コマンドを表示
        sync_command = Text("zoltraakdocument", font_size=24).next_to(shapes, DOWN)
        self.play(
            FadeOut(command2),  # 前のコマンドを消す
            Write(sync_command)
        )
        
        # ドキュメントが変更されてピコンとなる
        self.play(
            circle_req.animate.set_fill(BLUE, opacity=0.5),
            Flash(circle_req, line_length=0.5, num_lines=20, color=BLUE, flash_radius=circle_req.width/2+SMALL_BUFF, time_width=0.5),
            run_time=1
        )
        
        # プログラムが変更されてピコンとなる
        self.play(
            circle_lang.animate.set_fill(GREEN, opacity=0.5),
            Flash(circle_lang, line_length=0.5, num_lines=20, color=GREEN, flash_radius=circle_lang.width/2+SMALL_BUFF, time_width=0.5),
            run_time=1
        )
        
        # プログラムが変更されてピコンとなる
        self.play(
            circle_lang.animate.set_fill(GREEN, opacity=0.5),
            Flash(circle_lang, line_length=0.5, num_lines=20, color=GREEN, flash_radius=circle_lang.width/2+SMALL_BUFF, time_width=0.5),
            run_time=1
        )
        
        # ドキュメントが変更されてピコンとなる
        self.play(
            circle_req.animate.set_fill(BLUE, opacity=0.5),
            Flash(circle_req, line_length=0.5, num_lines=20, color=BLUE, flash_radius=circle_req.width/2+SMALL_BUFF, time_width=0.5),
            run_time=1
        )
        
        self.play(Create(sync_arrow1), Create(sync_arrow2))
        
        self.wait(1)
        # ドキュメントとプログラムの同期を表現
        sync_text = Text("zoltraakdocument を行うたびにシステム実行と双方の同期がチェックされる", font_size=24).next_to(shapes, DOWN*1.7, buff=1)
        self.play(Write(sync_text))