
def set_params(name, hit_point, ability):
    return {
        "name": name,
        "hit_point": hit_point,
        "ability": ability
    }


def battle(attacker, reciever, ability_id):
    ability_name = attacker.ability[ability_id]["name"]
    ability_damage = attacker.ability[ability_id]["damage"]
    reciever.hit_point -= ability_damage
    print(f"{attacker.name}の{ability_name}！")
    print(f"{reciever.name}に{ability_damage}のダメージ")


class Pokemon:
    def __init__(self, params):
        self.name = params["name"]
        self.hit_point = params["hit_point"]
        self.ability = params["ability"]


enemy_params = set_params(
        "女", 700, [
            {"name": "はたく", "damage": 50},
            {"name": "のしかかり", "damage": 100},
            {"name": "なきごえ", "damage": 10},
            {"name": "どくどく", "damage": 30}
        ]
    )

friend_params = set_params(
        "ピカチュウ", 500, [
            {"name": "でんきショック", "damage": 50},
            {"name": "ボルテッカー", "damage": 100},
            {"name": "しっぽをふる", "damage": 10},
            {"name": "たいあたり", "damage": 20}
        ]
    )

friend = Pokemon(friend_params)
enemy = Pokemon(enemy_params)

print(f"野生の{enemy.name}が現れた！")
print(f"行け！{friend.name}\n")

term_count = 0

while True:

    # ターンを4で割った余が ability_id
    # 0,1,2,3,0, ... の順で技を呼ぶことにする
    ability_id = term_count % 4

    # ダメージ計算と画面出力を行う
    battle(friend, enemy, ability_id)

    # 相手が倒れたか判定
    if enemy.hit_point <= 0:
        print(f"野生の{enemy.name}はたおれた！")
        break

    # 倒れていなかったら、HPを表示
    print(f"残りHP: {enemy.hit_point}\n")

    # 相手の攻撃ターン

    # ダメージ計算と画面出力を行う
    # friend と enemy が入れ替わっていることに注意
    battle(enemy, friend, ability_id)

    # ピカチュウが倒れたか判定
    if friend.hit_point <= 0:
        print(f"{friend.name}はたおれた！")
        break
    print(f"残りHP: {friend.hit_point}\n")

    # ターンを追加
    term_count += 1
