<!--
 * @Author: Mr.Car
 * @Date: 2023-11-30 16:56:07
-->
# pythonHTML2csv

Batch program to convert HTML to CSV

The purpose of this code is to convert all HTML files in a folder into CSV format and save them in a specified output path. If any errors occur during the conversion process, the names of these files will be recorded in a failure list file.

这段代码的目的是将一个文件夹中的所有 HTML 文件转换为 CSV 格式，并将它们保存在指定的输出路径中。如果转换过程中出现错误，这些文件名会被记录在一个失败列表文件中。


## 使用方式

需要准备：
1. 获取到batchHTML2CSV.ext的访问地址：`path/to/batchHTML2CSV.exe`
2. 获取到需要转化的文件夹地址 `path/to/someDir`

打开 windows powershell，键入如下指令

```
path/to/batchHTML2CSV.exe path/to/someDir
```

则会在 bathchHTML 同级别的目录下，获得存放结果文件的 out 文件夹

Tips：
1. 可以通过`-h`访问帮助信息
2. 可以指定输出目录