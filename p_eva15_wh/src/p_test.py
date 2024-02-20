#!/usr/bin/env python3

import random

'''
入れます
319を繰り返す
　当たる→　５９％→　Rush
　外れる→　41%（時短100回）→　Rush or 左
Rush
　1/99を164回転
　　当たる→　リセット
　　外れる→　左
'''
class Eva15():
    # 左打ち（1/319で当たる。）
    # 
    current_balance = 0 # 最新の残高を格納していくための変数

    # init_balance: 初期残高
    # 
    def __init__(self, init_balance, ball_price=4):
        self.balance = init_balance # 初期残高
        self.ball_price = ball_price # 4円
        self.balls = init_balance/ball_price
        self.add_balls == 0

    # よくあるパチンコの計算を関数にまとめたい
    def pachinko(probability, num_traials):
        # 当たっか、否かの判定を表す変数（Bool型: True or False）フラグを立てる。
        win_flug == False #####
        for i in range (num_traials):
            if random.randrange(probability)==1:
                win_flug ==True
            else: pass    
            print(win_flug)

    # Bool(1/319)
    def hidariUti(probability=319):
        print(にげちゃだめだにげちゃだめｄにげちゃだめにげちゃだｍ) # 煽る
        # 0～319の中でランダムの数を生成して、それが1だったらTrueを返す
        if random.randrange(probability)==1:
            return True
        else: 
            return False

    # (59%, 41% chance)
    def chanceTime():
        # 左打ちを実行
        if self.hidariUti(): # 左打ちが当たったら、pass。Rushへ（True）
            return True
        else: # HU Hazure:
            # 時短のチャンス、お祈りチャンス
            for i in 100:
                print(i)
            

        # IN case of Atari
        self.add_balls == 450
        # if random.randrange(100)  0~1
        if rand(random.random(), 2) <= 58: #[0,1,~,100]
            return true
        else:
            ###
            pass
            # chance
            # !!


    # ST.()
    # ラッシュタイム：81％で継続
    def rush():
        # 
        while(self.balance != 0):
            if self.chanceTime():
                pass
            else: false


import sys
import pygame

def main():
    # pygameの初期化
    pygame.init()
    # メイン画面（Surface）初期化(横, 縦)
    main_surface = pygame.display.set_mode((300, 300)) 
    # メイン画面のタイトル
    pygame.display.set_caption("Pygame Sample")
    # フォントオブジェクト生成（引数：フォント名とフォントサイズ）
    # フォント名にNoneを指定するとPygameの既定のフォントになる
    font = pygame.font.Font(None, 30)
    # テキストのSurfaceオブジェクトの生成（引数：テキスト内容、antialias、文字の色RGB）
    text_surface = font.render("Hello World", True, (0, 0, 255))
    #メイン画面の色設定（引数：RGB）
    main_surface.fill((220, 220, 220))
    # メイン画面上にテキストを配置（引数：配置するSurface、座標）
    main_surface.blit(text_surface, (100, 100)) 
    # メイン画面の更新
    pygame.display.update()
    # Clockオブジェクトの生成
    clock = pygame.time.Clock()
    # ループを続けるかのフラグ
    going = True
    # 終了イベント発生までループをまわす
    while going:
        # イベントを取得
        for event in pygame.event.get():
            # 終了イベント（画面の×ボタン押下など）の場合、
            # ループを抜ける
            if event.type == pygame.QUIT:
                going = False
 
        # フレームレート（1秒間に何回画面を更新するか）の設定
        clock.tick(10)
    # 終了処理
    pygame.quit()
    sys.exit()


if __name__=="__main__":
    main()
    # print("初期残高は？")
    # input_balance = input("Inicial Balance Amount:")
    # print(f'your balance:{input_balance}\nBall Price: 4 yen')

    # # クラスを実体化（定義したクラスを実際に生成する）
    # # __init__(コンストラクタ)の中身が実行される。（self.balance、、、が定義される）
    # new_eva15_machine = Eva15(input_balance)
    # # 実際にクラスの中に定義した関数を使う書き方↓
    # # 始まる。残高
    # new_eva15_machine.rush()
    # # global_balance = new_eva15_machine.balance # 指定クラス内の変数を外の変数に格納する書き方

