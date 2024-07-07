# Set the directory for the backup and log files
backup_dir="/cygdrive/e/tar_test/"
log_file="${backup_dir}/backup_log.txt"

# Get the current date
current_date=$(date +%Y_%m_%d)

# Create a directory with the current date
mkdir -p "${backup_dir}test_${current_date}" >> "$log_file" 2>&1

# Change directory to the Oracle product directory
cd /cygdrive/d/oracle/product/19c >> "$log_file" 2>&1

# Create a tar archive of the 'testing' directory and gzip it
tar -cvf - testing | gzip -c > "${backup_dir}test_${current_date}/testing.tar.gz" >> "$log_file" 2>&1
