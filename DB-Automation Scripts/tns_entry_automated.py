import subprocess

def check_database_status(username, password, hostname, port, service_name):
    # Construct the TNS entry
    tns_entry = f'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST={hostname})(PORT={port}))(CONNECT_DATA=(SERVICE_NAME={service_name})))'

    # Use tnsping to check the status
    command = f'tnsping {tns_entry}'

    try:
        subprocess.run(command, check=True, shell=True)
        print(f"The database on {hostname}:{port}/{service_name} is UP.")
    except subprocess.CalledProcessError as e:
        print(f"The database on {hostname}:{port}/{service_name} is DOWN. Error: {e}")

# Example usage
check_database_status("system", "ADMIN", "localhost", "1521", "xe")
