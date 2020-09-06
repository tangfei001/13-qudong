**课时163-Python操作MySQL实战（一）**

# **01-需要安装的库** #
    001:需要安装库 pymysql-- pip3 install pymysql
    002:cilentmysql

## 02:安装mysql文档 ##
### 03:安装Navicat ###
#### 04:mysql与Navicat建立连接 ####

mysql -h localhost -u root - p
-----------------------------------------------------------------------
管理MySQL的命令
 列出 MySQL 数据库管理系统的数据库列表 ：SHOW DATABASES
 使用某个数据库：USE 数据库名
 显示指定数据库的所有表 SHOW TABLES
 显示数据表的属性，属性类型，主键信息 ，是否为 NULL，默认值等其他信息等  SHOW COLUMNS FROM 数据表	
 显示数据表的详细索引信息，包括PRIMARY KEY（主键）
 SHOW INDEX FROM 数据表
 status
-------------------------------------------------------------------
数据库的操作
 创建数据库 CREATE DATABASE 数据库名;
 删除数据库 DROP DATABASE <数据库名>;

mysql服务器
启动服务 net start mysql
停止服务 net stop mysql


