import re


def find_name(log_line):
    pattern = r'(?<=/)[A-Za-z0-9_-]+\.(JPG|jpg)'
    ftp_pattern = r'@[a-z-\.]+(?=/)'
    if re.search(pattern, log_line) is not None:
        return re.search(pattern, log_line).group(), re.search(ftp_pattern, log_line).group()


def image_name(path_to_file):  # return list of lines
    with open(path_to_file, 'r') as log_file:
        log_lines = log_file.readlines()
    return log_lines


def main(path_to_file):
    log_lines = image_name(path_to_file)
    for log_line in log_lines:
        if find_name(log_line) is not None:
            print(find_name(log_line))


if __name__ == '__main__':
    path_to_log_file = "/Volumes/big4photo/Documents/photo_upload_logs/PXP/upload-220727-2238-FTP.log"
    main(path_to_log_file)

    assert image_name(path_to_log_file) is not None
