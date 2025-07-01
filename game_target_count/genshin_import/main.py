from calculate_draws import calculate_draws

def main():
    print("可选选项：\n")
    judgement_gi = input("请输入 调试方向：")
    if judgement_gi in ["抽卡计算", "cd"]:
        calculate_draws()
    elif judgement_gi == "dc_1":
        pass
    else:
        pass