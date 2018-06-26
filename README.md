# Call
## 帮助文档
-  `monitor.exe -h`
	```
	monitor.exe
        -h|--help       帮助文档
        -l|--logList    是否打印当前窗口列表
        -t|--type       请求服务类型
                1:      当前窗口列表
                2:      启用监控
                3:      测试参数化运行状态
                4:      测试日志打印
        -d|--duration   运行休眠时长
        -p|--logPath    日志输出文件的绝对路径
	```

## 调用示例
- `monitor.exe -t 2 -d 30`



# STATISTIC
## windows 10
| Type    | Situation    | Alert                     | Content                                                                                                                                | Class           |
|:--------|:-------------|:--------------------------|:---------------------------------------------------------------------------------------------------------------------------------------|:----------------|
| DOC     | 密码         | password<br/>密码         | 请键入打开文件所需的密码<br/>\\1...\Office 各情况文档\password.docx                                                                    | bosa_sdm_msword |
|         | 文件损坏     | Microsoft Word            | 很抱歉，无法打开 error.docx，因为内容有问题。<br/> 详细信息：文件已损坏，无法打开。                                                    | bosa_sdm_msword |
|         | 修复         | Microsoft Word            | Word 在 error.docx 中发现无法读取的内容。是否恢复此文档的内容？如果您信任此文档的来源，请单击“是”。                                    | #32770 (对话框) |
|         | ~~只读~~     |                           |                                                                                                                                        |                 |
|         | 未注册       | Microsoft Office 激活向导 |                                                                                                                                        | NetUIHWND       |
| PPTX    | 密码         | password<br/>密码         | 输入密码以打开文件<br/>password.pptx<br/>密码（P）：                                                                                   | NUIDialog       |
|         | 文件损坏     | Microsoft PowerPoint      | 很抱歉，PowerPoint 无法读取...error.pptx                                                                                               | #32770 (对话框) |
|         | 修复         | Microsoft PowerPoint      | PowerPoint 发现 ...\fix.pptx 中的内容有问题。<br/>PowerPoint可尝试修复此演示文稿。<br/><br/>如果您信任此演示文稿的来源，请单击“修复”。 | #32770 (对话框) |
|         | ~~只读~~     |                           |                                                                                                                                        |                 |
|         | 未注册       | Microsoft Office 激活向导 |                                                                                                                                        | NUIDialog       |
| EXCEL   | 密码         | 密码                      | "password.xlsx"有密码保护                                                                                                              | bosa_sdm_XL9    |
|         | 文件损坏     | Microsoft Excel           | Excel 无法打开文件"error.xlsx"，因为文件格式或文件扩展名无效。请确定文件未损坏，并且文件扩展名与文件的格式匹配。                       | #32770 (对话框) |
|         | ~~修复~~     |                           |                                                                                                                                        |                 |
|         | ~~只读~~     |                           |                                                                                                                                        |                 |
|         | 未注册       |                           |                                                                                                                                        |                 |
|         | 打印机不可用 | Microsoft Excel           | 当前打印机不可用，请选择其它打印机。<br/> 显示帮助(E) >>                                                                               | #32770          |
|         | 保存失败     | Microsoft Excel           | 无法保存该文档。该文档可能已被打开，或者保存时出错。                                                                                   | #32770          |
| Printer | 选择打印机   | 打印机设置                | 打印机(P)：...                                                                                                                         | bosa_sdm_XL9    |

