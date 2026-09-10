from pathlib import Path
import shutil
import argparse

CATEGORY_MAP = {
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".svg"},
    "Documents": {".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt", ".md"},
    "Spreadsheets": {".xls", ".xlsx", ".csv", ".ods"},
    "Presentations": {".ppt", ".pptx", ".odp"},
    "Videos": {".mp4", ".mkv", ".avi", ".mov", ".wmv", ".webm"},
    "Audio": {".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a"},
    "Archives": {".zip", ".rar", ".7z", ".tar", ".gz"},
    "Code": {".py", ".js", ".java", ".c", ".cpp", ".html", ".css", ".sql"},
}


def get_category(file_path):
    """Return the folder category based on the file extension."""
    extension = file_path.suffix.lower()

    for category, extensions in CATEGORY_MAP.items():
        if extension in extensions:
            return category

    return "Others"


def get_unique_destination(destination):
    """Prevent overwriting files with the same name."""
    if not destination.exists():
        return destination

    counter = 1
    while True:
        new_name = (
            f"{destination.stem}_{counter}{destination.suffix}"
        )
        new_destination = destination.with_name(new_name)

        if not new_destination.exists():
            return new_destination

        counter += 1


def organize_folder(folder, dry_run=False):
    """Organize files in the selected folder."""
    folder = Path(folder).expanduser().resolve()

    if not folder.exists() or not folder.is_dir():
        raise ValueError(f"Folder does not exist: {folder}")

    processed = 0

    for item in sorted(folder.iterdir()):
        if not item.is_file():
            continue

        category = get_category(item)
        category_folder = folder / category
        destination = get_unique_destination(category_folder / item.name)

        if dry_run:
            print(f"[DRY RUN] {item.name} -> {category}/{destination.name}")
        else:
            category_folder.mkdir(exist_ok=True)
            shutil.move(str(item), str(destination))
            print(f"Moved: {item.name} -> {category}/{destination.name}")

        processed += 1

    return processed


def main():
    parser = argparse.ArgumentParser(
        description="Organize files into folders by file type."
    )
    parser.add_argument(
        "folder",
        nargs="?",
        default=".",
        help="Folder to organize. Default: current folder",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without moving files",
    )

    args = parser.parse_args()

    try:
        count = organize_folder(args.folder, args.dry_run)
        print(f"\nProcessed {count} file(s).")
    except ValueError as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
