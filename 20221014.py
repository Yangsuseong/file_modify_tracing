import os
import time

# Set Variable
# 모니터링할 최상위 디렉토리 경로
rootdir = '/root/file_test/'
# 모니터링할 시간 간격 (Sec)
interval = 2
#####################################################
# DEF

# 모든 하위 디렉토리 검색하여 리스트로 생성하는 함수
def listdirs(rootdir):
    for file in os.listdir(rootdir):
        d = os.path.join(rootdir, file)
        if os.path.isdir(d):
            #print(d)
            listdirs(d)
            dir_list.append(d)

# 디렉토리별 크기 리스트 생성 함수
def getsizedir(dir):
    for i in dir:
        tmp = int(os.path.getmtime(i))
        dir_size.append(tmp)
#####################################################
# RUN

# 하위 디렉토리 리트 생성
global dir_list
dir_list = []
dir_list.append(rootdir)
listdirs(rootdir)

# 디렉토리별 크기 리스트 생성
global dir_size
dir_size = []

getsizedir(dir_list)
    

# 설정된 시간마다 모니터링
while(True):
    for i in range(len(dir_list)):
        if dir_size[i] != int(os.path.getmtime(dir_list[i])):
            print("Warning: Modify Detected in '" + dir_list[i] + "' directory")
            dir_size[i] = int(os.path.getmtime(dir_list[i]))
    time.sleep(interval)
