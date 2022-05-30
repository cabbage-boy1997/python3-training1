
def params_to_dict(name, hit_point, ability):
    """
    与えられた引数を辞書に変換する関数
    Pokemonクラスのインスタンス化に使う
    Args:
        name = (str)ポケモンの名前
        hit_point = (int)ポケモンの体力
        ability = (list)技のリスト、要素は⬇️
            {name: 技の名前、damage: ダメージ}
    Return:
        none
    """
    return {
        "name": name,
        "hit_point": hit_point,
        "ability": ability
    }


def battle(attacker, reciever, ability_id):
    """
    ダメージ計算と画面出力を行う
    Args:
        attacker = 攻撃側のPokemonインスタンス
        reciever = 受け手側のPokemonインスタンス
        ability_id = 呼ぶ技のid（何番目か）
    Return:
        none
    """
    ability_name = attacker.ability[ability_id]["name"]
    ability_damage = attacker.ability[ability_id]["damage"]
    reciever.hit_point -= ability_damage
    print(f"{attacker.name}の{ability_name}！")
    print(f"→ {reciever.name}に{ability_damage}のダメージ")


class Pokemon:
    """
    ポケモンのクラス
    params_to_dict()関数によって辞書化されたパラメータを引数に取る
    """
    def __init__(self, params):
        self.name = params["name"]
        self.hit_point = params["hit_point"]
        self.ability = params["ability"]


# 敵のパラメータを辞書化する
enemy_params = params_to_dict(
        "女", 700, [
            {"name": "はたく", "damage": 50},
            {"name": "のしかかり", "damage": 100},
            {"name": "なきごえ", "damage": 10},
            {"name": "どくどく", "damage": 30}
        ]
    )

# 味方のパラメータを辞書化する
friend_params = params_to_dict(
        "ピカチュウ", 500, [
            {"name": "でんきショック", "damage": 50},
            {"name": "ボルテッカー", "damage": 100},
            {"name": "しっぽをふる", "damage": 10},
            {"name": "たいあたり", "damage": 20}
        ]
    )

# 敵味方それぞれインスタンス化
friend = Pokemon(friend_params)
enemy = Pokemon(enemy_params)

print(f"野生の{enemy.name}が現れた！")
print(f"行け！{friend.name}\n")

# ターンの初期化
term_count = 0

while True:

    print(f"[{term_count}ターン目]")
    # ターンを4で割った余が ability_id
    # 0,1,2,3,0, ... の順で技を呼ぶことにする
    ability_id = term_count % 4

    # ダメージ計算と画面出力を行う
    battle(friend, enemy, ability_id)

    # 相手が倒れたか判定
    # 倒れていない場合何もせず続行するので else は不要
    if enemy.hit_point <= 0:
        print(f"→ 野生の{enemy.name}はたおれた！\n")
        break

    # 倒れていなかったら、HPを表示
    print(f"→ 残りHP: {enemy.hit_point}\n")

    # 相手の攻撃ターン
    # friend と enemy が入れ替えて、戦闘を実行
    battle(enemy, friend, ability_id)

    # 味方が倒れたか判定
    if friend.hit_point <= 0:
        print(f"→ {friend.name}はたおれた！\n")
        break
    print(f"→ 残りHP: {friend.hit_point}\n")

    # ターンに値を追加
    term_count += 1

print("\n戦闘は終了した。")
