# MySQL
> > Ref Link : [W3Resource](https://w3resource.com/mysql/mysql-show.php)

**INDEX**
- Architecture
- Replication
- Parameters
- Administrator
  - Backup
  - Privileges
- SHOW / SET Command
- Command Line Interface
- Variables
- Function
- Data Type
- Tuning : Explain
- Tuning : Hint

## Architecture
### Storage Engine
### Database Engine

## Replication
Replication Setting
### Replication Manage
#### Master Node
#### Slave Node


## Parameters
Parameter Settings

## Administrator
administrator
### Backup
### Privileges
> 작성 완료 (2019-08-09)

- ROLE 생성하여 부여할 수 있음
- SHOW GRANTS FOR _USER_NAME_ USING _ROLE_NAME_
- 모든 권한 부여는 `ALL PRIVILEGES` 사용
```
GRANT priv_type ON dbname.tablename TO user_or_role [with grant option]
```

| Privilege     | Context     |Comment     |
| :------------- | :------------- | :------------- |
|Alter	|Tables|	To alter the table|
|Alter routine	| Functions,Procedures	|To alter or drop stored functions/procedures|
|Create	|Databases,Tables,Indexes	|To create new databases and tables|
|Create routine	|Databases|	To use CREATE FUNCTION/PROCEDURE|
|Create temporary tables|	Databases	|To use CREATE TEMPORARY TABLE|
|Create view	|Tables	|To create new views|
|Create user|	Server Admin	|To create new users|
|Delete	|Tables	|To delete existing rows|
|Drop|	Databases,Tables	|To drop databases, tables, and views|
|Event	|Server Admin	|To create, alter, drop and execute events|
|Execute	|Functions,Procedures|	To execute stored routines|
|File	|File access on server	|To read and write files on the server|
|Grant option	|Databases,Tables,Functions,Procedures	|To give to other users those privileges you possess|
|Index	|Tables	|To create or drop indexes|
|Insert	|Tables	|To insert data into tables|
|Lock tables	|Databases	|To use LOCK TABLES (together with SELECT privilege)|
|Process	|Server Admin	|To view the plain text of currently executing queries|
|Proxy	|Server Admin	|To make proxy user possible|
|References|	Databases,Tables|	To have references on tables|
|Reload	|Server Admin	|To reload or refresh tables, logs and privileges|
|Replication client|	Server Admin|	To ask where the slave or master servers are|
|Replication slave	|Server Admin|	To read binary log events from the master|
|Select	|Tables	|To retrieve rows from table|
|Show databases|	Server Admin|	To see all databases with SHOW DATABASES|
|Show view	|Tables	|To see views with SHOW CREATE VIEW|
|Shutdown	|Server Admin|	To shut down the server|
|Super	|Server Admin|	To use KILL thread, SET GLOBAL, CHANGE MASTER, etc.|
|Trigger|	Tables	|To use triggers|
|Create tablespace|	Server Admin	|To create/alter/drop tablespaces|
|Update	|Tables	|To update existing rows|
|Usage	|Server Admin	|No privileges - allow connect only|

## SHOW / SET Command
> 작성 완료 (2019-08-09)

- 패턴 검색시 대소문자 구분함.



**Admin**
- SHOW DATABASE _[LIKE 'pattern' | WHERE expr]_
- SHOW TABLES _[{FROM | IN} db_name] [LIKE 'pattern' | WHERE expr]_
- SHOW PROCESSLIST
- SHOW PLUGINS
- SHOW ENGINE _[engine_name]_ STATUS
- SHOW ENGINES
- SHOW ERRORS
- SHOW WARNINGS
- SHOW EVENTS
- SHOW OPEN TABLES

**Stat/Variables**
- SHOW _[GLOBAL | SESSION]_ STATUS _[LIKE 'pattern' | WHERE expr]_
- SHOW _[GLOBAL | SESSION]_ VARIABLES _[LIKE 'pattern' | WHERE expr]_

**Privileges**
- SHOW GRANTS _[FOR user]_H
- SHOW PRIVILEGES

**Character Set**
- SHOW CHARACTER SET _[LIKE 'pattern' | WHERE expr]_
- SHOW COLLATION _[LIKE 'pattern' | WHERE expr]_

**Description (Table/Index)**
- SHOW COLUMNS _{FROM | IN} tbl_name [{FROM | IN} db_name] [LIKE 'pattern' | WHERE expr]_
- SHOW INDEX[S] _{FROM | IN} tbl_name [{FROM | IN} db_name] [WHERE expr]_
- SHOW TABLE STATUS _[{FROM | IN} db_name] [LIKE 'pattern' | WHERE expr]_

**DDL Metadata**
- SHOW CREATE DATBASE
- SHOW CREATE FUNCTION
- SHOW CREATE PROCEDURE
- SHOW CREATE TABLE
- SHOW CREATE TRIGGER
- SHOW CREATE VIEW
- SHOW CREATE EVENT
- SHOW FUNCTION CODE
- SHOW FUNCTION STATUS
- SHOW PROCEDURE CODE
- SHOW PROCEDURE STATUS

**Binary / Relay Log**
- SHOW BINARY LOGS
- SHOW BINLOG EVENTS _[IN 'log_name'] [FROM pos] [LIMIT [offset,] row_count]_
- SHOW RELAYLOG EVENTS _[IN 'log_name'] [FROM pos] [LIMIT [offset,] row_count]_

**Replication**
- SHOW SLAVE HOSTS
- SHOW SLAVE STATUS
- SHOW MASTER STATUS

## Command Line Interface
구동
mysql -h 1.1.1.1 -P3306 -uUSER -pPASS DATABASENAME
Script 수행
mysql -uUSER -pPASS < script.sql
mysql> sourche script.sql
Process Kill
kill PROCESS_ID
