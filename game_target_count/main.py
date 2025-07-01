from object_set.game_target_count.genshin_import import main as genshin_import
from object_set.game_target_count.honkai_import_3 import main as honkai_import_3
from object_set.game_target_count.zenless_zone_zero import main as zenless_zone_zero
from object_set.game_target_count.star_rail import main as star_rail

# 译为 游戏目标计算

def main():
    judgement = input("请输入需要计算测试的游戏（不清楚如何输入请输入 l）：")
    judgement = judgement.lower()
    # ！缩写不能只写大写，否则程序会识别不到缩写
    if judgement in ["原神","genshin","GI","gi","genshin impact"]:
        genshin_import.main()
    elif judgement in ["崩坏3","honkai","HI3","hi3","honkai 3rd"]:
        honkai_import_3.main()
    elif judgement in ["绝区零","ZZZ","zzz","zenless zone zero"]:
        zenless_zone_zero.main()
    elif judgement in ["崩坏：星穹铁道","SR","sr","star rail"]:
        star_rail.main()
    elif judgement in "l":
        l()
        main()
    else:
        print("输入的游戏未找到对应计算函数。以下是可选游戏：")
        l()
        main()

    # 询问用户是否继续
    while True:
        choice = input("是否要重新启动游戏目标计算？(y/n): ").lower()
        if choice == 'y':
            main()
            break
        elif choice == 'n':
            print("程序已退出。")
            break
        else:
            print("输入无效，请输入 'y' 或 'n'。")


def l():
    games = {
        genshin_import:["原神","genshin","GI","genshin impact"],
        honkai_import_3:["崩坏3","honkai","HI3","honkai 3rd"],
        zenless_zone_zero:["绝区零","ZZZ","zzz","zenless zone zero"],
        star_rail:["崩坏：星穹铁道","SR","star rail"]
    }
    for func, values in games.items():
        print(f"※ 游戏名：【{values[0]}】，对应可选项：{values}")


if __name__ == '__main__':
    main()
