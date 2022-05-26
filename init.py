#毎ターン同じ技しか出せない
#効果は抜群、今ひとつ(3type)
#攻撃、防御、特攻、特防、素早さ
#コマンドJ or viewのterminal

    #技を四つ覚えてランダムに使用できる
    #素早さが高い方が先に攻撃する
class Pokemon(object):
    def __init__(self, level, pokemontype, name):
        self.level = level
        self.hp = 100
        self.speed = 50
        self.pokemontype = pokemontype
        self.name = name

    def status(self):
        return f"{なまえ:{self.name} | レベル:{self.level} | タイプ:{self.pokemontype} | HP:{self.hp} | すばやさ:{self.speed}}"

class Onna(Pokemon):
    def __init__(self, level):
        super().__init__(level, "ほのお", "女の子")
        self.hp += 5 * level
        self.speed += 3 * level
        self.onna_waza = [
             {"name": "はたく", "damage": 50},
             {"name": "のしかかり", "damage": 100},
             {"name": "なきごえ", "damage": 10},
             {"name": "どくどく", "damage": 30}
         ]


class Pikachu(Pokemon):
    def __init__(self, level):
        super().__init__(level, "でんき", "ピカチュウ")
        self.hp += 4 * level
        self.speed += 4 * level
        self.pikachu_waza = [
             {"name": "でんきショック", "damage": 50},
             {"name": "ボルテッカー", "damage": 100},
             {"name": "しっぽをふる", "damage": 10},
             {"name": "たいあたり", "damage": 20}
         ]
 

#敵と遭遇（野生）
creature_enemy = Onna(50)
onna_hp = creature_enemy.hp
print(f"野生の{creature_enemy.name}が現れた！")


#自分のポケモン出す
creature_friend = Pikachu(50)
pikachu_hp = creature_friend.hp
print(f"行っておいで、{creature_friend.name}! \n")

n = int(input())
waza_p = creature_friend.pikachu_waza
waza_o = creature_enemy.onna_waza


while True:    #どちらかが倒れるまで繰り返す

    for i in range(3):
        print(waza_p[i])
    print("0~3の番号で技を選択")

    
    if creature_friend.speed >= creature_enemy.speed:
        onna_hp -= waza_p[n]["damage"]
        print(f"{creature_friend.name} の {waza_p[n]["name"]} こうげき！")
        print(f"{creature_enemy.name} に {waza_p[n]["damage"]} のダメージ！")
        print(f"{creature_enemy.name} 残りHP {onna_hp} \n")
        #自分の攻撃ターン

        if onna_hp <= 0:
            print(f"野生の{creature_enemy.name}はたおれた！")
            break
    
    
    else:
        pikachu_hp -= waza_o[n]["damage"]
        print(f"{creature_enemy.name} の {waza_o[n]["name"]} こうげき！")
        print(f"{creature_friend.name} に {waza_o[n]["damage"]} のダメージ！")
        print(f"{creature_friend.name} 残りHP {pikachu_hp} \n")
        #相手の攻撃ターン

         if pikachu_hp <= 0:
            print(f"{creature_friend.name}はたおれた！")
            break

