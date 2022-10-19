import re

from find_log_files import find_logs
from xlsx_report_file import create_report_file, find_row_with_image_name, find_last_row, write_to_file


def find_name(log_line):
    pattern = r'(?<=/)[A-Za-z0-9_-]+\.(JPG|jpg)'
    ftp_pattern = r'@[a-z-\.]+(?=/)'
    if re.search(pattern, log_line) is not None:
        return re.search(pattern, log_line).group(), re.search(ftp_pattern, log_line).group()


def image_name(path_to_file):  # return list of lines from log file
    with open(path_to_file, 'r') as log_file:
        log_lines = log_file.readlines()
    return log_lines


def get_column_name(ftp_name):  # return colum's letter for ftp address
    ftp_dict = {"@ftp.kommersant.ru": "B",
                "@ftp.itar-tass.com": "D",
                "@stringer.photoxpress.ru": "C"}
    return ftp_dict[ftp_name]





def main(path_to_log_file):
    path_to_report_file = create_report_file()  # create report file, scip if exist
    log_lines = image_name(path_to_log_file)
    for log_line in log_lines:
        if find_name(log_line) is not None:
            image_file_name, ftp_name = find_name(log_line)
            print(find_name(log_line))  # get file name and ftp address
            row_number = find_row_with_image_name(image_file_name, path_to_report_file)  # get row to write
            column_name = get_column_name(ftp_name)
            if row_number is None:  # if no image_file_name in "A" column write data to new column
                row_number = find_last_row(path_to_report_file) + 1
            write_to_file(path_to_report_file, image_file_name, column_name, row_number)





if __name__ == '__main__':
    pattern = '*.log'
    # path_all_log_files = '/Volumes/big4photo/Documents/photo_upload_logs'
    # path_all_log_files = '/Volumes/big4photo/Documents/photo_upload_logs/TASS'
    # path_all_log_files = '/Volumes/big4photo/Documents/photo_upload_logs/Kommersant'
    path_all_log_files = '/Volumes/big4photo/Documents/photo_upload_logs/PXP'

    all_log_files = find_logs(pattern, path_all_log_files)
    for path_to_log_file in all_log_files:
        # path_to_log_file = "/Volumes/big4photo/Documents/photo_upload_logs/PXP/upload-220915-1524-FTP.log"
        main(path_to_log_file)


    assert image_name(path_to_log_file) is not None
