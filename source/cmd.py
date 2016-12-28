#-*- coding:utf-8 -*-
##帧格式的其他域
FIXED_START_CHAR=16
FIXED_END_CHAR=22

VERIABLE_START_CHAR = 104
VERIABLE_END_CHAR = 22

CONTROL_LEN=1#控制域的长度
ADDR_LEN=4#地址的长度
#客户端制造报文的时候用
CMAKE_CONNECT=1
CMAKE_UNCONNECT=2
CMAKE_CMD_INVALID = 0
CMAKE_HARTBEAT=3
CMAKE_STARTFILE=4
CMAKE_MAKEFILEDATA=5
CMAKE_MAKEFILEERROR=6


#客户端到主站
##系统连接类
CCMD_SYSTEM_START = 0
CCMD_CONNECT_REQ = 1 #连接请求
CCMD_UNCONNECT_REQ=2 #请求断开连接
CCMD_CMD_INVALID=3
CCMD_CMD_HARTBEAT = 4#心跳包
CCMD_SYSTEM_END = 15
##文件传输类
CCMD_FILE_START = 16 #文件命令的开始序号
CCMD_FILE_REQ_START=17 #文件传输请求开始
CCMD_FILE_TRANSFERRING=18 #文件正在传输
CCMD_FILE_COMPLETE = 19 #文件传输完成，这是最后一个包
CCMD_FILE_BUSY = 20 #忙，等待一段时间再请求
CCMD_FILE_ERROR=21 #表示客户机在读取文件的时候错误
CCMD_FILE_END = 25 #文件命令的终止序号



#主站到客户端
##系统连接类
HCMD_SYSTEM_START = 0
HCMD_CONNECT_RES = 1 #响应客户端连接请求,表示可以进行下一步命令

HCMD_CMD_INVALID=3
HCMD_CMD_HARTEAT = 4#回应子站发送的心跳包
HCMD_SYSTEM_END = 15
##文件传输类
HCMD_FILE_START = 16  #文件命令的开始序号
HCMD_FILE_CONFIRM_START=17 #确认开始传输文件命令
HCMD_FILE_NEXT_TRANSFERRING=18 #文件传输正确，请下位机继续传输
HCMD_FILE_RETRYTHIS=19 #当前文件包传输错误，重传
HCMD_FILE_COMPLETE = 20 #响应文件传输终止或已经完成文件的传输
HCMD_FILE_OR_NEXT = 21 #是否有下一个文件的传输
HCMD_FILE_BUSY = 22 #忙，等待一段时间再请求
HCMD_FILE_END = 25 #文件命令的终止序号
