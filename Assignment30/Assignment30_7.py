import os
import shutil
import time
from datetime import datetime
import schedule


def perform_backup(source_file, dest_dir):
    # Fixed: Saved the log file directly inside the destination folder
    log_file = os.path.join(dest_dir, "backup log.txt")
    
    try:
        # Double-check validation (Good fallback practice)
        if not os.path.exists(source_file):
            print(f"Error: Source file '{source_file}' does not exist.")
            return

        # Ensure destination directory exists, create it if it doesn't
        os.makedirs(dest_dir, exist_ok=True)

        # Get current date and time
        now = datetime.now()

        # Parse filename and extension from the source file
        file_name, file_ext = os.path.splitext(os.path.basename(source_file))

        # Format backup filename: e.g., "Data 25 07 2026 16 30_00.txt"
        timestamp_filename = now.strftime("%d %m %Y %H %M_%S")
        backup_filename = f"{file_name} {timestamp_filename}{file_ext}"
        destination_file_path = os.path.join(dest_dir, backup_filename)

        # Perform the file copy using shutil
        shutil.copy(source_file, destination_file_path)

        # Format log timestamps: e.g., 25-07-2026 and 04:30:00 PM
        log_date = now.strftime("%d-%m-%Y")
        log_time = now.strftime("%I:%M:%S %p")

        # Construct exact log entry
        log_entry = (
            f"Backup completed successfully at {log_date}\n{log_time}\n\n"
        )

        # Write/Append backup operation details into the log file
        with open(log_file, "a") as log:
            log.write(log_entry)

        print(f"Success: Backup created at {destination_file_path}")

    except Exception as e:
        # Log failure safely
        error_entry = f"Backup failed at {datetime.now().strftime('%d-%m-%Y %I:%M:%S %p')}. Error: {e}\n\n"
        try:
            with open(log_file, "a") as log:
                log.write(error_entry)
        except Exception:
            pass  # Fallback if writing log itself fails due to permissions
        print(f"Error occurred during backup: {e}")


def main():
    # 1. Accept the source file path
    source_file = input("Enter the source file path: ").strip()

    # FIX 1: Validate path immediately BEFORE entering the 1-hour loop
    if not os.path.exists(source_file):
        print(f"Error: The source path '{source_file}' is invalid or does not exist.")
        print("Program shutting down. Please run again and provide a valid path.")
        return

    # FIX 2: Ensure it is a file, not a directory (since you are using shutil.copy)
    if os.path.isdir(source_file):
        print(f"Error: '{source_file}' is a folder, but this script is configured to backup a single file.")
        print("Use a file path instead.")
        return

    # 3. Accept the destination directory path
    dest_dir = input("Enter the destination directory path: ").strip()

    print(f"\nBackup service initiated for: {source_file}")
    print("Press Ctrl+C to stop the program.\n")

    schedule.every().hour.do(perform_backup, source_file=source_file, dest_dir=dest_dir)
    perform_backup(source_file, dest_dir)

    try:

        # Infinite loop to perform a file backup every hour
        while True:
            schedule.run_pending()  # 
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\nBackup scheduler stopped cleanly by user.")


if __name__ == "__main__":
    main()
