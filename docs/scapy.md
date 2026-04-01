# 网络包处理工具

Scapy 是一个强大的 Python 网络数据包处理库，支持创建、发送、捕获和分析网络数据包。

官网：[https://scapy.net/](https://scapy.net/)，文档参考：[https://scapy.readthedocs.io/en/latest/](https://scapy.readthedocs.io/en/latest/)

## 0x01. 安装

```shell
pip install scapy

# Windows 可能需要安装 Npcap
# https://npcap.com/

# Linux 可能需要权限
# sudo pip install scapy
```

## 0x02. 基本使用

### 导入和启动

```python
from scapy.all import *

# 查看可用协议
ls()

# 查看特定协议
ls(IP)
ls(TCP)
ls(UDP)

# 交互式 shell
# 在命令行运行: scapy
```

### 创建数据包

```python
from scapy.all import *

# 创建简单的 IP 数据包
packet = IP(dst="8.8.8.8")
print(packet)

# 创建 ICMP 数据包（ping）
ping_packet = IP(dst="8.8.8.8")/ICMP()
print(ping_packet)

# 创建 TCP 数据包
tcp_packet = IP(dst="192.168.1.1")/TCP(dport=80, flags="S")
print(tcp_packet)

# 创建 UDP 数据包
udp_packet = IP(dst="192.168.1.1")/UDP(dport=53)/DNS(qd=DNSQR(qname="example.com"))
print(udp_packet)

# 查看数据包摘要
print(ping_packet.summary())
print(ping_packet.show())
```

## 0x03. 发送和接收数据包

### 发送数据包

```python
from scapy.all import *

# 发送 ICMP 数据包（Layer 3）
send(IP(dst="8.8.8.8")/ICMP())

# 发送并接收响应
reply = sr1(IP(dst="8.8.8.8")/ICMP())
print(reply.summary())

# 发送 TCP SYN 包
reply = sr1(IP(dst="192.168.1.1")/TCP(dport=80, flags="S"))
if reply:
    print(reply.summary())

# 发送 UDP 数据包
send(IP(dst="8.8.8.8")/UDP(dport=53)/DNS(qd=DNSQR(qname="example.com")))
```

### 发送和接收多个数据包

```python
from scapy.all import *

# 发送多个包并收集响应
ans, unans = sr(IP(dst=["8.8.8.8", "8.8.4.4"])/ICMP())
print(f"收到 {len(ans)} 个响应")
print(f"未收到 {len(unans)} 个响应")

# 打印响应
for sent, received in ans:
    print(f"从 {received.src} 收到响应")
```

### 高级发送选项

```python
from scapy.all import *

# 指定接口发送
sendp(Ether()/IP(dst="8.8.8.8")/ICMP(), iface="eth0")

# 发送并等待响应
reply = sr1(IP(dst="8.8.8.8")/ICMP(), timeout=2)
if reply:
    print(f"收到响应: {reply.src}")
else:
    print("超时，未收到响应")

# 发送多个包并设置超时
ans, unans = sr(IP(dst="8.8.8.8")/ICMP(), count=5, timeout=2)
```

## 0x04. 数据包嗅探

### 基本嗅探

```python
from scapy.all import *

# 嗅探数据包
packets = sniff(count=10)  # 捕获10个包
print(f"捕获了 {len(packets)} 个数据包")

# 打印每个包的摘要
for pkt in packets:
    print(pkt.summary())

# 嗅探特定协议
packets = sniff(filter="tcp", count=10)  # 只捕获TCP包

# 嗅探特定主机
packets = sniff(filter="host 192.168.1.1", count=10)

# 嗅探特定端口
packets = sniff(filter="port 80", count=10)
```

### 高级嗅探

```python
from scapy.all import *

# 实时嗅探并处理
def packet_callback(packet):
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        print(f"IP包: {src_ip} -> {dst_ip}")
    
    if packet.haslayer(TCP):
        src_port = packet[TCP].sport
        dst_port = packet[TCP].dport
        print(f"TCP: {src_port} -> {dst_port}")

# 开始嗅探
sniff(iface="eth0", prn=packet_callback, count=100)

# 过滤并处理特定数据包
def process_http(packet):
    if packet.haslayer(TCP) and packet[TCP].dport == 80:
        print(f"HTTP请求到: {packet[IP].dst}")

sniff(filter="tcp port 80", prn=process_http, count=10)
```

### 保存和读取数据包

```python
from scapy.all import *

# 嗅探并保存到文件
packets = sniff(count=100)
wrpcap("captured.pcap", packets)

# 从文件读取
packets = rdpcap("captured.pcap")
print(f"从文件读取了 {len(packets)} 个数据包")

# 分析保存的包
for pkt in packets:
    print(pkt.summary())
```

## 0x05. 网络扫描

### 主机发现

```python
from scapy.all import *

# ARP 扫描局域网
ans, unans = arping("192.168.1.0/24")
for sent, received in ans:
    print(f"主机 {received.psrc} 存活 (MAC: {received.hwsrc})")

# ICMP ping 扫描
ans, unans = sr(IP(dst="192.168.1.1-10")/ICMP(), timeout=2)
for sent, received in ans:
    print(f"主机 {received.src} 存活")
```

### 端口扫描

```python
from scapy.all import *

# TCP SYN 扫描
def syn_scan(target, ports):
    open_ports = []
    for port in ports:
        pkt = IP(dst=target)/TCP(dport=port, flags="S")
        resp = sr1(pkt, timeout=1, verbose=0)
        if resp and resp.haslayer(TCP) and resp[TCP].flags == 0x12:  # SYN-ACK
            open_ports.append(port)
            # 发送 RST 关闭连接
            send(IP(dst=target)/TCP(dport=port, flags="R"), verbose=0)
    return open_ports

# 扫描常见端口
target = "192.168.1.1"
common_ports = [21, 22, 23, 25, 53, 80, 110, 443, 993, 995]
open_ports = syn_scan(target, common_ports)
print(f"开放端口: {open_ports}")
```

### 服务识别

```python
from scapy.all import *

def identify_service(target, port):
    """尝试识别服务"""
    pkt = IP(dst=target)/TCP(dport=port, flags="S")
    resp = sr1(pkt, timeout=2, verbose=0)
    
    if resp and resp.haslayer(TCP) and resp[TCP].flags == 0x12:
        # 发送 RST
        send(IP(dst=target)/TCP(dport=port, flags="R"), verbose=0)
        
        # 根据端口猜测服务
        services = {
            21: "FTP",
            22: "SSH",
            23: "Telnet",
            25: "SMTP",
            53: "DNS",
            80: "HTTP",
            443: "HTTPS",
            3306: "MySQL",
            5432: "PostgreSQL"
        }
        return services.get(port, "未知服务")
    return None

target = "192.168.1.1"
for port in [22, 80, 443]:
    service = identify_service(target, port)
    if service:
        print(f"端口 {port}: {service}")
```

## 0x06. 协议分析

### HTTP 分析

```python
from scapy.all import *

# 嗅探 HTTP 流量
def analyze_http(packet):
    if packet.haslayer(TCP) and packet.haslayer(Raw):
        payload = packet[Raw].load.decode('utf-8', errors='ignore')
        if 'HTTP' in payload or 'GET' in payload or 'POST' in payload:
            print(f"HTTP 流量: {packet[IP].src}:{packet[TCP].sport} -> {packet[IP].dst}:{packet[TCP].dport}")
            print(payload[:200])  # 显示前200字符
            print("-" * 50)

sniff(filter="tcp port 80", prn=analyze_http, count=10)
```

### DNS 分析

```python
from scapy.all import *

# 嗅探 DNS 查询
def analyze_dns(packet):
    if packet.haslayer(DNS) and packet.haslayer(DNSQR):
        query = packet[DNSQR].qname.decode()
        print(f"DNS 查询: {query}")
        print(f"查询类型: {packet[DNSQR].qtype}")

sniff(filter="udp port 53", prn=analyze_dns, count=10)

# 发送 DNS 查询
dns_query = IP(dst="8.8.8.8")/UDP(dport=53)/DNS(qd=DNSQR(qname="example.com"))
response = sr1(dns_query)
if response and response.haslayer(DNS):
    print(f"DNS 响应: {response[DNS].summary()}")
```

### ARP 分析

```python
from scapy.all import *

# 嗅探 ARP 流量
def analyze_arp(packet):
    if packet.haslayer(ARP):
        arp = packet[ARP]
        if arp.op == 1:  # ARP 请求
            print(f"ARP 请求: {arp.psrc} 询问 {arp.pdst} 的 MAC")
        elif arp.op == 2:  # ARP 响应
            print(f"ARP 响应: {arp.psrc} 的 MAC 是 {arp.hwsrc}")

sniff(filter="arp", prn=analyze_arp, count=10)
```

## 0x07. 数据包构造

### 自定义数据包

```python
from scapy.all import *

# 创建自定义数据包
class MyPacket(Packet):
    name = "My Custom Packet"
    fields_desc = [
        ByteField("version", 1),
        ShortField("length", 0),
        StrField("data", "")
    ]

# 使用自定义数据包
pkt = MyPacket(version=2, data="Hello")
print(pkt.show())

# 构造完整的数据包
full_pkt = Ether()/IP()/TCP()/MyPacket(version=2, data="Hello")
print(full_pkt.show())
```

### 批量数据包构造

```python
from scapy.all import *

# 构造多个数据包
packets = []
for i in range(10):
    pkt = IP(src=f"192.168.1.{i+1}", dst="8.8.8.8")/ICMP()
    packets.append(pkt)

# 发送所有数据包
send(packets, verbose=0)

# 使用 fuzz 自动填充
pkt = IP(dst="8.8.8.8")/fuzz(TCP())/Raw(load="test")
print(pkt.show())
```

## 0x08. 实用示例

### 简单端口扫描器

```python
from scapy.all import *
import sys

def port_scanner(target, start_port, end_port):
    """简单端口扫描器"""
    print(f"扫描 {target} 的端口 {start_port}-{end_port}")
    
    open_ports = []
    for port in range(start_port, end_port + 1):
        pkt = IP(dst=target)/TCP(dport=port, flags="S")
        resp = sr1(pkt, timeout=0.5, verbose=0)
        
        if resp and resp.haslayer(TCP) and resp[TCP].flags == 0x12:
            open_ports.append(port)
            print(f"端口 {port} 开放")
            # 发送 RST
            send(IP(dst=target)/TCP(dport=port, flags="R"), verbose=0)
    
    return open_ports

# 使用示例
target = "192.168.1.1"
open_ports = port_scanner(target, 1, 100)
print(f"扫描完成，开放端口: {open_ports}")
```

### 简单嗅探器

```python
from scapy.all import *

def simple_sniffer(interface, packet_count=100):
    """简单嗅探器"""
    print(f"在接口 {interface} 上嗅探 {packet_count} 个数据包...")
    
    def process_packet(packet):
        if packet.haslayer(IP):
            src = packet[IP].src
            dst = packet[IP].dst
            proto = packet[IP].proto
            
            if packet.haslayer(TCP):
                sport = packet[TCP].sport
                dport = packet[TCP].dport
                print(f"TCP: {src}:{sport} -> {dst}:{dport}")
            elif packet.haslayer(UDP):
                sport = packet[UDP].sport
                dport = packet[UDP].dport
                print(f"UDP: {src}:{sport} -> {dst}:{dport}")
            elif packet.haslayer(ICMP):
                print(f"ICMP: {src} -> {dst}")
    
    sniff(iface=interface, prn=process_packet, count=packet_count)

# 使用示例（需要管理员权限）
# simple_sniffer("eth0", 50)
```

### 简单 ARP 欺骗检测

```python
from scapy.all import *

def detect_arp_spoof(interface="eth0"):
    """检测 ARP 欺骗"""
    arp_table = {}
    
    def process_arp(packet):
        if packet.haslayer(ARP):
            arp = packet[ARP]
            if arp.op == 2:  # ARP 响应
                ip = arp.psrc
                mac = arp.hwsrc
                
                if ip in arp_table:
                    if arp_table[ip] != mac:
                        print(f"警告: ARP 欺骗检测到!")
                        print(f"IP {ip} 的 MAC 从 {arp_table[ip]} 变为 {mac}")
                else:
                    arp_table[ip] = mac
                    print(f"记录: {ip} -> {mac}")
    
    print("开始 ARP 欺骗检测...")
    sniff(filter="arp", prn=process_arp, store=0)

# 使用示例（需要管理员权限）
# detect_arp_spoof()
```

## 参考
1. [Scapy 官方文档](https://scapy.readthedocs.io/en/latest/)
2. [Scapy GitHub](https://github.com/secdev/scapy)
3. [Scapy 教程](https://scapy.readthedocs.io/en/latest/usage.html)