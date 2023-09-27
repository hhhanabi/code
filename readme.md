# 词法分析器
### 项目简介
基于正则表达式的词法分析器，其原理是将输入的程序代码字符串进行扫描和分析，识别其中的各种单词符号并将其分类编码。识别单词符号的方法是使用正则表达式对输入字符串进行匹配，根据匹配的结果进行分类编码。同时，为了防止程序中出现注释对识别造成干扰，在识别之前先将注释从程序代码中移除。 
### 状态转换图
<img src="https://github.com/hhhanabi/code/blob/main/1.png">
