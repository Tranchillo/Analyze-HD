import os

def analyze_drive(drive, output_file, size_limit=1 * 1024 * 1024 * 1024):
    # Cartelle da escludere
    excluded_dirs = [
        os.path.join(drive, "Windows"),
        os.path.join(drive, "Program Files"),
        os.path.join(drive, "Program Files (x86)"),
        os.path.join(drive, "ProgramData"),
        os.path.join(drive, "Users\\All Users"),
        os.path.join(drive, "$Recycle.Bin"),
    ]
    
    with open(output_file, "w", encoding="utf-8") as report:
        report.write(f"Report dei file più grandi di 1GB nel drive {drive}:\n")
        report.write("=" * 80 + "\n")

        for root, dirs, files in os.walk(drive):
            # Escludi directory specificate
            if any(root.startswith(excluded_dir) for excluded_dir in excluded_dirs):
                continue
            
            for file in files:
                try:
                    file_path = os.path.join(root, file)
                    # Controlla la dimensione del file
                    if os.path.isfile(file_path):
                        file_size = os.path.getsize(file_path)
                        if file_size > size_limit:
                            report.write(f"{file_path} - {file_size / (1024 * 1024 * 1024):.2f} GB\n")
                except (OSError, PermissionError):
                    # Ignora errori di accesso ai file
                    continue

    print(f"Analisi completata. Report salvato in: {output_file}")

# Configura il percorso di analisi
drive_to_analyze = "C:\\"
output_report_file = os.path.join(drive_to_analyze, "LargeFilesReport.txt")

# Esegui lo script
analyze_drive(drive_to_analyze, output_report_file)
