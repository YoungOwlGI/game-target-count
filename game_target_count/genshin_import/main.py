from .calculate_draws import calculate_draws

def main():
    print("1：抽卡计算")
    judgement_gi = input("请输入需要计算的游戏模块（1/2）：")
    if judgement_gi == "1":
        calculate_draws()
    elif judgement_gi == "2":
        pass
    else:
        pass