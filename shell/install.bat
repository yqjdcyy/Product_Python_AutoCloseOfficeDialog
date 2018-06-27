@echo off

sc create dialog_autoclose_monitor binPath= "C:\Windows\System32\monitor.exe -l -t 2 -d 30" DisplayName= "自动关闭弹窗服务" type= own start= auto
sc start dialog_autoclose_monitor

echo DONE! 
pause