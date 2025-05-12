import datetime
from pkg.file import File

fs = File(".")

largest_files = fs.getMaxSizeFile(2)
print("Top 2 largest files:")
for file in largest_files:
    print(f"File: {file['path']}, Size: {file['size']} bytes")

date = datetime.date(2018, 2, 1)
latest_files = fs.getLatestFiles(date)
print("\nFiles modified after 1st Feb 2018:")
for file in latest_files:
    print(f"File: {file['path']}, Modified Date: {file['modified_date']}")
