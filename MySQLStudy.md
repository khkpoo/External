# modify 0954
# Test
# MySQL
>  Ref Link : [W3Resource](https://w3resource.com/mysql/mysql-show.php)

**INDEX**
- ~~Architecture~~
- ~~Replication~~
  - Binary/Relay-log Manage
  - Replication Command
  - Thread Manage  
- ~~Parameters~~
- ~~Administrator~~
  ~~- Backup~~
  - Privileges
- SHOW / SET Command
- ~~Command Line Interface~ ~
- ~~Variables~~
- ~~Function~~
- ~~Data Type~~
- ~~Tuning : Explain~~d
- ~~Tuning : Hint~~


## Architecture
> Write More.
### Storage Engine
### Database Engine

## Replication
> Write More.
### Binary/Relay-log Manage
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
      |LAPTOP-1-bin.000005 | 	124 | 	Previous_gtids | 	1 | 	     155|  	|

2. **Relay Log Manage**
    - Relay Log Event 상세 확인  
``show relaylog events [in 'LAPTOP-4LJT842D-bin.000005']``

### Replication Command
CHANGE MASTER TO MASTER_LOG_FILE='binary_log.xxxxx',
MASTER_LOG_POS=XXXX,
MASTER_HOST='MASTER_IP',
MASTER_PORT=3306,
MASTER_USER='REPLI_USER',
MASTER_PASSWORD='REPLI_PASS'

### Thread Manage
 START SLAVE

## Parameters
> 정리안된 Parameter들 다수.

- **Base Settings**
```
user                        = mysql                   # MySQL 구동 할 OS 계쩡 정보
port                        = 3306
basedir                     = /mysql/mysql-5.7.15
datadir                     = /orad/mysql_data        # Innodb 외의 데이터 파일 경로
tmpdir                      = /orad/inno/tmp          # MySQL 내부적으로 사용하는 Temp 영역 (Temp Table 아니다)
socket                      = /tmp/mysql.sock
pid-file                    = /tmp/mysqld.pid
default-storage-engine      = InnoDB                  # 기본적으로 사용할 스토리지 엔진
```
- **Time Zone**
```
# Timezone Name 미설치시 default-time-zone='UTC' 형식으로 설정하면 에러발생
# '+0:00' 또는 '-0:00' 으로 설정
#
# Time Zone Name 설치법 (없을 경우 +NN:NN 형태로기술해야함)
# https://dev.mysql.com/downloads/timezones.html
# timezone_2019b_leaps_sql.zip (Non-POSIX)
# mysql -uroot -proot1234 mysql < timezone_leaps.sql
# set time_zone='+09:00'
# set time_zone='Asia/seoul'

default_time_zone            = '+9:00'                 # 설정안할경우 SYSTEM 값임.. (OS따라감)
default-time-zone            = Asia/Seoul

```

- **Character Set**
> 추가 확인 필요

```
character-set-server        = utf8mb4                 # 기본 문자 집합
collation-server            = utf8mb4_general_ci      # 대소문자 구분하려 할 경우 "룰 설정
character_set_database      = utf8                    # 8 deprecated ?
[mysqld]
character_set_server        = utf8
collation_server            = utf8_general_ci
[client]
character_set_client        = utf8                    # 8 deprecated ?
default_character_set       = utf8
```

- **onnection**
```
back_log                    = 100                     # 클라이언트가 MySQL 접속시 인증을 대기 대기 큐에 담아 둘지 결정.
max_connections             = 300
max_connect_errors          = 999999
thread_cache_size           = 50                      # 쓰레드 풀, 최대 몇 개까지 스레드를 스레드 풀에 보관할지 결정. Threads_created / Connections)값이 0.01 즉 1% 이상이면 thread_cache_size 값 증가 고려
                                                      # Connection Pool 사용시 필요없음
table_open_cache            = 400
wait_timeout                = 28800                   # 지정된 시간 동안 응답이 없는 클라이언트 강제 종료
# bind-address              = 172.17.1.0
```

- **Session Memory**
```
# 아래 네개는 세션 범위의 변수 예) 500개 세션 접속 500*512kb=256000kb(250MB). 동적 변수
sort_buffer_size            = 128K                    # 적정 수준 64KB~512KB. 2MB이상은 느려지는 현상 발생.
join_buffer_size            = 128K                    # 적절한 조인 조건이 없어 Driven 테이블이 Full Table Scan될 때 사용. 128~512KB 사이 권장
read_buffer_size            = 128K                    # 정확하진 않으나, Full Table Scan시 사용. 16kb~32MB에서 128kb일 때 가장 빠른 성능
read_rnd_buffer_size        = 128K                    # 읽어야 할 데이터 레코드를 버퍼링하는데 필요. 
                                                      # Two-Pass 정렬시 사용되는 영역. ( 정렬대상 적을시 Single-pass, 크면 Two-pass )
                                                      # 64~128kb 적정. 웹환경이 아닌 dw일 경우 늘려야 함
# Query Cache... Depricated in 8
# 쿼리 캐쉬와 관련되었으며 128MB를 넘기지 않는다.메모리가 충분치 않거나, 테이블 데이터가 빈번하게 변경되면 64MB 이상으로는 설정하지 않음.
# query_cache_size            = 32M
# query_cache_limit           = 2M
```

- **Innodb : Memory**
```
innodb_buffer_pool_size           = 1G                # innodb 중 가장 중요한 옵션.50~80 수준 설정.
#innodb_additional_mem_pool_size  = 16M               # 메타정보나 통계정보를 내부적으로 별도 가짐. 해당 정보의 공간 설정. 테이블이 1000개 미만 16MB 이상이면 32MB로 설정
innodb_change_buffering           = all               # all / inserts / deletes / cahnges (inserts+deletes) / purges / none
innodb_change_buffer_max_size     = 25                # Innodb_buffer_pool_size 대비 % 값을 갖는다
```

- **Innodb : Data File**
```
innodb_autoextend_increment = 100
innodb_file_per_table       = 1                                 # innodb 스토리지 엔진 사용하는 테이블은 *.ibd로 생성되는데 테이블 스페이스 개념으로 사용됨.
                                                                # 1이면 테이블 단위로 각각 1개씩 데이터파일과 테이블 스페이스를 생성.
                                                                # 0이면 하나의 테이블 스페이스에 모든 테이블의 데이터가 저장.
                                                                # 하나의 테이블 스페이스에서 테이블 삭제 시 빈 블록은 os로 반환하지 않음.
                                                                # 하지만 테이블별로 운영할 경우 os로 반환되어 해당 파라미터는 1로 설정.
innodb_data_home_dir        = /orad/inno/data
innodb_data_file_path       = ib_system:100M:autoextend         # 시스템 데이터 + 사용자 데이터
                                                                # 시스템 데이터 : 사용자가 생성한 테이블에 대한 메타정보, 트랜잭션을 위한 UNDO와 같이 InnoDB가 임의적으로 만들어낸것
                                                                # 시스템 테이블 스페이스는 ib_system으로 생성된다.
                                                                # 사용자 데이터는 innodb_file_per_table 옵션이 1이면 테이블별로 생성.
                                                                # innodb_file_per_table가 0으로 되면, innodb_data_file_path에서 생성된 데로 생성
                                                                # 트랜잭션이 많은 서비스에서는 ib_system이 10G까지 증가된 사례도 있음.
                                                                # 여러 개로 둘 경우 innodb_data_home_dir=비게 두고 innodb_data_file_path=/data1/ibdata1:300G;/data2/ibdata2:700G
                                                                # innodb_data_file_path           = ibdata1:128M;ibdata2:128M:autoextend:max:4096M
```

- **Innodb : Undo File**
```
innodb_undo_directory                      = /mysql/innodb/undo
innodb_max_undo_log_size                   = 1073741824               # Tuncate 수행 여부 결정 기준값 (해당 기준치를 넘을 경우 초기화 값으로 Truncate 되도록)
innodb_undo_log_truncate                   = 1                        # Tuncate 수행 여부 0(Disable)
innodb_purge_rseg_truncate_frequency       = 128                      # 자동 Truncate 수행 빈도. DML 수행 횟수. 수치가 작을수록 잦은 Undo 공간체크를 수행하므로 Truncate 수행 빈도 증가함
innodb_undo_tablespaces                    = 2                        # Undo TS 개수 (초기화시점에만적용), Deprecate in 8
```

- **Innodb : Redo Log**
```
innodb_log_group_home_dir     = /orad/inno/log            # Redo Log 위치
innodb_log_buffer_size        = 16M                       # Redo Log를 위한 버퍼메모리 크기이며 16~32MB면 충분.  
                                                          # innodb_log_file_size log file의 크기이며, innodb_log_files_in_group 그룹의 개수
                                                          # innoDB 버퍼 풀이 10G 이상이면, 개  수에 상관없이 2~4G면 적절, 이하이면  2GB이하 설정
                                                          # 데이터를 변경하는 쿼리가 빈번하면 전체 로그의 크기를 4G로 하는 것이 적정.(5.6이상에서는 4G 이상 가능)
innodb_log_file_size          = 1024M
innodb_log_files_in_group     = 2
innodb_redo_log_archive_dirs                              # New Feature in Mysql 8 ~
```
- **Innodb : Etc**
```
innodb_fast_shutdown        = 1                         # Clean Shutdown. 종료시 변경사항 Datafile에 기록. 
                                                        # 재시작 시 Redo가 필요없고 시작이 빠르나, 종료시 느림
```

- **MyISAM**
```
key_buffer_size             = 32M                       # MyISAM엔진에서 주로 인덱스에 대해서만 버퍼 역할을 한다. 일반적으로 30~50%설정.
bulk_insert_buffer_size     = 32M
myisam_sort_buffer_size     = 1M
myisam_max_sort_file_size   = 2G
myisam_repair_threads       = 1
ft_min_word_len             = 2
# myisam_recover                                        # unknown
#ft_min_word_len            = 3
```

- **Log File**
```
## General 로그를 사용하려면 아래 설정은 그대로 유지하고
## MySQL 서버에 로그인한 후 "SET GLOBALgeneral_log=1" 명령으로 활성화
general_log                 = 0
general_log_file            = /usr/local/mysql/logs/general_query.log
log-error                   = /mysql/mysql-5.7.15/alert/mysqld.log
log_slow_admin_statements                                               # ALTER TABLE... 과 같은 DDL에 대한 느린 쿼리 로그 기록 여부를 결정.
slow-query-log              = 1                                         # 어떠한 쿼리를 튜닝할 것인지를 알려주며 1이면 활성화.
long_query_time             = 1
slow_query_log_file         = /mysql/mysql-5.7.15/alert/slow_query.log
log_output                  = table                                     # Table or File
```

- **Replication**
```
server-id                   = 1
log-slave-updates                                                 # 마스터-1.슬레이브-슬레이브일 경우 1.슬레이브에서 binlog에 기록할지를 결정하는 요소
```

- **Replication : Master Node**
```
log-bin                         = /usr/local/mysql/logs/binary_log
log-bin-index                   = /usr/local/mysql/logs/binary_index
max_binlog_size                 = 512M
binlog_expire_logs_seconds      = 259200
# binlog_cache_size             = 128K                            # 버퍼에 기록했다 디스크로 기록. 버퍼용 메모리 크기. 소용량 56~256kb
binlog_cache_size               = 2M                              # Sessin별 사용량이므로 크지않게, 56 ~ 256 KB
binlog_format                   = MIXED
log_bin_trust_function_creators = 0
log-bin-trust-function-creators = 1                               # 바이너리 로그가 활성화된 상태에서 스터어드 함수가 생성되면 " 바이너리 로그로 인한 복제가 안전하지 않다"란 에러 발생.
                                                                  # 해당 파라미터는 위와 같은  경고를 무시하고 스토어드 함수  를 생성.
sync_binlog                     = 1                               # 로그의 성능부하는 innodb의 로그와 binlog의 sync시 부하가 발생.(주로 쓰기 작업)
                                                                  # 1으로 설정시 트랜잭션 커밋 될 때마다 바이너리 로그를 디  스크에 플러쉬.
                                                                  # 0으로 설정시 디스크에 기록 하나 동기화를 하지 않기 떄문  에 버퍼까지만 기록하고 처리   완료.
                                                                  # 0으로 설정시 마스터가 죽으 면, 바이너리 로그가 손실되어  데이터가 틀려질 수 있음(성능  빠름)
# Depricated
#expire_logs_days               = 14

```

- **Replication : Slave Node**
```
relay-log                   = /orad/mysql_dalta/binlog/binary_log
relay_log_purge             = TRUE                                  # 이미 적용하여 불필요한 relay log 자동 purge (1,0)
read_only                                                           # 슬레이브일 경우 읽기전용으로 만드는 옵션
```

- **Statistics**
```
# Persistent Statistics 사용시
# mysql.innodb_table_stats (Disk)에 저장
# Analyze table 로 수집하거나, 데이터변동시 자동 수집
innodb_stats_persistent                 = ON
innodb_stats_auto_recalc                = ON
innodb_stats_persistent_sample_pages    = 20

# Non-Persistent Statistics 사용시
# Memory에만 Statistics정보 저장
# Analyze table 로 수집하거나, innodb_stats_on_metadata가 켜진 경우라면 show table status 같은 command 조회시 동적 수집
innodb_stats_persistent                 = OFF
innodb_stats_on_metadata                = ON
innodb_stats_transient_sample_pages     = 8                     # innodb_stats_sample_pages 가 Deprecated 되고 innodb_stats_sample_pages 로 변경 됨 (MySQL 8.0~)
```

## Administrator
> Write More.
### Backup
### Privileges
> 작성 완료 (2019-08-09)

- ROLE 생성하여 부여할 수 있음 (5. 버전 지원안됨)
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
|File	|File access on server	|To read and write files on the server, **SELECT INTO FILE / LOAD DATA IN**|
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
test  
