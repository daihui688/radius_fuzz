Code_Access_Request = 1  # 接入请求报文
Code_Access_Accept = 2  # 接入成功回应报文
Code_Access_Reject = 3  # 接入拒绝回应报文
Code_Accounting_Request = 4  # 计费请求报文
Code_Accounting_Response = 5  # 计费回应报文
Code_Access_Challenge = 11  # 接入挑战(盘问)报文
Code_Status_Server_Experimental = 12  # 服务器状态报文(试验)
Code_Status_Client_Experimental = 13  # 客户端状态报文（试验）
Code_Reserved = 255  # 保留


AttributeType_User_Name = 1  # 用户名
AttributeType_User_Password = 2  # 用户密码
AttributeType_CHAP_Password = 3  # CHAP密码
AttributeType_NAS_IP_Address = 4  # NAS的IP地址
AttributeType_NAS_Port = 5  # NAS的物理端口号
AttributeType_Service_Type = 6  # 用户请求的服务类型
AttributeType_Framed_Protocol = 7  # 使用帧接入的协议
AttributeType_Framed_IP_Address = 8  # 分配给用户的IP地址
AttributeType_Framed_IP_Netmask = 9  # 分配给用户的IP地址掩码
AttributeType_Framed_Routing = 10  # 用户的路由方法
AttributeType_Filter_Id = 11  # 用户的过滤列表的名称
AttributeType_Framed_MTU = 12  # 用户的最大传输单位
AttributeType_Framed_Compression = 13  # 链路使用的压缩协议
AttributeType_Login_IP_Host = 14  # 用户连接的系统
AttributeType_Login_Service = 15  # 用户连接登录主机的服务
AttributeType_Login_TCP_Port = 16  # 用户连接到登录主机的TCP端口号
# AttributeType_Unassigned = 17
AttributeType_Reply_Message = 18  # 显示给用户的文本信息
AttributeType_Callback_Number = 19  # 用来回调的拨号字符串
AttributeType_Callback_Id = 20  # 调用场所的名字
# AttributeType_Unassigned = 21
AttributeType_Framed_Route = 22  # 在NAS上给用户配置的路由信息
AttributeType_Framed_IPX_Network = 23  # 分配给用户的IPX网络号
AttributeType_State = 24
AttributeType_Class = 25
AttributeType_Vendor_Specific = 26  # 允许厂商支持他们的扩展属性
AttributeType_Session_Timeout = 27  # 提供给用户的服务的最大秒数
AttributeType_Idle_Timeout = 28  # 提供给用户最大的连接闲置持续的最大秒数
AttributeType_Termination_Action = 29  # 当服务结束时NAS应该做何动作
AttributeType_Called_Station_Id = 30  # 允许NAS在接入请求报文中包含用户呼叫的电话号码(被叫号码)
AttributeType_Calling_Station_Id = 31  # 允许NAS在接入请求报文中包含主叫的电话号码
AttributeType_NAS_Identifier = 32  # 标识发起接入请求报文的NAS的字符串
AttributeType_Proxy_State = 33
AttributeType_Login_LAT_Service = 34
AttributeType_Login_LAT_Node = 35
AttributeType_Login_LAT_Group = 36
AttributeType_Framed_AppleTalk_Link = 37
AttributeType_Framed_AppleTalk_Network = 38
AttributeType_Framed_AppleTalk_Zone = 39
# 40-59 accounting
AttributeType_Acct_Status_Type = 40  # 计费请求报文类型
AttributeType_Acct_Delay_Time = 41  # 发送报文延误的秒数
AttributeType_Acct_Input_Octets = 42  # 用户从端口接收到的字节总数
AttributeType_Acct_Output_Octets = 43  # 用户发送到端口的字节总数
AttributeType_Acct_Session_Id = 44  # 在日志文件中匹配计费开始和计费结束记录的唯一的计费ID
AttributeType_Acct_Authentic = 45  # 用户的认证方式
AttributeType_Acct_Session_Time = 46  # 用户接受服务的时间
AttributeType_Acct_Input_Packets = 47  # 用户从端口接收到的数据包总数
AttributeType_Acct_Output_Packets = 48  # 用户发送到端口的数据包总数
AttributeType_Acct_Terminate_Cause = 49  # 表明会话如何被终止的
AttributeType_Acct_Multi_Session_Id = 50  # 唯一计费会话ID
AttributeType_Acct_Link_Count = 51  # 计费记录生成时该多链路会话的已经知道的链路个数

AttributeType_CHAP_Challenge = 60  # 由NAS发送的CHAP挑战
AttributeType_NAS_Port_Type = 61  # 用户认证的NAS的物理端口的类型
AttributeType_Port_Limit = 62  # NAS提供给用户的端口的最大数量
AttributeType_Login_LAT_Port = 63


ServiceType_Login = 1
ServiceType_Framed = 2
ServiceType_Callback_Login = 3
ServiceType_Callback_Framed = 4
ServiceType_Outbound = 5
ServiceType_Administrative = 6
ServiceType_NAS_Prompt = 7
ServiceType_Authenticate_Only = 8
ServiceType_Callback_NAS_Prompt = 9
ServiceType_Call_Check = 10
ServiceType_Callback_Administrative = 11

Acct_Status_Type_Start = 1  # 计费开始
Acct_Status_Type_Stop = 2  # 计费结束
Acct_Status_Type_Interim_Update = 3  # 计费更新
Acct_Status_Type_Interim_Accounting_On = 4  # 计费开始，通常为设备重启后
Acct_Status_Type_Interim_Accounting_Off = 5  # 计计费结束，通常为设备重启前
# 9-14 Reserved for Tunnel Accounting（为隧道计费保留）
# 15 Reserved for Failed（为计费失败保留）
