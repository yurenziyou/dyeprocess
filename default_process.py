"""
-----------------------------------------------------------------
    File Name    : default_process
    Autor        : 愚人自忧-simple
    Date         : 2020/8/21-22:07
    IDE          : PyCharm
    E-mail       : 18392129744@163.com
    function     :
-----------------------------------------------------------------
"""

reactive_dyeing = {
    'name': '活性染色',
    'process': [
        {
            'step_type': '加料',
            'template': 30,
            'keep_T_time': None,
            'change_heat_rate': 3,
            'goods_name': '染料',
            'add_goods_time': 10,
        },
        {
            'step_type': '加料',
            'template': 30,
            'keep_T_time': None,
            'change_heat_rate': 3,
            'goods_name': '1/2元明粉',
            'add_goods_time': 5,
        },
        {
            'step_type': '加料',
            'template': 30,
            'keep_T_time': None,
            'change_heat_rate': 3,
            'goods_name': '1/2元明粉',
            'add_goods_time': 5,
        },
        {
            'step_type': '加料',
            'template': 30,
            'keep_T_time': None,
            'change_heat_rate': 3,
            'goods_name': '纯碱',
            'add_goods_time': 5,
        },
        {
            'step_type': '变温',
            'template': 60,
            'keep_T_time': None,
            'change_heat_rate': 3,
            'goods_name': None,
            'add_goods_time': None,
        },
        {
            'step_type': '保温',
            'template': 60,
            'keep_T_time': 60,
            'change_heat_rate': 3,
            'goods_name': None,
            'add_goods_time': None,
        },
        {
            'step_type': '排水',
            'template': 60,
            'keep_T_time': None,
            'change_heat_rate': 3,
            'goods_name': None,
            'add_goods_time': None,
        }
    ]
}
test_dyeing = {
    'name': '活性染色',
    'process': [
        {
            'step_type': '排水',
            'template': 60,
            'keep_T_time': None,
            'change_heat_rate': 3,
            'goods_name': None,
            'add_goods_time': None,
        }
    ]
}
