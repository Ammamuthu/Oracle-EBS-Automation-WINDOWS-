cd /cygdrive/e/tar_test/
current_date=$(date +%Y_%m_%d)

mkdir "test_${current_date}"
cd /cygdrive/d/oracle/product/19c
tar -cvf - testing | gzip -c > /cygdrive/e/tar_test/"test_${current_date}"/testing.tar.gz

# SET PATH=%PATH%;C:\Users\Ashok\AppData\Local\Programs\Python\Python312;

# REM running Python scripts
# python mailer.py