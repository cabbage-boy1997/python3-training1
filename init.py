#毎ターン同じ技しか出せない
#効果は抜群、今ひとつ(3type)
#攻撃、防御、特攻、特防、素早さ
#コマンドJ or viewのterminal

import random
# import pprint
import json

a = open('pokemon_status.json')
b = json.load(a)

    #技を四つ覚えてランダムに使用できる
    #素早さが高い方が先に攻撃する
class Pokemon(object):
    def __init__(self, level, status_dic):
        self.level = level
        self.hp = status_dic["HP"] 
        self.hp += 4 * level
        self.speed = status_dic["speed"]
        self.speed += 4 * level
        self.pokemontype = status_dic["type"]
        self.name = status_dic["name"]
        self.waza = status_dic["waza"]

    # def status(self):
        # return f"{なまえ:{self.name} | レベル:{self.level} | タイプ:{self.pokemontype} | HP:{self.hp} | すばやさ:{self.speed}}"

# class Onna(Pokemon):
#     def __init__(self, level):
#         super().__init__(level, , "女の子")
#         self.hp += 5 * level
#         self.speed += 3 * level
#         self.onna_waza = [
#              {"name": "はたく", "damage": 50},
#              {"name": "のしかかり", "damage": 100},
#              {"name": "なきごえ", "damage": 10},
#              {"name": "どくどく", "damage": 30}
#          ]


# class Pikachu(Pokemon):
#     def __init__(self, level):
#         super().__init__(level, "でんき", "ピカチュウ")
#         self.hp += 4 * level
#         self.speed += 4 * level
#         self.pikachu_waza = [
#              {"name": "でんきショック", "damage": 50},
#              {"name": "ボルテッカー", "damage": 100},
#              {"name": "しっぽをふる", "damage": 10},
#              {"name": "たいあたり", "damage": 20}
#          ]

def main():

    #敵と遭遇（野生）
    creature_enemy = Pokemon(50, b["onna_status"])
    # creature_enemy.hp = creature_enemy.hp
    print(f"野生の{creature_enemy.name}が現れた！")


    #自分のポケモン出す
    creature_friend = Pokemon(50, b["pikachu_status"])
    # creature_friend.hp = creature_friend.hp
    print(f"行っておいで、{creature_friend.name}! \n")

    # creature_friend.waza = creature_friend.waza
    # creature_enemy.waza = creature_enemy.waza



    while True:    #どちらかが倒れるまで繰り返す

        print(f"{creature_friend.name}はどうする？")
        print("0~3の番号で技を選択")
        for i in range(4):
            print("[" + str(creature_friend.waza[i]["waza_name"]) + "]") 

        n = int(input())
        r = random.randint(0, 3)

        if creature_friend.speed >= creature_enemy.speed:

            creature_enemy.hp -= creature_friend.waza[n]["damage"]
            print(f"{creature_friend.name} の {creature_friend.waza[n]['waza_name']} こうげき！")
            print(f"{creature_enemy.name} に {creature_friend.waza[n]['damage']} のダメージ！")
            
            #自分の攻撃ターン


            if creature_enemy.hp <= 0:
                print(f"野生の{creature_enemy.name}はたおれた！")
                break

            else:
                print(f"{creature_enemy.name} 残りHP {creature_enemy.hp} \n")

                creature_friend.hp -= creature_enemy.waza[r]["damage"]
                print(f"{creature_enemy.name} の {creature_enemy.waza[r]['waza_name']} こうげき！")
                print(f"{creature_friend.name} に {creature_enemy.waza[r]['damage']} のダメージ！")
                print(f"{creature_friend.name} 残りHP {creature_friend.hp} \n")
                #相手の攻撃ターン

                if creature_friend.hp <= 0:
                    print(f"{creature_friend.name}はたおれた！")
                    break



        
        else:
            creature_friend.hp -= creature_enemy.waza[r]["damage"]
            print(f"{creature_enemy.name} の {creature_enemy.waza[r]['waza_name']} こうげき！")
            print(f"{creature_friend.name} に {creature_enemy.waza[r]['damage']} のダメージ！")

            #相手の攻撃ターン

            
            if creature_friend.hp <= 0:
                print(f"{creature_friend.name}はたおれた！")
                break
            
            else:
                print(f"{creature_friend.name} 残りHP {creature_friend.hp} \n")
                
                creature_enemy.hp -= creature_friend.waza[n]["damage"]
                print(f"{creature_friend.name} の {creature_friend.waza[n]['waza_name']} こうげき！")
                print(f"{creature_enemy.name} に {creature_friend.waza[n]['damage']} のダメージ！")
                print(f"{creature_enemy.name} 残りHP {creature_enemy.hp} \n")
                #自分の攻撃ターン

                if creature_enemy.hp <= 0:
                    print(f"野生の{creature_enemy.name}はたおれた！")
                    break

if __name__ == "__main__":
    main()






# pprint.pprint(b)
