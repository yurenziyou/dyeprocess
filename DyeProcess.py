class DyeProcess:
    default_heat_rate = 3
    default_blow_off_water_T = 60
    default_start_T = 30
    '''
         工艺的格式为
            {
            'step_type':'保温','变温','加料','排水',
            'template':30,
            'keep_T_time': 5,
            'change_heat_rate':3,
            'goods_name';'元明粉',
            'add_goods_time':5,
            }
        '''

    def __init__(self, name, process=None):
        self.name = name
        if process:
            self.process = process
        else:
            self.process = []

    def add_step(self, one_steps=None):
        # 在最后面添加一个步骤
        if one_steps:
            self.process.append(one_steps)

    def insert_step(self, index, one_steps=None):
        # 在index位置插入一个步骤
        if one_steps:
            self.process.insert(index, one_steps)

    def delete_step(self, index):
        del self.process[index]

    def __str__(self):
        for step in self.process:
            pass


if __name__ == '__main__':
    process = [{
        'step_type': '保温',
        'template': 30,
        'keep_T_time': 5,
        'change_heat_rate': 3,
        'goods_name': None,
        'add_goods_time': None,
    },
        {
            'step_type': '加料',
            'template': 30,
            'keep_T_time': None,
            'change_heat_rate': 3,
            'goods_name': '元明粉',
            'add_goods_time': 5,
        }, {
            'step_type': '加料',
            'template': 30,
            'keep_T_time': None,
            'change_heat_rate': 3,
            'goods_name': '纯碱',
            'add_goods_time': 5,
        }]
    dyeProcess = DyeProcess('涤纶染色工艺')
    dyeProcess2 = DyeProcess('活性染色工艺')
    print(dyeProcess.process)
    dyeProcess.add_step({'step_type': '变温',
                            'template': 60,
                            'keep_T_time': None,
                            'change_heat_rate': 3,
                            'goods_name': None,
                            'add_goods_time': None, })
    dyeProcess2.add_step({'step_type': '保温',
                             'template': 20,
                             'keep_T_time': 60,
                             'change_heat_rate': 3,
                             'goods_name': None,
                             'add_goods_time': None, })
    # dyeProcess.add_process([90, 3, 60, '', ''])
    print(dyeProcess.process)
    print(dyeProcess2.process)

    # dyeProcess.insert(1, [40, 2, 10, '', ''])
    # dyeProcess.insert(1, [])
    # print(dyeProcess.process)
