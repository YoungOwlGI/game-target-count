from .Cultivation_Wilderness import level_3_7_8
from .Cultivation_Wilderness import level_4_7_8

def main():
    print("3：田园播种\n4：钓鱼挖矿")
    judgement_level = input("请输入需要计算的游戏模块（3/4）：")
    if judgement_level == "3":
        level_3_7_8()
    elif judgement_level == "4":
        level_4_7_8()
    else:
        print("请正确输入！")