## Windows Service 2008 R2
| Type    | Situation    | Alert                | Content                                                                                                             | Class           |
|:--------|:-------------|:---------------------|:--------------------------------------------------------------------------------------------------------------------|:----------------|
| DOC     | 密码         | 密码                 | 请键入打开文件所需的密码                                                                                            | bosa_sdm_msword |
|         | 文件损坏     | Microsoft Word       | 无法打开文件 *.docx，因为内容有错误<br/>详细信息：文件已损坏，无法打开。                                            | bosa_sdm_msword |
|         | 修复         | Microsoft Word       | Word 在 *.docx 中发现无法读取的内容。是否恢复此文件的内容？如果您信任此文件的来源，请单击“是”                       | #32770          |
|         | ~~只读~~     |                      |                                                                                                                     |                 |
|         | 未注册       |                      |                                                                                                                     |                 |
| PPTX    | 密码         | 密码                 | 输入密码以打开文件<br>*.pptx                                                                                        | #32770          |
|         | 文件损坏     | Microsoft Powerpoint | PowerPoint 发现 *.pptx 中的内容有问题。PowerPoint 可尝试修复此尝试稿。<br/>如果您信任此演示文稿的来源，请单击“修复” | #32770          |
|         | 修复         | Microsoft Powerpoint | PowerPoint 发现 *.pptx 中的内容有问题。PowerPoint 可尝试修复此尝试稿。<br/>如果您信任此演示文稿的来源，请单击“修复” | #32770          |
|         | ~~只读~~     |                      |                                                                                                                     |                 |
|         | 未注册       |                      |                                                                                                                     |                 |
| EXCEL   | 密码         | 密码                 | “*.xlsx”有密码保护。                                                                                                | #32770          |
|         | 文件损坏     | Microsoft Excel      | Excel 无法打开文件“*.xlsx”，因为文件格式或文件扩展名无效。请确定文件未损坏，并且文件扩展名与文件的格式匹配。        | bosa_sdm_XL9    |
|         | ~~修复~~     |                      |                                                                                                                     |                 |
|         | ~~只读~~     |                      |                                                                                                                     |                 |
|         | 未注册       |                      |                                                                                                                     |                 |
|         | 打印机不可用 |                      |                                                                                                                     |                 |
|         | 保存失败     |                      |                                                                                                                     |                 |
| Printer | 选择打印机   |                      |                                                                                                                     |                 |


# SITUATION
## 打印机阻塞
- Printer.选择打印机
- EXCEL.打印机不可用
- EXCEL.保存失败

## 无法运行
```
该版本的 D:\PPT-Convertor-Gateway\tools\office-auto-close.exe 与您运行的 Windows
 版本不兼容。请查看计算机的系统信息，了解是否需要 x86 (32 位)或 x64 (64 位)版本
的程序，然后联系软件发行者。
```

# CHECK
## Windows 10
| Type      | Sub-Type   | Finissh   |
| :-------- | :--------- | :-------- |
| XLS       |            |           |
|           | ERROR      | Y         |
|           | PASSWORD   | Y         |
| PPT       |            |           |
|           | ERROR      | Y         |
|           | FIX        | Y         |
|           | PASSWORD   | Y         |
| DOC       |            |           |
|           | ERROR      | Y         |
|           | PASSWORD   | Y         |
|           | READONLY   | Y         |
| PRINTER   |            |           |
|           | BROKE      | -         |

## Windows Service 2008 R2
| Type      | Sub-Type   | Finissh   |
| :-------- | :--------- | :-------- |
| XLS       |            |           |
|           | ERROR      | Y         |
|           | PASSWORD   | Y         |
| PPT       |            |           |
|           | ERROR      | Y         |
|           | FIX        | Y         |
|           | PASSWORD   |           |
| DOC       |            |           |
|           | ERROR      | Y         |
|           | PASSWORD   | Y         |
|           | READONLY   | Y         |
| PRINTER   |            |           |
|           | BROKE      | -         |


# REFERENCE
- code
	- [yqjdcyy/Utils_Python](https://github.com/yqjdcyy/Utils_Python/blob/master/windows/dialog/README.md)
- SpyXX
	- [SpyXX for windows service 2008 R2](http://web.archive.org/web/20090921065444/http://www.windows-spy.com:80/download/)
	- [SpyXX for Windows 10](http://otzm88f21.bkt.clouddn.com/69e378a2-e871-4c28-9d78-3fe59305c23d.zip)
	- [I want Spy++ but I don't have Visual Studio [closed]](https://stackoverflow.com/questions/1811019/i-want-spy-but-i-dont-have-visual-studio)

