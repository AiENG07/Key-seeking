import datetime

def is_leap_year(year):
    """判断是否为闰年"""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def generate_birthday_dict(start_year=1900, end_year=2024):
    birthday_list = []

    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            if month == 2:
                # 二月份，闰年有29天，平年有28天
                day_range = range(1, 30) if is_leap_year(year) else range(1, 29)
            elif month in [4, 6, 9, 11]:
                # 4, 6, 9, 11月有30天
                day_range = range(1, 31)
            else:
                # 其他月份有31天
                day_range = range(1, 32)
            
            for day in day_range:
                date_str = f"{year:04d}{month:02d}{day:02d}"  # 格式化为YYYYMMDD
                birthday_list.append(date_str)

    return birthday_list

# 生成生日字典
birthdays = generate_birthday_dict()

# 打印出生日字典中的一些条目
for birthday in birthdays[-10:]:  # 打印前10个生日
    print(birthday)

# 可以根据需要将列表保存到文件中
# with open('./birthdays_password.txt', 'w') as file:
#     for birthday in birthdays:
#         file.write(f"{birthday}\n")