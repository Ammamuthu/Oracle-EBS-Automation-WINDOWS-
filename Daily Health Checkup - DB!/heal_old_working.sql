set feedback off
set verify off
col spoolname new_value spoolname_var
SELECT 'HEALTH-Check'||to_char(sysdate,'DD-MON-YYYY_HH24') || '.html' spoolname
FROM dual;

SET MARKUP HTML ON SPOOL ON -
HEAD "<TITLE>DATABASE STATUS</TITLE> -
<style> h1 {text-align: center;} </style> -
<br> <H1> Daily Health Checkup Report from 3i </h1><br><br> -
<STYLE type='text/css'> -
<!-- BODY {background: #595959; font-family: 'Poppins', sans-serif;} --> -
TH {background-color: #000000; color: #FEffff;} -
.center {text-align: center;} -
</STYLE>" -
BODY "TEXT='#FEffff'" -
TABLE "WIDTH='90%' BORDER='3'"

spool &&spoolname_var


PROMPT      NAME AND DETAILS



select DBID, NAME, CREATED ,LOG_MODE ,OPEN_MODE from v$DATABASE;

PROMPT 		TABLE SPACE

select name, ROUND(SPACE_LIMIT/1024/1024/1024,2) "Allocated Space(GB)", 
round(SPACE_USED/1024/1024/1024,2) "Used Space(GB)",
round(SPACE_RECLAIMABLE/1024/1024/1024,2) "SPACE_RECLAIMABLE (GB)" ,
(select round(ESTIMATED_FLASHBACK_SIZE/1024/1024/1024,2) 
from V$FLASHBACK_DATABASE_LOG) "Estimated Space (GB)"
from V$RECOVERY_FILE_DEST;


PROMPT 		LOG_SEQUENCE_IN_PROD

select process,status,sequence# from v$managed_standby;

PROMPT 	INVALIDS COUNT

select count(*) from dba_objects where status='INVALID';

spool OFF;
SET MARKUP HTML OFF;