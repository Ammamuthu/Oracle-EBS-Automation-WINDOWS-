E:

call E:\oracle\STG40\11.2.0\STG40_erpdev.cmd

sqlplus / as sysdba @E:\oracle\STG40\HEALTH\heal.sql

REM SENDING MAIL of the html script
PYTHON Mail_send_Health