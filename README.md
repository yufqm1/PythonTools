# PythonTools
日常小工具，提高工作效率

1. File serialization: 批量解压某一文件夹下的压缩文件，解压后存放在指定文件夹。
场景：百度云下载的大量压缩文件，需一个个手动解压很不友好
问题：执行程序出现No module named 'rarfile'，首先python环境中需有rarfile、unrar模块，可使用pip/pip3 list
	查看安装的模块中是否有之。安装方法pip/pip3 install rarfile/unrar，安装完后依旧存在问题，windows上考虑是否已经安装了
	WinRAR，需安装上，且将其设置为系统环境变量，或将WinRAR.exe、UnRAR.exe拷贝到python执行文件同目录。linux上应该也是未找到对应的rar执行文件，可自行检查。

