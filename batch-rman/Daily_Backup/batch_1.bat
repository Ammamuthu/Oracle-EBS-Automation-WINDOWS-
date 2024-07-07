@echo on

REM Change to another directory (D drive in this example)
D:

REM Source the file (assuming it's a cmd script)
call "D:\oracle\product\19c\db_1\STG12_ERPTEST.cmd


REM Change to the directory containing the RMAN script
cd D:\Automation-scripts\Batch-scripts

REM Run the RMAN script
rman target / @rman_daily.cmd log=backup_daily_prod_%date:~4,2%_%date:~7,2%_%date:~10%.log trace=J:\ERP_Backup_2015\backup_daily_prod_%date:~4,2%_%date:~7,2%_%date:~10%.trc

REM running Python scripts
python mailer.py