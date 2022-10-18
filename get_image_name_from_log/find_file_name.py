import re

def find_name(log_line):
    pattern = r'(?<=/)[A-Za-z0-9_-]+\.(JPG|jpg)'
    return re.search(pattern,log_line).group()



if __name__ == '__main__':
    log_line = '2022-10-17 15:36:14	[OK]	/Volumes/big4photo-2/My photo 2022/20220505PEV_8104-HDR.JPG	FTP	ftpphoto@ftp.kommersant.ru//PHOTO/INBOX/SHOOTS/Pavlenko_Evgenij_2571/KSP_017685/20220505PEV_8104-HDR.JPG	2936919	466c712da2f1f6c887a95a667e37a0b7'
    print(find_name(log_line))