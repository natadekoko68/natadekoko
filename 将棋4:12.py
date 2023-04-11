komamei_dic = {"ou":"王","kin":"金","gin":"銀","kei":"桂","kyo":"香", "kaku":"角", "hisha":"飛", "hu": "歩", "ngin":"成銀", "成桂":"nkei","nkyo":"成香", "uma":"馬", "ryu":"龍", "to":"と"}
koma_move ={"ou":[(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)],"kin":[(1,0),(1,1),(0,1),(-1,1),(-1,0),(0,-1)]}

class shogi:
    # komamei_dic = {"ou":"王","kin":"金","gin":"銀","kei":"桂","kyo":"香", "kaku":"角", "hisha":"飛車", "hu": "歩", "ngin":"成銀", "成桂":"nkei","nkyo":"成香", "uma":"馬", "ryu":"龍", "to":"と"}
    #王: ou, 金: kin, 銀: gin, 桂馬: kei, 香車: kyo, 角: kaku, 飛車: hisha, 歩: hu,
    #成銀: ngin, 桂成: nkei, 香成: nkyo, 馬: uma, 龍: ryu, と: to
    #先手0 後手1

    def __init__(self):
        self.board = [[["kyo",1],["kei",1],["gin",1],["kin",1],["ou",1],["kin",1],["gin",1],["kei",1],["kyo",1]],
        [["-",-1],["hisha",1],["-",-1],["-",-1],["-",-1],["-",-1],["-",-1],["kaku",1],["-",-1]],
        [["hu",1],["hu",1],["hu",1],["hu",1],["hu",1],["hu",1],["hu",1],["hu",1],["hu",1]],
        [["-",-1],["-",-1],["-",-1],["-",-1],["-",-1],["-",-1],["-",-1],["-",-1],["-",-1]],
        [["-",-1],["-",-1],["-",-1],["-",-1],["-",-1],["-",-1],["-",-1],["-",-1],["-",-1]],
        [["-",-1],["-",-1],["-",-1],["-",-1],["-",-1],["-",-1],["-",-1],["-",-1],["-",-1]],
        [["hu",0],["hu",0],["hu",0],["hu",0],["hu",0],["hu",0],["hu",0],["hu",0],["hu",0]],
        [["-",-1],["kaku",0],["-",-1],["-",-1],["-",-1],["-",-1],["-",-1],["hisha",0],["-",-1]],
        [["kyo",0],["kei",0],["gin",0],["kin",0],["ou",0],["kin",0],["gin",0],["kei",0],["kyo",0]]]
        self.kif = []
        self.mochigoma_sente = []
        self.mochigoma_gote = []
        self.tesu = 0
        self.turn = "senteban"

        #以下kif形式用
        self.kaisijikan = 0
        self.syuryojikan = 0
        self.tewariai = "hirate"
        self.sente_name = "sente"
        self.gote_name = "gote"
        
    #盤面の表示
    def print_board(self):
        a = ["1","2","3","4","5","6","7","8","9"]
        b = a[::-1]
        print("\t".join(b))
        for i in range(9):
            temp = []
            for j in range(10):
                if j != 9:
                    if self.board[i][j][1] != -1:
                        temp.append(str(self.board[i][j][1])+self.board[i][j][0])
                    else:
                        temp.append(self.board[i][j][0])
                else:
                    temp.append(a[i])
            print("\t".join(temp))
    
    #盤面+持ち駒の表示
    def print_senkyoku(self):
        print("後手の持ち駒 :", "\t".join(self.mochigoma_gote))
        self.print_board()
        print("先手の持ち駒 :", "\t".join(self.mochigoma_sente))

    #漢字の盤面表示
    def print_kanji(self):
        self.kanji_board = []
        for i in range(9):
            temp = []
            for j in range(9):
                if self.board[i][j][1] == 0:
                    temp.append(""+komamei_dic[self.board[i][j][0]])
                elif self.board[i][j][1] == 1:
                    temp.append("後"+komamei_dic[self.board[i][j][0]])
                else:
                    temp.append("-")
            self.kanji_board.append(temp)

        mochigoma_sente_kanji = []
        mochigoma_gote_kanji = []

        for key in self.mochigoma_sente:
            mochigoma_sente_kanji.append(komamei_dic[key])
        for key in self.mochigoma_gote:
            mochigoma_gote_kanji.append(komamei_dic[key])
        
        print("後手の持ち駒 :", "\t".join(mochigoma_gote_kanji))
        for i in range(9):
            print("\t".join(self.kanji_board[i]))
        print("先手の持ち駒 :", "\t".join(mochigoma_sente_kanji))
    
    #駒の成りの設定
    def nari(self,koma):
        if koma == "gin":
            return "ngin"
        if koma == "kei":
            return "nkei"
        if koma == "kyo":
            return "nkyo"
        if koma == "kaku":
            return "uma"
        if koma == "hisha":
            return "ryu"
        if koma == "hu":
            return "to"
        else:
            return koma
    
    def hunari(self,koma):
        if koma == "ngin":
            return "gin"
        if koma == "nkei":
            return "kei"
        if koma == "nkyo":
            return "kyo"
        if koma == "uma":
            return "kaku"
        if koma == "ryu":
            return "hisha"
        if koma == "to":
            return "hu"
        else:
            return koma

    #とりあえず駒を動かす
    def move(self, koma, prev, next):

        #駒の配置
        prev_temp_a, prev_temp_b = prev
        prev_a, prev_b = prev_temp_b - 1, 9 - prev_temp_a
        next_temp_a, next_temp_b = next
        next_a, next_b = next_temp_b-1, 9 - next_temp_a

        #駒の持ち主と手番の一致
        teban_bin = self.tesu % 2
        if teban_bin != self.board[prev_a][prev_b][1]:
            if teban_bin == 1:
                "後手番です"
            elif teban_bin == 0:
                "先手版です"
            return False

        #次の手番の決定
        self.tesu += 1
        if self.tesu%2 == 0:
            self.teban = "senteban"
        else:
            self.teban = "goteban"

        #駒の動き
        if self.board[prev_a][prev_b][0] != koma:
            return False
        if prev_a < 0 or prev_a > 8:
            return False
        if prev_b < 0 or prev_b > 8:
            return False
        if next_a < 0 or next_a > 8:
            return False
        if next_b < 0 or next_b > 8:
            return False
        elif self.board[next_a][next_b][1] != -1:
            if self.board[next_a][next_b][1] == 0:
                self.mochigoma_gote.append(self.hunari(self.board[next_a][next_b][0]))
            elif self.board[next_a][next_b][1] == 1:
                self.mochigoma_sente.append(self.hunari(self.board[next_a][next_b][0]))
            self.board[next_a][next_b] = self.board[prev_a][prev_b]
            self.board[prev_a][prev_b] = ["-",-1]
        else:
            self.board[next_a][next_b] = self.board[prev_a][prev_b]
            self.board[prev_a][prev_b] = ["-",-1]

        if prev != None and self.board[next_a][next_b][1] == 0 and next_a <= 2:
            self.board[next_a][next_b][1] = self.nari(self.board[next_a][next_b][1])
        if prev != None and self.board[next_a][next_b][1] == 1 and next_a >= 6:
            self.board[next_a][next_b][1] = self.nari(self.board[next_a][next_b][1])        

        return True

    # def pos_move(self,temp):
        # temp_temp_a, temp_temp_b = prev
        # temp_a, temp_b = temp_temp_b - 1, 9 - temp_temp_a
        # koma = self.board[temp_a][temp_b][0]
        # ans = []
        # if koma == "kin":
        #     if temp_a, temp_b

    
A = shogi()

A.move("hu",(2,7),(2,6))
A.move("hu",(2,6),(2,5))
A.move("hu",(2,5),(2,4))
A.move("hu",(2,4),(2,3))
A.move("hu",(2,3),(2,2))
A.move("hu",(2,2),(2,1))
A.print_kanji()