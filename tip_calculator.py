# 小费计算器
bill = float(input("请输入餐费金额 (AUD): "))
tip_percent = float(input("请输入小费比例 (%): "))

tip = bill * tip_percent / 100
total = bill + tip

print("------------------------")
print(f"餐费       : ${bill:.2f}")
print(f"小费 ({tip_percent}%) : ${tip:.2f}")
print(f"总金额     : ${total:.2f}")