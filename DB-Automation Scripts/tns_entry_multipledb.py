import subprocess

def check_database_status(hostname, port, service_name):
    # Construct the TNS entry
    tns_entry = f'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST={hostname})(PORT={port}))(CONNECT_DATA=(SERVICE_NAME={service_name})))'

    # Use tnsping to check the status
    command = f'tnsping {tns_entry}'

    try:
        subprocess.run(command, check=True, shell=True)
        print(f"The database on {hostname}:{port}/{service_name} is UP.")
    except subprocess.CalledProcessError as e:
        print(f"The database on {hostname}:{port}/{service_name} is DOWN. Error: {e}")

database = [{"hostname":"localhost","port":"1521","service_name":"xe"},
{"hostname":"Ip_address","port":"1521","service_name":"demo"}]
# Example usage

for db in database:
    check_database_status(db["hostname"],db["port"],db["service_name"])
