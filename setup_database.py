import subprocess

def run_script(script_name):
    """
    Runs a Python script and prints the result.
    """
    print(f"Running {script_name}...")
    result = subprocess.run(["python", script_name], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"{script_name} completed successfully.\n")
    else:
        print(f"Error running {script_name}:\n{result.stderr}\n")

if __name__ == "__main__":
    # List of scripts to run in order
    scripts = [
        "init_db.py",              # Initializes the clients table
        "init_law_firms.py",         # Initializes the law_firms table with default data
        "add_firm_name_column.py", # Adds the firm_name column to the law_firms table
        "add_lawfirm_column.py",   # Adds the law_firm column to the clients table
    ]

    print("Starting database setup...\n")
    for script in scripts:
        run_script(script)

    print("Database setup complete!")