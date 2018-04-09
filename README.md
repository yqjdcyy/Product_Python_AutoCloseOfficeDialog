

# STATISTIC

|  Type | Situation |           Alert           |                                                                Content                                                                 |      Class      |          Btn           |
|-------|-----------|---------------------------|----------------------------------------------------------------------------------------------------------------------------------------|-----------------|------------------------|
| DOC   | 密码      | password<br/>密码         | 请键入打开文件所需的密码<br/>\\1...\Office 各情况文档\password.docx                                                                    | bosa_sdm_msword | TAB* 2+ ENTER<br/> ESC |
|       | 文件损坏  | Microsoft Word            | 很抱歉，无法打开 error.docx，因为内容有问题。<br/> 详细信息：文件已损坏，无法打开。                                                    | bosa_sdm_msword | ENTER<br/> ESC         |
|       | 修复      | Microsoft Word            | Word 在 error.docx 中发现无法读取的内容。是否恢复此文档的内容？如果您信任此文档的来源，请单击“是”。                                    | #32770 (对话框) | ENTER<br/> ESC         |
|       | ~~只读~~  |                           |                                                                                                                                        |                 |                        |
|       | 未注册    | Microsoft Office 激活向导 |                                                                                                                                        | NetUIHWND       | TAB* 6+ ENTER<br/> ESC |
| PPTX  | 密码      | password<br/>密码         | 输入密码以打开文件<br/>password.pptx<br/>密码（P）：                                                                                   | NUIDialog       | TAB* 2+ ENTER<br/> ESC |
|       | 文件损坏  | Microsoft PowerPoint      | 很抱歉，PowerPoint 无法读取...error.pptx                                                                                               | #32770 (对话框) | ENTER<br/> ESC         |
|       | 修复      | Microsoft PowerPoint      | PowerPoint 发现 ...\fix.pptx 中的内容有问题。<br/>PowerPoint可尝试修复此演示文稿。<br/><br/>如果您信任此演示文稿的来源，请单击“修复”。 | #32770 (对话框) | TAB+ ENTER<br/> ESC    |
|       | ~~只读~~  |                           |                                                                                                                                        |                 |                        |
|       | 未注册    | Microsoft Office 激活向导 |                                                                                                                                        | NUIDialog       | TAB* 6+ ENTER<br/> ESC |
| EXCEL | 密码      | 密码                      | "password.xlsx"有密码保护                                                                                                              | bosa_sdm_XL9    | TAB* 2+ ENTER<br/> ESC |
|       | 文件损坏  | Microsoft Excel           | Excel 无法打开文件"error.xlsx"，因为文件格式或文件扩展名无效。请确定文件未损坏，并且文件扩展名与文件的格式匹配。                       | #32770 (对话框) | ENTER<br/> ESC         |
|       | ~~修复~~  |                           |                                                                                                                                        |                 |                        |
|       | ~~只读~~  |                           |                                                                                                                                        |                 |                        |
|       | 未注册    |                           |                                                                                                                                        |                 |                        |
		


# CHECK

| Type | Sub-Type | Finissh |
|------|----------|---------|
| XLS  |          |         |
|      | ERROR    | Y       |
|      | PASSWORD | Y       |
| PPT  |          |         |
|      | ERROR    | Y       |
|      | FIX      | Y       |
|      | PASSWORD |         |
| DOC  |          |         |
|      | ERROR    |         |
|      | PASSWORD | Y       |
|      | READONLY |         |