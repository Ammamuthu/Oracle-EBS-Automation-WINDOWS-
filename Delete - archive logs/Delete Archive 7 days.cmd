@echo on

REM (MOVING TOB DRIVE)
E:

REM SOURCEING THE DATABASE
CALL E:\oracle\PROD\11.2.0\PROD_erplive.cmd

REM LAUNCHING THE RMAN UTILITY
rman target /


delete archivelog until time 'SYSDATE-7';

YES

EXIT