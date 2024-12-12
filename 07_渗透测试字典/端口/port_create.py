# 定义不同的端口范围
common_ports = [21, 22, 23, 25, 53, 69, 80,8080,3128,8081,9098, 110, 119, 123, 135,137,138,139, 161, 389, 443, 465, 873, 1080, 1158, 1433, 1521, 2100, 3389, 3306, 5432, 5601, 6379, 8080, 8081, 8888, 9000, 9080, 9090, 9200, 10050, 10051, 11211, 27017, 22122]  # 常用端口
enterprise_ports = [21,22,25,3389,53,80,110,143,443,8080,873,1521,2049,27017,3306]  # 企业端口

# 生成全部端口
all_ports = list(range(1, 65536))

# 将端口列表写入文件
def write_ports_to_file(port_list, filename):
    with open(filename, 'w') as f:
        for port in port_list:
            f.write(str(port) + '\n')

# 用户选择
print("请选择要生成的端口列表类型：")
print("1 - 全部端口")
print("2 - 常用端口")
print("3 - 企业端口")
choice = input("输入选项（1/2/3）：")
# choice = '1'  # 这里直接设置choice为1，方便测试

if choice == '1':
    write_ports_to_file(all_ports, './all_ports.txt')
    print("全部端口已生成并保存到 all_ports.txt")
elif choice == '2':
    common_ports_list = list(range(1, 65536))
    common_ports_list = [port for port in common_ports_list if port in common_ports]
    write_ports_to_file(common_ports_list, './common_ports.txt')
    print("常用端口已生成并保存到 common_ports.txt")
elif choice == '3':
    enterprise_ports_list = list(range(1, 65536))
    enterprise_ports_list = [port for port in enterprise_ports_list if port in enterprise_ports]
    write_ports_to_file(enterprise_ports_list, './enterprise_ports.txt')
    print("企业端口已生成并保存到 enterprise_ports.txt")
else:
    print("无效的选择")