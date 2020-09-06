**01-安装Mysql文档**

# 01-安装第三方库 #

pip install pymysql

## **02-安装Mysql文档** ##

*****01:安装与配置mysql*****
    001:安装mysql
    MySQL 5.7.30 安装与升级问题详细教程
    https://www.jb51.net/article/187601.htm

*## 002:配置环境变量 ##*
    01-下载完成后，解压到你想要安装的目录,比如我的目录是:D:\Program Files (x86)\mysql-5.7.30-winx64
    02-在系统变量path后面追加D:\Program Files (x86)\mysql-5.7.30-winx64\bin
    03-创建配置文件my.ini(my.ini必须保存为ANSI格式(配置文件默认就是是ANSI编码格式)

### 003-mysql的配置 ###
    01-以管理员身份打开命令行
    02-CD到MySQL的bin目录（注意此处一定要到bin目录下去执行)
    03-安装mysql服务器: mysqld --install
    04-初始化mysql : mysqld --initialize --console
    05-启动mysql服务: net start mysql
    06-登录验证, mysql是否安装成功:  mysql -u root -p 
    07-修改密码:  mysqladmin -u root -p password
    08-再次登录验证新密码: mysql -u root -p
    09:关闭服务: net stop mysql























