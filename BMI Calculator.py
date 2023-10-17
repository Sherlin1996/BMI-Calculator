#BMI = 體重(公斤) / 身高(公尺)平方
# 過輕:BMI < 18.5
# 正常:18.5<=BMI<24
# 過重：24<=BMI<27
name = input("請輸入你的名字: ")
high = pow(round(int(input("請輸入你的體重身高:  "))*0.01,2),2)
weight = int(input("請輸入你的體重:  "))
BMI = weight/high 
if BMI>0:
    if(BMI<18.5):
        print(name +",你的體重過輕，你需要再吃營養些，讓自己重一些！")
    elif (BMI<=24):
        print(name +", 你是正常體重!")
    elif (BMI<27):
        print(name +", 你的體重過重.")
    elif (BMI<30):
        print(name +", 你有輕度肥胖.")
    elif (BMI<35):
        print(name +", 你有中度肥胖.")
    else:
        print(name +",你有重度肥胖")
else:
    print("請正確輸入。")