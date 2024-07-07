set feedback off
set verify off
col spoolname new_value spoolname_var
SELECT 'G:\HEALTH_PROD_CHECKUP\HEALTH_CHECKUP_'||to_char(sysdate, 'yy_mm_dd_hh12') || '.html' spoolname
FROM dual;
SET MARKUP HTML ON SPOOL ON -
HEAD "<TITLE>DATABASE STATUS</TITLE> -
<style> h1 {text-align: center;} </style> -
<br> <H1> Daily Health Checkup Report from 3i </h1><br><br> -
<STYLE type='text/css'> -
BODY {background: #9BC869; font-family: 'Poppins','Helvetica', sans-serif;}  -
TABLE {border-collapse: collapse; Border:None; TEXT-ALIGN: center; padding : 5px;} -
TH {background-color: #FDEE86; color: #3D3D3E;} -
TD {BACKGROUND-COLOR: #FFFFFF; color: #3D3D3E;} -
.center {text-align: center;} -
</STYLE>" -
BODY "TEXT='#FFFFFF'" -
TABLE "WIDTH='90%' BORDER='5'"

spool &&spoolname_var


PROMPT	NAME AND DETAILS



select DBID, NAME, CREATED ,LOG_MODE ,OPEN_MODE from v$DATABASE;

PROMPT RMAN Details 

SELECT SESSION_KEY,INPUT_TYPE,STATUS,to_char(START_TIME,'mm/dd/yy hh24:mi') start_time,to_char(END_TIME,'mm/dd/yy hh24:mi') end_time,elapsed_seconds/3600 hrs from v$RMAN_BACKUP_JOB_DETAILS order by session_key;

PROMPT 		TABLE SPACE

set linesize 500
col NAME for a50
select name, ROUND(SPACE_LIMIT/1024/1024/1024,2) "Allocated Space(GB)", 
round(SPACE_USED/1024/1024/1024,2) "Used Space(GB)",
round(SPACE_RECLAIMABLE/1024/1024/1024,2) "SPACE_RECLAIMABLE (GB)" ,
(select round(ESTIMATED_FLASHBACK_SIZE/1024/1024/1024,2) 
from V$FLASHBACK_DATABASE_LOG) "Estimated Space (GB)"
from V$RECOVERY_FILE_DEST;



PROMPT 		LOG_SEQUENCE_IN_PROD

select process,status,sequence# from v$managed_standby;

PROMPT  	DIFFERNECE DC to DR

SELECT ARCH.THREAD# "Thread", ARCH.SEQUENCE# "Last Sequence Received", APPL.SEQUENCE# "Last Sequence Applied", (ARCH.SEQUENCE#-APPL.SEQUENCE#) "Difference" FROM (SELECT THREAD# ,SEQUENCE# FROM GV$ARCHIVED_LOG WHERE (THREAD#,FIRST_TIME ) IN (SELECT THREAD#,MAX(FIRST_TIME) FROM GV$ARCHIVED_LOG GROUP BY THREAD#)) ARCH,(SELECT THREAD# ,SEQUENCE# FROM GV$LOG_HISTORY WHERE (THREAD#,FIRST_TIME) IN (SELECT THREAD#,MAX(FIRST_TIME) FROM GV$LOG_HISTORY GROUP BY THREAD#)) APPL WHERE ARCH.THREAD#=APPL.THREAD# ORDER BY 1;

PROMPT 		INVALIDS COUNT AT CDB

select count(*) from dba_objects where status='INVALID';

PROMPT 		INVALIDS COUNT AT PDB

alter session set container=PDB_NAME;

select count(*) from dba_objects where status='INVALID';

PROMPT 		CONCURRENT MANAGER STATUS

select decode(CONCURRENT_QUEUE_NAME,'FNDICM','Internal Manager','FNDCRM','Conflict Resolution Manager','AMSDMIN','Marketing Data Mining Manager','C_AQCT_SVC','C AQCART Service','FFTM','FastFormula Transaction Manager','FNDCPOPP','Output Post Processor','FNDSCH','Scheduler/Prereleaser Manager','FNDSM_AQHERP','Service Manager: AQHERP','FTE_TXN_MANAGER','Transportation Manager','IEU_SH_CS','Session History Cleanup','IEU_WL_CS','UWQ Worklist Items Release for Crashed session','INVMGR','Inventory Manager','INVTMRPM','INV Remote Procedure Manager','OAMCOLMGR','OAM Metrics Collection Manager','PASMGR','PA Streamline Manager','PODAMGR','PO Document Approval Manager','RCVOLTM','Receiving Transaction Manager','STANDARD','Standard Manager','WFALSNRSVC','Workflow Agent Listener Service','WFMLRSVC','Workflow Mailer Service','WFWSSVC','Workflow Document Web Services Service','WMSTAMGR','WMS Task Archiving Manager','XDP_APPL_SVC','SFM Application Monitoring Service','XDP_CTRL_SVC','SFM Controller Service','XDP_Q_EVENT_SVC','SFM Event Manager Queue Service','XDP_Q_FA_SVC','SFM Fulfillment Actions Queue Service','XDP_Q_FE_READY_SVC','SFM Fulfillment Element Ready Queue Service','XDP_Q_IN_MSG_SVC','SFM Inbound Messages Queue Service','XDP_Q_ORDER_SVC','SFM Order Queue Service','XDP_Q_TIMER_SVC','SFM Timer Queue Service','XDP_Q_WI_SVC','SFM Work Item Queue Service','XDP_SMIT_SVC','SFM SM Interface Test Service') as "Concurrent Manager's Name", max_processes as "TARGET Processes", running_processes as "ACTUAL Processes" from apps.fnd_concurrent_queues where CONCURRENT_QUEUE_NAME in ('FNDICM','FNDCRM','AMSDMIN','C_AQCT_SVC','FFTM','FNDCPOPP','FNDSCH','FNDSM_AQHERP','FTE_TXN_MANAGER','IEU_SH_CS','IEU_WL_CS','INVMGR','INVTMRPM','OAMCOLMGR','PASMGR','PODAMGR','RCVOLTM','STANDARD','WFALSNRSVC','WFMLRSVC','WFWSSVC','WMSTAMGR','XDP_APPL_SVC','XDP_CTRL_SVC','XDP_Q_EVENT_SVC','XDP_Q_FA_SVC','XDP_Q_FE_READY_SVC','XDP_Q_IN_MSG_SVC','XDP_Q_ORDER_SVC','XDP_Q_TIMER_SVC','XDP_Q_WI_SVC','XDP_SMIT_SVC');


spool OFF;
SET MARKUP HTML OFF;
EXIT;
	