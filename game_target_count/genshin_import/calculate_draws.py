"""
    原作/策划：小猫头鹰
    利用AI：豆包
"""
import tkinter as tk
from tkinter import messagebox


def calculate_draws():
    # 创建主窗口
    root = tk.Tk()
    root.title("抽卡计算器")
    root.geometry("400x400")

    # 存储输入框和复选框的变量
    input_vars = []
    checkbox_vars = []

    # 设置列权重，使界面可伸缩
    root.columnconfigure(0, weight=3)  # 字段标签占3份
    root.columnconfigure(1, weight=1)  # 输入框占1份
    root.columnconfigure(2, weight=1)  # 复选框占1份

    # 创建顶部标签
    headers = ["主要字段", "数量", "选择框"]
    for col, header in enumerate(headers):
        tk.Label(root, text=header, font=('Arial', 10, 'bold')).grid(row=0, column=col, padx=10, pady=5, sticky='w')

    # 定义输入字段数据
    fields = [
        "请输入原石数量：",
        "请输入纠缠之缘数量：",
        "请输入星辉数量：",
        "请输入垫的数量：",
        "请输入创世结晶数量："
    ]

    # 创建输入框和复选框
    for i, field in enumerate(fields, start=1):
        # 字段标签
        tk.Label(root, text=field).grid(row=i, column=0, padx=10, pady=5, sticky='w')

        # 输入框
        input_var = tk.StringVar()
        input_entry = tk.Entry(root, textvariable=input_var, width=10)
        input_entry.grid(row=i, column=1, padx=10, pady=5)

        # 复选框
        checkbox_var = tk.BooleanVar()
        input_checkbox = tk.Checkbutton(root, variable=checkbox_var)
        input_checkbox.grid(row=i, column=2, padx=10, pady=5)

        input_vars.append(input_var)
        checkbox_vars.append(checkbox_var)

    # 计算按钮
    calculate_button = tk.Button(root, text="计算", command=lambda: calculate_sum(input_vars, checkbox_vars))
    calculate_button.grid(row=len(fields) + 1, column=0, columnspan=3, pady=20)

    # 显示结果的标签
    result_label = tk.Label(root, text="目前可用抽数: ")
    result_label.grid(row=len(fields) + 2, column=0, columnspan=3, pady=10)

    def calculate_sum(input_vars, checkbox_vars):
        try:
            sum_value = 0
            # 处理输入框1（原石）和5（创世结晶）的值，分别除以160
            value1 = float(input_vars[0].get()) / 160 if checkbox_vars[0].get() else 0
            value5 = float(input_vars[4].get()) / 160 if checkbox_vars[4].get() else 0

            # 处理输入框3（星辉）的值，除以5（退一法）
            value3 = int(float(input_vars[2].get()) / 5) if checkbox_vars[2].get() else 0

            # 累加其他框的值
            value2 = float(input_vars[1].get()) if checkbox_vars[1].get() else 0
            value4 = float(input_vars[3].get()) if checkbox_vars[3].get() else 0

            # 计算总和
            sum_value = value1 + value2 + value3 + value4 + value5
            result_label.config(text=f"目前可用抽数: {sum_value:.2f}")  # 保留两位小数
            print(f"目前可用抽数: {sum_value:.2f}")
        except ValueError:
            messagebox.showerror("输入错误", "请输入有效的数字")
        except Exception as e:
            messagebox.showerror("计算错误", f"发生未知错误: {str(e)}")

    # 运行主循环
    root.mainloop()


if __name__ == '__main__':
    calculate_draws()