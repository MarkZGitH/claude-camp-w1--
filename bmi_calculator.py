# BMI 计算器
height = float(input("请输入身高 (米): "))
weight = float(input("请输入体重 (公斤): "))

bmi = weight / (height ** 2)

print(f"您的 BMI 是: {bmi:.2f}")

if bmi < 18.5:
    print("健康建议: 体重偏轻，建议增加营养摄入。")
elif bmi < 24:
    print("健康建议: 体重正常，请保持健康生活方式。")
elif bmi < 28:
    print("健康建议: 体重超重，建议适量运动。")
else:
    print("健康建议: 肥胖，建议咨询医生制定减重计划。")