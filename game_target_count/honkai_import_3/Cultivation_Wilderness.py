"""
文件译为：荒野育成手记
荒野育成手记是 崩坏3 在原画集活动中的主要活动。
"""

import datetime

def level_3_7_8():
    # 定义最终值
    end = 80000
    now = int(input("请输入当前值："))
    # 计算差值
    difference = end - now
    print("目前的差值是：", difference)
    """
        rice = 水稻
        wheat = 小麦
        frequency = 次数
        amount = 金额
        physical = 体力
        sow = 播种
        watering = 浇水
        harvest = 收割
    """
    # 售价
    rice_amount = 700
    wheat_amount = 400
    star_tomato_amount = 40
    # 体力消耗
    physical_sow = 1
    physical_watering = physical_harvest = 9

    rice_frequency = difference / rice_amount
    print("只种水稻需要种", rice_frequency, "个。")
    physical_r_f = rice_frequency * (physical_sow + physical_watering + physical_harvest)
    print("纯计算所得体力结果：", physical_r_f)

    def rice_phy():
        over_sow = int(input("请输入已播种水稻："))
        over_watering = int(input("请输入已浇水水稻："))
        # 计算已播种的水稻还需要多少体力
        sowed: int = over_sow * (physical_watering + physical_harvest)
        # print(sowed)
        # 计算已浇水的水稻还需要多少体力
        watered: int = over_watering * physical_harvest
        # print(watered)
        # # 计算意外值体力之和
        # num = sowed + watered

        end_num_all = rice_frequency - (over_sow + over_watering)
        end_num_all_product = end_num_all * (physical_sow + physical_watering + physical_harvest)
        end_num = end_num_all_product + sowed + watered
        print("需要体力：", end_num)
        # 计算所需体力
        print("\n下一步准备调试时间函数程序正确性：\n")

        def time_honkai3():
            now_physical = int(input("当前体力："))
            time_1 = 90
            # reverse 反向   计算的是精确的还需要的体力值
            now_physical_reverse = end_num - now_physical
            physical_seconds = now_physical_reverse * time_1
            # 体力刷新需要时间（秒）
            print("体力刷新所需秒：", physical_seconds)
            print("体力刷新所需分钟：", physical_seconds / 60)
            print("体力刷新所需小时：", physical_seconds / 3600)
            # 获取当前时间
            current_time = datetime.datetime.now()
            # 计算下一次体力刷新时间
            next_refresh_time = current_time + datetime.timedelta(seconds=physical_seconds)
            # 计算距离下次刷新体力的时间差
            time_difference = next_refresh_time - current_time
            print(f"距离体力满足要求还有 {time_difference}。")
            print(f"体力将在{next_refresh_time}满足要求。")

        time_honkai3()

    judgement_hi = input("是否要继续调试程序（是y否n）：")
    if judgement_hi == "y":
        rice_phy()
    elif judgement_hi == "n":
        pass
    else:
        print("请正确输入！")

def level_4_7_8():
    def fishing():
        # 定义最终值
        num_all = 10
        num = int(input("请输入已经完成的钓鱼次数："))
        # 计算鱼饵需要的体力
        physical_fish = (num_all - num) * 45
        print("钓鱼需要的体力：", physical_fish)
        # 计算鱼饵需要的时间
        time_1 = 90
        fish_seconds = physical_fish * time_1
        print("鱼饵需要的时间：", fish_seconds)
        # 计算距离下次刷新体力的时间差
        current_time = datetime.datetime.now()
        next_refresh_time = current_time + datetime.timedelta(seconds=fish_seconds)
        time_difference = next_refresh_time - current_time
        print(f"距离体力满足要求还有 {time_difference}。")
        print(f"体力将在{next_refresh_time}满足要求。")

    def mining():
        # 定义最终值
        num_all = 15
        num = int(input("请输入已经完成的挖矿次数："))
        # 计算矿石需要的体力
        physical_mine = (num_all - num) * 9
        print("挖矿需要的体力：", physical_mine)
        # 计算矿石需要的时间
        time_1 = 90
        mine_seconds = physical_mine * time_1
        print("矿石需要的时间：", mine_seconds)
        # 计算距离下次刷新体力的时间差
        current_time = datetime.datetime.now()
        next_refresh_time = current_time + datetime.timedelta(seconds=mine_seconds)
        time_difference = next_refresh_time - current_time
        print(f"距离体力满足要求还有 {time_difference}。")
        print(f"体力将在{next_refresh_time}满足要求。")

    fishing()
    print("【※=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=※】")
    mining()

