import time
log_file_name = f"backup_daily_prod_{time.strftime('%y_%m_%d')}.html"
print(log_file_name)

# HEALTH_CHECKUP_24_06_21_07


log_file_name = f"HEALTH_CHECKUP_{time.strftime('%y_%m_%d')}.html"
print(log_file_name)

import time

# Get current date in YYYY-MM-DD format
current_date = time.strftime('%Y_%m_%d')

# Construct the file name using string formatting
log_file_name = "HEALTH_CHECKUP_" + current_date + ".html"

# Print the constructed file name
print(log_file_name)
