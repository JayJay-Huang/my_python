import sys
from os.path import dirname, abspath

proj_path = dirname(abspath(__file__))  # 取絕對路徑 # 取上級目錄
sys.path.append(proj_path + '')  # 切換目錄

# from ... import ...
