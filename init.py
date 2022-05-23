#毎ターン同じ技しか出せない
#効果は抜群、今ひとつ(3type)
#攻撃、防御、特攻、特防、素早さ
#コマンドJ or viewのterminal

    #技を四つ覚えてランダムに使用できる
    #素早さが高い方が先に攻撃する
class Pokemon(object):
    def __init__(self,level,pokemontype = "ノーマル"):
        self.level = level
        self.hp = 100
        self.speed = 50
        self.pokemontype = pokemontype
        self.name = "pokemon"

    def status(self):
        return f"{なまえ:{self.name} | レベル:{self.level} | タイプ:{self.pokemontype} | HP:{self.hp} | すばやさ:{self.speed}}"

class Onna(Pokemon):
    def __init__(self, level):
        super().__init__(level)
        self.hp += 5 * level
        self.speed += 3 * level
        if self.pokemontype == "ノーマル":
            self.pokemontype = "ほのお"
        if self.name == "pokemon":
            self.name = "女"


class Pikachu(Pokemon):
    def __init__(self, level):
        super().__init__(level)
        self.hp += 4 * level
        self.speed += 4 * level
        if self.pokemontype == "ノーマル":
            self.pokemontype = "でんき"
        if self.name == "pokemon":
            self.name = "ピカチュウ"

def



onna_waza = {
     "はたく" : 50,
     "のしかかり" : 100,
     "なきごえ" : 10,
     "どくどく" : 30,
}

pikachu_waza = {
     "でんきショック" : 50,
     "ボルテッカー" : 100,
     "しっぽをふる" : 10,
     "たいあたり" : 20,
}

#敵と遭遇（野生）
print("野生の女の子が現れた！")


#自分のポケモン出す
print("行っておいで、ピカチュウ！\n")

while True:    #どちらかが倒れるまで繰り返す
    
    #自分の攻撃ターン
    waza_p = "しっぽをふる"    #ここで技名を変更する（技選択）

    onna_hp -= pikachu_waza[waza_p]
    print("ピカチュウの" + waza_p + "こうげき！")
    print("女の子に" + str(pikachu_waza[waza_p]) + "のダメージ")
    print("女の子残りHP " + str(onna_hp) + "\n")


    #（相手の攻撃ターン）
    #倒した
    if onna_hp <= 0:
        print("野生の女の子はたおれた！")
        break

    else:
        waza_o = "どくどく"    #ここで技名を変更する（技選択）

        pikachu_hp -= onna_waza[waza_o]
        print("女の子の" + waza_o + "こうげき！")
        print("ピカチュウに" + str(onna_waza[waza_o]) + "のダメージ")
        print("ピカチュウ残りHP " + str(pikachu_hp) + "\n")

        if pikachu_hp <= 0:
            print("ピカチュウはたおれた！")
            break
    #（経験値）



