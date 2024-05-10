import os
import rarfile
import zipfile

currentPath = os.getcwd()
# 文件列表
zfileList = []
# 读取文件夹内文件
def readDictionary(dictoryName):
    for filename in os.listdir(dictoryName):
        filepath = os.path.join(dictoryName,filename)
        if os.path.isdir(filepath):
            readDictionary(filepath)
        else:
            if filepath.endswith(".zip") or filepath.endswith("rar"):
                zfileList.append(filepath)
                un_rar(filepath)
                print(filepath)
                
#解压压缩文件
def un_rar(file_name):
    rar = rarfile.RarFile(file_name)
    if os.path.isdir(currentPath + "_files"):
        pass
    else:
        os.mkdir(currentPath + "_files")
        
    os.chdir(currentPath + "_files")
    rar.extractall()
    rar.close()
    
def un_zip(filename):
    zipfiles = zipfile.ZipFile(filename)
    if os.path.isdir(filename + "_files"):
        pass
    else:
        os.mkdir(filename+"_files")
    for names in zipfiles.namelist():
        zipfiles.extract(names,filename + "_files/")
    zipfiles.close()

if __name__ == "__main__":
    dictionaryName = "E:\\download-series"
    print("-------------Start-------------")
    readDictionary(dictionaryName)
    print("-------------End-------------")
    
    