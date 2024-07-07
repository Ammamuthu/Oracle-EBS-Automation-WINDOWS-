run{
allocate channel c1 type disk;

allocate channel c2 type disk;

allocate channel c3 type disk;

allocate channel c4 type disk;

allocate channel c5 type disk;

allocate channel c6 type disk;

BACKUP as compressed backupset FULL FILESPERSET 10 FORMAT ' E:\rman_bkp\STG12_D_%s_%p_%d_%t.bak' DATABASE;

BACKUP as compressed backupset filesperset 10 FORMAT 'E:\rman_bkp\STG12_A_%s_%p_%d_%t.bak' ARCHIVELOG ALL;

BACKUP FORMAT 'E:\rman_bkp\STG12_C_%s_%p_%d_%t.bak' CURRENT CONTROLFILE;

RELEASE CHANNEL c1;

RELEASE CHANNEL c2;

RELEASE CHANNEL c3;

RELEASE CHANNEL c4;

RELEASE CHANNEL c5;

RELEASE CHANNEL c6;
}
exit