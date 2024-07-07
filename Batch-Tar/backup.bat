@echo off

REM Launch Cygwin and execute backup commands
C:\cygwin\cygwin.bin --login -i << EOF
cd /cygdrive/d/oracle/product/19c
tar -cvf - testing | gzip -c > /cygdrive/e/tar_test/testing.tar.gz
EOF
