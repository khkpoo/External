# MySQL
>  Ref Link : [W3Resource](https://w3resource.com/mysql/mysql-show.php)

**INDEX**
- ~~Architecture~~
- ~~Replication~~
  - Replication Manage
  - Replication Parameter
- ~~Parameters~~
- ~~Administrator~~
  ~~- Backup~~
  - Privileges
- SHOW / SET Command
- ~~Command Line Interface~~
- ~~Variables~~
- ~~Function~~
- ~~Data Type~~
- ~~Tuning : Explain~~
- ~~Tuning : Hint~~

## Architecture
> Write More.
### Storage Engine
### Database Engine

## Replication
> Write More.
### Replication Manage
1. **Binary Log Manage**

    - Binary Log List 확인    
    ``show binary logs``    

      | Log_name | File_size     | Encrypted|
      | :------------- | :------------- | :------------- |
      |LAPTOP-1-bin.000001	|178 |	No |
      |LAPTOP-1-bin.000002	|2092538 |	No |


    - Binary Log Purge (날짜기준)
    ``purge binary logs before '2019-08-05'``

    - Binary Log Purge (파일기준)
    ``purge binary logs to  'LAPTOP-4LJT842D-bin.000004'``

    - Binary Log Event 상세 확인
    ``show binlog events [in 'LAPTOP-4LJT842D-bin.000005']``  

      | Log_name | Pos | Event_type | Server_id | End_log_pos | Info |
      | :------------- | :------------- | :------------- | :------------- | :------------- | :------------- |
      |LAPTOP-1-bin.000005 | 	4 | 	Format_desc | 	1 | 	124| Server ver: 8.0.17, Binlog ver: 4 |


2. **Relay Log Manage**
    - Relay Log Event 상세 확인
``show relaylog events [in 'LAPTOP-4LJT842D-bin.000005']``

### Replication Parameter

## Parameters
> Write More.

## Administrator
> Write More.
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



1. **Administrator**
    - SHOW DATABASE _[LIKE 'pattern' | WHERE expr]_
    - SHOW TABLES _[{FROM | IN} db_name] [LIKE 'pattern' | WHERE  expr]_
    - SHOW PROCESSLIST
    - SHOW PLUGINS
    - SHOW ENGINE _[engine_name]_ STATUS
    - SHOW ENGINES
    - SHOW ERRORS
    - SHOW WARNINGS
    - SHOW EVENTS
    - SHOW OPEN TABLES

2. **Stat/Variables**
    - SHOW _[GLOBAL | SESSION]_ STATUS _[LIKE 'pattern' | WHERE expr]_
    - SHOW _[GLOBAL | SESSION]_ VARIABLES _[LIKE 'pattern' | WHERE expr]_

3. **Privileges**
    - SHOW GRANTS _[FOR user]_
    - SHOW PRIVILEGES

4. **Character Set**
    - SHOW CHARACTER SET _[LIKE 'pattern' | WHERE expr]_
    - SHOW COLLATION _[LIKE 'pattern' | WHERE expr]_

5. **Description (Table/Index)**
    - SHOW COLUMNS _{FROM | IN} tbl_name [{FROM | IN} db_name] [LIKE    'pattern' | WHERE expr]_
    - SHOW INDEX[S] _{FROM | IN} tbl_name [{FROM | IN} db_name] [WHERE    expr]_
    - SHOW TABLE STATUS _[{FROM | IN} db_name] [LIKE 'pattern' | WHERE expr]_

6. **DDL Metadata**
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

7. **Binary / Relay Log**
    - SHOW BINARY LOGS
    - SHOW BINLOG EVENTS _[IN 'log_name'] [FROM pos] [LIMIT [offset,]     row_count]_
    - SHOW RELAYLOG EVENTS _[IN 'log_name'] [FROM pos] [LIMIT [offset,] row_count]_

8. **Replication**
    - SHOW SLAVE HOSTS
    - SHOW SLAVE STATUS
    - SHOW MASTER STATUS

## Command Line Interface
> Dump, Admin 등 Binary수행커맨드 추가필요

1. **구동 및 접속**
```
Windows     : mysqld_safe --user=mysql &
Non-Windows : mysql.exe --defaults-file="...\my.ini" service_name

mysql -h 1.1.1.1 -P3306 -uUSER -pPASS DATABASENAME
```
2. **중지**
```
mysqladmin -uUSER -pPASS shutdown
```
3. **Script 수행**
```
mysql -uUSER -pPASS < script.sql
mysql> sourche script.sql
```
4. **Session Kill**
```
Process Kill
kill PROCESS_ID
```
