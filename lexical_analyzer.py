import re
import tkinter as tk
from tkinter import filedialog

# 定义关键字和标识符的正则表达式
keywords = [ 'if','then','else','int','char','for']
identifiers=[]
identifier_pattern = r'[a-zA-Z_][a-zA-Z0-9_]*'

# 定义分隔符和算术运算符的正则表达式
separators=['(',')','{','}',';',',','"']
separator_pattern = r'[\(\)\{\};,\'"]'
operators=['+','-','*','/','%','=','<','>','>=','<=','==']
operator_pattern = r'\+|\-|\*|\/|\%|\=|\<|\>|\>\=|\<\=|\=\='

# 定义常数的正则表达式
integers=[]
integer_pattern = r'[0-9]+'

# 定义注释的正则表达式
comment_pattern = r'(/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/)|(//.*)'

#定义映射关系
my_dict = {'keywords': '1', 'separator':'2', 'operator': '3','integer':'4','identifier':'5'}

# 定义词法分析器函数
def lex(code):
    tokens = []
    i = 0
    while i < len(code):
        # 跳过空格和换行符
        if code[i].isspace():
            i += 1
            continue

        # 匹配关键字和标识符
        match = re.match(identifier_pattern, code[i:])
        if match:
            word = match.group(0)
            if word in keywords:
                tokens.append((word, my_dict['keywords']+str(keywords.index(word) + 1)))
            else:
                if word not in identifiers:
                    identifiers.append(word)
                tokens.append((word, my_dict['identifier']+str(identifiers.index(word)+1)))                
            i += len(word)
            continue

        # 匹配分隔符
        match=re.match(separator_pattern,code[i:])
        if match:
            separator=match.group(0)
            tokens.append((separator,my_dict['separator']+str(separators.index(separator)+1)))
            i += len(separator)
            continue

        # 匹配运算符
        match=re.match(operator_pattern,code[i:])
        if match:
            operator=match.group(0)
            tokens.append((operator,my_dict['operator']+str(operators.index(operator)+1)))
            i += len(operator)
            continue
        
        # 匹配数字
        match = re.match(integer_pattern,code[i:])
        if match:
            integer=match.group(0)
            if integer not in integers:
                integers.append(integer)
            tokens.append((integer, my_dict['integer']+str(integers.index(integer)+1)))
            i += len(match.group(0))
            continue

        # 无法识别
        tokens.append((code[i],'error'))
        i += 1
    return tokens

# 创建一个窗口
root = tk.Tk()

# 添加一个文本框，用于显示分析结果
text_box = tk.Text(root, height=40, width=80)
text_box.pack()

# 添加一个按钮，用于选择文件
def select_file():
    # 打开文件选择对话框
    file_path = filedialog.askopenfilename()
    # 如果用户选择了文件，则读取文件内容并进行词法分析
    if file_path:
        with open(file_path, 'r') as file:
            code = file.read()
            # 移除注释
            code = re.sub(comment_pattern, '', code)
            # 进行词法分析
            tokens = lex(code)
            # 在文本框中显示分析结果
            text_box.delete('1.0', tk.END)
            for token in tokens:
                text_box.insert(tk.END, str(token) + '\n')
            text_box.insert(tk.END, '常数表:')
            for integer in integers:
                text_box.insert(tk.END, str(integer) + ',')
            text_box.insert(tk.END, '\n变量表:')
            for identifer in identifiers:
                text_box.insert(tk.END,str(identifer)+',')

button = tk.Button(root, text='选择文件', command=select_file)
button.pack()
