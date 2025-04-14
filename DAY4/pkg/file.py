import os
import datetime

class File:
    def __init__(self, directory):
        self.directory = directory
        self.files = self._get_all_files()

    def _get_all_files(self):
        files_list = []
        for root, _, files in os.walk(self.directory):
            for file in files:
                file_path = os.path.join(root, file)
                file_info = self._get_file_info(file_path)
                files_list.append(file_info)
        return files_list

    def _get_file_info(self, file_path):
        file_size = os.path.getsize(file_path)
        modified_date = datetime.datetime.fromtimestamp(os.path.getmtime(file_path)).date()
        return {'path': file_path, 'size': file_size, 'modified_date': modified_date}

    def getMaxSizeFile(self, n):
        sorted_files = sorted(self.files, key=lambda file: file['size'], reverse=True)
        return sorted_files[:n]

    def getLatestFiles(self, date):
        return [file for file in self.files if file['modified_date'] > date]
