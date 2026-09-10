# Automated File Organizer

## Internship Details

- **Intern Name:** ERRAGADDAM ABHINAY REDDY
- **Intern ID:** CITS8534
- **Intern Role:** Python Programming
- **Duration:** 4 Weeks

## Project Description

The Automated File Organizer is a Python program that sorts files into separate folders based on their file extensions.

For example:

- Images are moved to the `Images` folder.
- Documents are moved to the `Documents` folder.
- Videos are moved to the `Videos` folder.
- Audio files are moved to the `Audio` folder.
- Unknown file types are moved to the `Others` folder.

## Features

- Automatically creates category folders.
- Supports images, documents, videos, audio, archives, code, and more.
- Prevents overwriting files with duplicate names.
- Includes a dry-run option to preview changes.
- Uses only Python standard-library modules.

## Requirements

- Python 3.8 or later
- No external packages are required.

## How to Run

Open a terminal in the project folder and run:

```bash
python file_organizer.py
```

This organizes files in the current folder.

To organize another folder:

```bash
python file_organizer.py "C:\Users\YourName\Downloads"
```

On macOS or Linux:

```bash
python file_organizer.py "/home/yourname/Downloads"
```

## Preview Before Moving Files

Use the `--dry-run` option:

```bash
python file_organizer.py "C:\Users\YourName\Downloads" --dry-run
```

This displays the planned changes without moving any files.

## Example

Before running:

```text
Downloads/
├── photo.jpg
├── report.pdf
├── song.mp3
└── video.mp4
```

After running:

```text
Downloads/
├── Images/
│   └── photo.jpg
├── Documents/
│   └── report.pdf
├── Audio/
│   └── song.mp3
└── Videos/
    └── video.mp4
```

## Technologies Used

- Python
- pathlib
- shutil
- argparse

## Conclusion

This project demonstrates file handling, directory management, extension-based classification, command-line arguments, and safe file movement using Python.
