from genshin_import import main as genshin_import
from honkai_import_3 import main as honkai_import_3
from zenless_zone_zero import main as zenless_zone_zero
from star_rail import main as star_rail

from SMTP import send_email


def main():
    judgement = input("请输入需要计算测试的游戏（不清楚如何输入请输入 l）：")
    judgement = judgement.lower()

    # 游戏类型判断逻辑
    if judgement in ["原神", "genshin", "GI", "gi", "genshin impact"]:
        genshin_import.main()
    elif judgement in ["崩坏3", "honkai", "HI3", "hi3", "honkai 3rd"]:
        honkai_import_3.main()
    elif judgement in ["绝区零", "ZZZ", "zzz", "zenless zone zero"]:
        zenless_zone_zero.main()
    elif judgement in ["崩坏：星穹铁道", "SR", "sr", "star rail"]:
        star_rail.main()
    elif judgement == "l":  # 注意单个是 == ，多个则 in 列表
        l()
        main()
        return  # 递归调用后直接返回，避免重复执行后续逻辑
    else:
        print("输入的游戏未找到对应计算函数。以下是可选游戏：")
        l()
        main()
        return  # 同上，递归调用后返回

    # 询问是否继续
    while True:
        choice = input("是否要重新启动游戏目标计算？(y/n): ").lower()
        if choice == 'y':
            main()
            break
        elif choice == 'n':
            # 优化退出提示，明确说明程序退出
            print("你选择退出游戏目标计算程序，若需使用可再次运行启动。")
            break
        else:
            print("输入无效，请输入 'y' 或 'n'。")


def l():
    games = {
        genshin_import: ["原神", "genshin", "GI", "genshin impact"],
        honkai_import_3: ["崩坏3", "honkai", "HI3", "honkai 3rd"],
        zenless_zone_zero: ["绝区零", "ZZZ", "zzz", "zenless zone zero"],
        star_rail: ["崩坏：星穹铁道", "SR", "star rail"]
    }
    for func, values in games.items():
        print(f"※ 游戏名：【{values[0]}】，对应可选项：{values}")


try:
    main()
except Exception as e:
    print(f"程序出现错误：{e}，你可从头开始运行程序。")
    send_email()
    main()

if __name__ == '__main__':
    main()