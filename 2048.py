# -*- coding:utf-8 -*-
from tkinter import *

# 定义行数量和列数量
grid_row_count, grid_col_count = 4, 4

# 定义每个数字格子大小
label_width, label_height = 90, 90

# 定义字体
label_font = ('黑体', 18, 'bold')

# 初始化窗体
tk = Tk()
tk.title('2048')
tk.resizable(False, False)
tk['background'] = '#BBADA0'

import random


def get2or4():
    return random.choice(['2', '4'])


# 初始化格子
label_array = []
for row in range(grid_row_count):
    label_array.append([])
    for col in range(grid_col_count):
        frame = Frame(tk)
        frame['width'] = label_width
        frame['height'] = label_height

        frame_grid_dict = {}
        frame_grid_dict['row'] = row
        frame_grid_dict['column'] = col
        frame_grid_dict['padx'] = 2
        frame_grid_dict['pady'] = 2
        frame.grid(frame_grid_dict)

        label = Label(frame)
        label['text'] = ''
        label['background'] = '#cdc1b4'
        label['foreground'] = '#776e65'
        label['font'] = label_font
        # 添加自定义行列属性
        label.row = row
        label.col = col
        label.oldBackground = None
        # 定义获取2或4函数
        label.get2or4 = get2or4
        label_array[row].append(label)  # 添加到列表

        label_place_dict = {}
        label_place_dict['x'] = 0
        label_place_dict['y'] = 0
        label_place_dict['width'] = label_width
        label_place_dict['height'] = label_height
        label.place(label_place_dict)


def getEmpytLabelList():
    '得到空列表'
    reList = []
    for row in range(grid_row_count):
        for col in range(grid_col_count):
            label = label_array[row][col]
            if label['text'] == '':
                reList.append(label)
    return reList


# 设置随机值
def setRandomLabel(n):
    for label in random.sample(getEmpytLabelList(), n):
        n = label.get2or4()
        label['text'] = n


setRandomLabel(2)


def upAction():
    # 将所有数字向上移动来填补上面空格
    for count in range(grid_row_count):
        for col in range(grid_col_count):
            for row in range(grid_row_count - 1):
                labelA = label_array[row][col]
                labelB = label_array[row + 1][col]
                if labelA['text'] == '' and labelB['text'] != '':
                    # 这个为空,可以将下面数字移动到这个位置
                    labelA['text'] = labelB['text']
                    labelB['text'] = ''
    # 判断是否发生碰幢，如果有碰撞则合并,合并结果靠上，下面填充空格
    for col in range(grid_col_count):
        for row in range(grid_row_count - 1):
            labelA = label_array[row][col]
            labelB = label_array[row + 1][col]
            if labelA['text'] != '' and labelB['text'] != '' and labelA['text'] == labelB['text']:
                labelA['text'] = str(int(labelA['text']) * 2)
                labelB['text'] = ''
    # 将所有数字向上移动来填补上面空格
    for count in range(grid_row_count):
        for col in range(grid_col_count):
            for row in range(grid_row_count - 1):
                labelA = label_array[row][col]
                labelB = label_array[row + 1][col]
                if labelA['text'] == '' and labelB['text'] != '':
                    # 这个为空,可以将下面数字移动到这个位置
                    labelA['text'] = labelB['text']
                    labelB['text'] = ''


def downAction():
    label_array.reverse()
    upAction()
    label_array.reverse()


def leftAction():
    # 将所有数字向左移动来填补上面空格
    for count in range(grid_row_count):
        for row in range(grid_row_count):
            for col in range(grid_col_count - 1):
                labelA = label_array[row][col]
                labelB = label_array[row][col + 1]
                if labelA['text'] == '' and labelB['text'] != '':
                    # 这个为空,可以将右面数字移动到这个位置
                    labelA['text'] = labelB['text']
                    labelB['text'] = ''
    # 判断是否发生碰幢，如果有碰撞则合并,合并结果靠左，右面填充空格
    for row in range(grid_row_count):
        for col in range(grid_col_count - 1):
            labelA = label_array[row][col]
            labelB = label_array[row][col + 1]
            if labelA['text'] != '' and labelB['text'] != '' and labelA['text'] == labelB['text']:
                labelA['text'] = str(int(labelA['text']) * 2)
                labelB['text'] = ''
    # 将所有数字向左移动来填补右面空格
    for count in range(grid_row_count):
        for row in range(grid_row_count):
            for col in range(grid_col_count - 1):
                labelA = label_array[row][col]
                labelB = label_array[row][col + 1]
                if labelA['text'] == '' and labelB['text'] != '':
                    # 这个为空,可以将右面数字移动到这个位置
                    labelA['text'] = labelB['text']
                    labelB['text'] = ''


def rightAction():
    for rowData in label_array:
        rowData.reverse()
    leftAction()
    for rowData in label_array:
        rowData.reverse()


def getScore():
    count = 0
    index = 0
    for row in range(grid_row_count):
        for col in range(grid_col_count):
            index += 1
            label = label_array[row][col]
            text = label['text']
            if text == '':
                text = '0'
            textValue = int(text)
            count = count + textValue * index
    return count


def isHas2048():
    for row in range(grid_row_count):
        for col in range(grid_col_count):
            label = label_array[row][col]
            if label['text'] == '2048':
                return True
    return False


import tkinter.messagebox as box


# 按键响应
def keyAction(keyEvent):
    old_score = getScore()
    keysym = keyEvent.keysym
    if keysym == 'Up':
        upAction()
    elif keysym == 'Down':
        downAction()
    elif keysym == 'Left':
        leftAction()
    elif keysym == 'Right':
        rightAction()
    new_score = getScore()
    success = isHas2048()
    if success == True:
        box.showinfo('提示', '你赢了!')
    else:
        empytList = getEmpytLabelList()
        if len(empytList) > 0:
            if old_score != new_score:
                setRandomLabel(1)
        else:
            box.showinfo('提示', '你输了!')


# 绑定键盘
tk.bind(sequence='<KeyRelease>', func=keyAction)

tk.mainloop()
