"""
-----------------------------------------------------------------
    File Name    : config
    Autor        : 愚人自忧-simple
    Date         : 2020/8/18-15:51
    IDE          : PyCharm
    E-mail       : 18392129744@163.com
    function     :
-----------------------------------------------------------------
"""
import configparser
import os


# config = configparser.ConfigParser()
# # 写入文件
# config['涤纶染色'] = {
#     '涤纶染色': [[30, '', 80, '', ''], [30, '', 40, '', ''], [90, 3, 60, '', '']],
#     '酸性还原清洗': [[30, '', 80, '', ''], [30, '', 40, '', ''], [90, 3, 60, '', '']],
#     '碱性还原清洗': [[30, '', 80, '', ''], [30, '', 40, '', ''], [90, 3, 60, '', '']],
# }
#
# config['活性酸性套色'] = {
#     '活性染色': [[30, '', 80, '', ''], [30, '', 40, '', ''], [90, 3, 60, '', '']],
#     '酸性染色': [[30, '', 80, '', ''], [30, '', 40, '', ''], [90, 3, 60, '', '']],
# }
#
# with open('text.dyep', 'w') as configfile:
#     config.write(configfile)
# # 写入结束

#
# # 读取配置
# config.read('text.ini')
# # 读取块
# print(config.sections())
# # 读取块内部
# print(config['NAME']['name1'])
# # 查看是否存在
# print(config.has_section('NAME'))
# # 读取结束   >>>True
#
# # 修改配置
# config.set('NAME', 'name3', 'dd')
# # 增加
# config.add_section('ID')
# config.set('ID', 'ID1', '12313312')
# config.write(open('text.ini', 'w'))
#
# # 删除块
# config.remove_section('number')
# config.write(open('text.ini', 'w'))

class tree():
    def __init__(self, name, num):
        self.name = name
        self.num = num


t1 = tree('nayun', 12)
t2 = tree('yanwen', 13)

