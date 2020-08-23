import os
import sys
import configparser
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QInputDialog, QMessageBox, QTableWidgetItem
from tkinter_demo.dyeProcess.DyeProcess import DyeProcess
from tkinter_demo.dyeProcess.default_process import *
from tkinter_demo.dyeProcess.windows import *


class MyMainWindows(QMainWindow, Ui_MainWindow):
    '''主窗口控制类'''
    newProjectName = None
    dyeProcessList = []

    def __init__(self, parent=None):
        super(MyMainWindows, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("绘制升温曲线")
        # 点击打开菜单,触发openMsg函数
        self.actionOpen.triggered.connect(self.openMsg)
        self.actionSave.triggered.connect(self.saveProcess)
        # 点击新建菜单,打开为新建工艺命名窗口
        # self.children = MySetNewProcessNameFrame()
        # self.actionNew.triggered.connect(self.children.show)
        self.actionNew.triggered.connect(self.getNewProjectName)
        # 工艺的增、删、改、插入、上移、下移
        # self.addDefaultProcess(test_dyeing['name'], test_dyeing['process'])
        # self.addDefaultProcess(test_dyeing['name'], test_dyeing['process'])
        self.stepTableShow()
        self.addProcessButton.clicked.connect(self.addProcess)
        self.deleteProcessButton.clicked.connect(self.deleteProcess)
        self.insertProcessButton.clicked.connect(self.insertProcess)
        self.processUpButton.clicked.connect(self.processUp)
        self.processDownButton.clicked.connect(self.processDown)
        # 工艺列表的信号
        self.processList.itemDoubleClicked.connect(self.editProcessListItem)
        self.processList.itemClicked.connect(self.stepTableShow)
        # 具体步骤的增加
        self.keep_T_button.clicked.connect(self.addKeepTSept)
        self.change_T_button.clicked.connect(self.changeTSept)
        # self.keep_T_button.clicked.connect(self.addKeepTSept)
        # self.keep_T_button.clicked.connect(self.addKeepTSept)

    def addKeepTSept(self):
        '''添加一步保温步骤'''
        nowItemRow = self.processList.currentRow()
        if nowItemRow == -1:
            ItemCount = self.processList.count()
            if ItemCount == 0:
                # 还没有新建工艺就新建一个,确认建立就继续,没建立就返回
                if self.addProcess(None):
                    pass
                else:
                    return False
            elif ItemCount == 1:
                self.processList.setCurrentRow(0)
            else:
                QMessageBox.warning(self, '未选择工艺', '请从左侧工艺栏选择要添加步骤的工艺!')
                return False
        else:
            pass
        T = self.keep_T.value()
        time = self.keep_T_time.value()
        keepTsept = {
            'step_type': '保温',
            'template': T,
            'keep_T_time': time,
            'change_heat_rate': None,
            'goods_name': None,
            'add_goods_time': None,
        }
        self.dyeProcessList[nowItemRow].add_step(keepTsept)
        self.stepTableShow()

    def changeTSept(self):
        '''添加一步保温步骤'''
        nowItemRow = self.processList.currentRow()
        if nowItemRow == -1:
            ItemCount = self.processList.count()
            if ItemCount == 0:
                # 还没有新建工艺就新建一个,确认建立就继续,没建立就返回
                if self.addProcess(None):
                    pass
                else:
                    return False
            elif ItemCount == 1:
                self.processList.setCurrentRow(0)
            else:
                QMessageBox.warning(self, '未选择工艺', '请从左侧工艺栏选择要添加步骤的工艺!')
                return False
        else:
            pass
        T = self.change_T.value()
        change_heat_rate = self.change_T_rate.value()
        keepTsept = {
            'step_type': '变温',
            'template': T,
            'keep_T_time': None,
            'change_heat_rate': change_heat_rate,
            'goods_name': None,
            'add_goods_time': None,
        }
        self.dyeProcessList[nowItemRow].add_step(keepTsept)
        self.stepTableShow()

    def stepTableShow(self):
        '''刷新显示具体工艺步骤的列表'''
        ItemCount = self.processList.count()
        if ItemCount != 0:
            nowItemRow = self.processList.currentRow()
            # print(nowItemRow)
            process = self.dyeProcessList[nowItemRow].process
            # print(id(self.dyeProcessList[nowItemRow]))
        else:
            return
        # print(process)
        self.stepTable.setRowCount(len(process))
        for row in range(0, len(process)):
            step_type = process[row]['step_type']
            if step_type == '保温':
                T_Item = QTableWidgetItem(step_type)
                self.stepTable.setItem(row, 0, T_Item)
                Template = QTableWidgetItem(str(process[row]['template']) + '℃')
                self.stepTable.setItem(row, 1, Template)
                keep_time = QTableWidgetItem(str(process[row]['keep_T_time']) + 'min')
                self.stepTable.setItem(row, 2, keep_time)
                change_heat_rate = QTableWidgetItem('-')
                self.stepTable.setItem(row, 3, change_heat_rate)
            if step_type == '变温':
                T_Item = QTableWidgetItem(step_type)
                self.stepTable.setItem(row, 0, T_Item)
                Template = QTableWidgetItem(str(process[row]['template']) + '℃')
                self.stepTable.setItem(row, 1, Template)
                keep_time = QTableWidgetItem('-')
                self.stepTable.setItem(row, 2, keep_time)
                change_heat_rate = QTableWidgetItem(str(process[row]['change_heat_rate']) + '℃/min')
                self.stepTable.setItem(row, 3, change_heat_rate)
            if step_type == '加料':
                T_Item = QTableWidgetItem(process[row]['goods_name'])
                self.stepTable.setItem(row, 0, T_Item)
                Template = QTableWidgetItem(str(process[row]['template']) + '℃')
                self.stepTable.setItem(row, 1, Template)
                keep_time = QTableWidgetItem(str(process[row]['add_goods_time']) + 'min')
                self.stepTable.setItem(row, 2, keep_time)
                change_heat_rate = QTableWidgetItem('-')
                self.stepTable.setItem(row, 3, change_heat_rate)
            if step_type == '排水':
                T_Item = QTableWidgetItem(step_type)
                self.stepTable.setItem(row, 0, T_Item)
                Template = QTableWidgetItem(str(process[row]['template']) + '℃')
                self.stepTable.setItem(row, 1, Template)
                keep_time = QTableWidgetItem('-')
                self.stepTable.setItem(row, 2, keep_time)
                change_heat_rate = QTableWidgetItem(str(process[row]['change_heat_rate']) + '℃/min')
                self.stepTable.setItem(row, 3, change_heat_rate)

    def processDown(self):
        '''工艺下移'''
        ItemCount = self.processList.count()
        nowItemRow = self.processList.currentRow()
        if nowItemRow == ItemCount - 1:
            pass
        else:
            nowItem = self.processList.takeItem(nowItemRow)
            self.processList.insertItem(nowItemRow + 1, nowItem)
            self.processList.setCurrentRow(nowItemRow + 1)

    def processUp(self):
        '''工艺上移'''
        ItemCount = self.processList.count()
        nowItemRow = self.processList.currentRow()
        if nowItemRow == 0:
            pass
        else:
            nowItem = self.processList.takeItem(nowItemRow)
            self.processList.insertItem(nowItemRow - 1, nowItem)
            self.processList.setCurrentRow(nowItemRow - 1)

    def editProcessListItem(self):
        '''双击编辑工艺名称'''
        nowItem = self.processList.currentItem()
        nowItem.editItem()

    def insertProcess(self):
        '''插入工艺'''
        nowItemRow = self.processList.currentRow()
        ItemCount = self.processList.count()
        newProcessName, ok = QInputDialog.getText(self, '新建工艺', '请输入新工艺名称')
        if ok:
            if nowItemRow == -1:
                self.processList.insertItem(0, newProcessName)
            else:
                self.processList.insertItem(nowItemRow, newProcessName)
        else:
            pass

    def deleteProcess(self):
        '''删除工艺'''
        nowItem = self.processList.currentItem()
        ItemCount = self.processList.count()
        nowItemRow = self.processList.currentRow()
        if nowItemRow == -1:
            if ItemCount == 0:
                QMessageBox.warning(self, '提示', '当前工艺列表中没有工艺可以删除!')
            else:
                QMessageBox.warning(self, '提示', '请选择要删除的工艺!')
        else:
            self.processList.takeItem(nowItemRow)

    def addProcess(self, processName):
        '''添加工艺'''
        if processName:
            newProcessName = processName
            ok = True
        else:
            newProcessName, ok = QInputDialog.getText(self, '新建工艺', '请输入新工艺名称')
        if ok:
            self.dyeProcessList.append(DyeProcess(newProcessName))
            self.processList.addItem(newProcessName)
            self.statusbar.showMessage('添加新工艺:{}'.format(newProcessName))
            ItemCount = self.processList.count()
            self.processList.setCurrentRow(ItemCount - 1)
            self.stepTableShow()
            return True
        else:
            return False

    def addDefaultProcess(self, processName, process):
        '''添加默认工艺'''
        self.dyeProcessList.append(DyeProcess(processName, process))
        self.processList.addItem(processName)
        self.statusbar.showMessage('添加新工艺:{}'.format(processName))
        ItemCount = self.processList.count()
        self.processList.setCurrentRow(ItemCount - 1)
        self.stepTableShow()
        # print(self.dyeProcessList[0].name)

    def saveProcess(self):
        '''保存工艺到文件'''

        if self.newProjectName:
            DirPath = os.getcwd() + '\saveProcess\\' + self.newProjectName
            file, ok = QFileDialog.getSaveFileName(self, '保存', DirPath, 'Dyep Files(*.dyep)')
        else:
            self.newProjectName, newok = QInputDialog.getText(self, '新建项目', '请输入新项目名称')
            if self.newProjectName and newok:
                DirPath = os.getcwd() + '\saveProcess\\' + self.newProjectName
                file, ok = QFileDialog.getSaveFileName(self, '保存', DirPath, 'Dyep Files(*.dyep)')
            else:
                ok = False
        # 点击了确认键才可以保存
        if ok:
            config = configparser.ConfigParser()
            print('初始化config')
            # 写入文件
            # config['ProjectName'] = self.newProjectName
            # config['process'] = self.dyeProcessList
            Process = []
            for oneProcess in self.dyeProcessList:
                Process.append({
                    'processName': oneProcess.name,
                    'process': oneProcess.process,
                })
            config['Project'] = {'ProjectName': self.newProjectName,
                                 'dyeProcessList': Process}

            print(config)
            with open(file, 'w') as configfile:
                config.write(configfile)
            self.statusbar.showMessage('保存成功:{}'.format(file))
        else:
            pass

    def openMsg(self):
        '''打开工艺文件'''
        DirPath = os.getcwd() + '\saveProcess'
        file, ok = QFileDialog.getOpenFileName(self, '打开', DirPath, 'Dyep Files(*.dyep)')
        self.statusbar.showMessage(file)

    def getNewProjectName(self):
        '''新建项目'''
        # if len(self.dyeProcessList):
        # QMessageBox.warning(self, '提示', '请选择要删除的工艺!', buttons=QMessageBox.No)

        self.newProjectName, ok = QInputDialog.getText(self, '新建项目', '请输入新项目名称')
        if ok and self.newProjectName:
            self.statusbar.showMessage(self.newProjectName)
            self.setWindowTitle("{}-绘制升温曲线".format(self.newProjectName))
            self.dyeProcessList = []
            self.stepTable.clear()
            self.processList.clear()
            self.stepTable.setHorizontalHeaderLabels(['项目', '温度', '时间', '速率'])
            return True
        else:
            return False


# class MySetNewProcessNameFrame(QMainWindow, Ui_setNewProcessNameForm):
#     newProcessName = 'default'
#
#     def __init__(self, parent=None):
#         super(MySetNewProcessNameFrame, self).__init__()
#         self.setupUi(self)
#
#         self.ok_button.clicked.connect(self.setNewprocessName)
#         self.close_button.clicked.connect(self.close)
#
#     def setNewprocessName(self):
#         if self.newName_lineEdit:
#             newProcessName = self.newName_lineEdit.text
#             self.label.setText(newProcessName)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywin = MyMainWindows()
    mywin.show()
    sys.exit(app.exec_())
