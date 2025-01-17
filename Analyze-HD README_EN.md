
# Analyze-HD

Analyze-HD is a Python script designed to analyze a computer drive and generate a report listing files larger than 1 GB. This can be useful for identifying files that occupy significant disk space.

## Features

- Excludes system folders such as `Windows`, `Program Files`, `$Recycle.Bin` to avoid analyzing irrelevant files.
- Recursively searches for large files in all directories of the specified drive.
- Generates a report (`LargeFilesReport.txt`) listing files larger than 1 GB, including their full path and size.

## System Requirements

- Python 3.6 or higher
- Read permissions on the specified drive

## Dependencies

This script only uses Python standard libraries, so no additional dependencies are required.

## How to Use

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Tranchillo/Analyze-HD.git
   cd Analyze-HD
   ```

2. **Run the script**:
   - Edit the `drive_to_analyze` variable in the `analyze_hd.py` file to specify the drive to analyze (e.g., `C:\`).
   - Execute the script:
     ```bash
     python analyze_hd.py
     ```

3. **Output**:
   - The generated report will be found in the root directory of the analyzed drive as `LargeFilesReport.txt`.

## Notes

- The script ignores file access errors (e.g., insufficient permissions).
- File size is checked against a predefined threshold of 1 GB. This value can be modified by editing the `size_limit` variable in the script.

## Contribute

If you want to contribute to the project, follow these steps:
1. Fork the repository.
2. Create a new branch for your changes.
3. Submit a pull request.

## License

This project is distributed under the MIT license. For more details, see the LICENSE file.

---

### Contact

For questions or suggestions, you can open an issue on [GitHub](https://github.com/Tranchillo/Analyze-HD/issues).
