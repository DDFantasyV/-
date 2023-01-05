# heuer-score
哈尔滨工程大学精简成绩查询（导出为excel）  <br>

# 使用教程：  <br>

## 1.安装依赖
创建**python虚拟环境**后，使用控制台终端cd到当前目录，使用以下代码进行依赖安装。  <br>
```
pip install -r requirements.txt
```

## 2.获取cookie信息  <br>
(1)进入https://jwgl.wvpn.hrbeu.edu.cn/jwapp/sys/cjcx/*default/index.do?EMAP_LANG=zh#/cjcx ,使用统一认证系统登录并进入成绩查询系统；  <br>
(2)使用浏览器的**开发者选项**获取cookie，具体操作流程如下图。  <br>

### 图片教程  <br>
![D 2SC9}POG%_U4U46)`C$AD](https://user-images.githubusercontent.com/101975462/210775683-4f531174-86a9-4aeb-b1ee-e4b401da9f69.png)  <br>

## 3.更新程序cookie信息  <br>
将第一步获取到的cookie信息输入程序中，运行即可。输出文件目录默认在程序同一目录下，文件名为*data.elsx*.  <br>

# 已实现功能  <br>
-获取成绩列表(包括开课学院、课程名、学分、课程类型、成绩等)  <br>
-导出为excel  <br>

# 待实现功能  <br>
-模拟登录  <br>
