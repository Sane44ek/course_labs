<div align="center">
<h1><a id="intro">Лабораторная работа №3</a><br></h1>
<a href="https://docs.github.com/en"><img src="https://img.shields.io/static/v1?logo=github&logoColor=fff&label=&message=Docs&color=36393f&style=flat" alt="GitHub Docs"></a>
<a href="https://daringfireball.net/projects/markdown"><img src="https://img.shields.io/static/v1?logo=markdown&logoColor=fff&label=&message=Markdown&color=36393f&style=flat" alt="Markdown"></a> 
<a href="https://symbl.cc/en/unicode-table"><img src="https://img.shields.io/static/v1?logo=unicode&logoColor=fff&label=&message=Unicode&color=36393f&style=flat" alt="Unicode"></a> 
<a href="https://shields.io"><img src="https://img.shields.io/static/v1?logo=shieldsdotio&logoColor=fff&label=&message=Shields&color=36393f&style=flat" alt="Shields"></a>
<a href="https://img.shields.io/badge/Risk_Analyze-2448a2"><img src="https://img.shields.io/badge/Course-Risk_Analysis-2448a2" alt= "RA"></a> <img src="https://img.shields.io/badge/AppSec-2448a2" alt= "RA"></a> <img src="https://img.shields.io/badge/Contributor-Чередова_А.С.-8b9aff" alt="Contributor Badge"></a></div>

***

Данная лабораторная работа посвещена изучению `nmap` и как с ним работать. Эта лабораторная работа послужит подпоркой для старта в выявлении и определении уязвимостей на уровне сканера портов, что бы освоить базовые методы сканирования. 
***

## Структура репозитория лабораторной работы

```bash
lab03
├── exmp_targets.txt
└── README.md
```

***

## Материал

**Nmap Network Mapper** `open-source` утилита для исследования и анализа сетей, в которой основная цель выявление активных устройств, открытых портов, сервисов, версий ПО, ОС и других характеристик, которые способствуют определнию вектора атаки и влияния, а также перехвата управления инфраструктурой или отслеживания. Фактически она рассматривается как виртуальная сетевая карта

- **Методы:**
    - TCP - connect, 
    - TCP SYN - stealth-сканирование, 
    - UDP 
    - FIN 
    - ACK 
    - Xmas tree 
    - NULL-сканирование
    -  ICMP ping
    -  FTP-proxy 
    -  idle scan - невидимое сканирование
    -  и т.д.
- **Возможности:**
    - Определение ОС удалённых хостов с помощью отпечатков TCP/IP-стеков - OS fingerprinting
    - Определение версий сервисов на открытых портах
    - Сканирование сетей с динамическим управлением временем отправки пакетов
    - Выявление пакетных фильтров, межсетевых экранов,маршрутизации и IP-фрагментации
    - Nmap Scripting Engine позволяет автоматизировать поиск уязвимостей SQL Injection и т.д.
    - Может избегать обнаружения, используя ложные хосты и изменение поведения сканера, и т.д.
    - Может сканировать диапазон IP-адресов и множества целей
    - Помогает определить, что открытый порт указывает на то, что служба запущена и ожидает соединений

- **Команды**

```bash
$ nmap -iL targets.txt # множествнные цели сканирований
     -sL # List Scan 
     -sn # Ping Scan 
     -Pn # all hosts online
     -PS/PA/PU/PY[portlist] # TCP SYN/ACK, UDP or SCTP
     -PE/PP/PM # ICMP echo, timestamp, netmask request
     -PO[protocol list] # IP Protocol Ping
     -n/-R # Не для DNS resolution
     --dns-servers <serv1[,serv2],...> # custom DNS
     --system-dns # Используйте OS
     --traceroute 
```

-  **Типы сканирований и опции nmap**

<table>
  <thead>
    <tr>
      <th>Scan type</th>
      <th>nmap option</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>TCP (connect)</td><td>-sT</td></tr>
    <tr><td>TCP SYN</td><td>-sS</td></tr>
    <tr><td>TCP NULL</td><td>-sN</td></tr>
    <tr><td>TCP FIN</td><td>-sF</td></tr>
    <tr><td>TCP XMAS</td><td>-sX</td></tr>
    <tr><td>TCP idle (zombie)</td><td>-sI</td></tr>
    <tr><td>UDP</td><td>-sU</td></tr>
    <tr><td>OS</td><td>-A</td></tr>
  </tbody>
</table>

- **Порты**

<table>
  <thead>
    <tr>
      <th>Port</th>
      <th>Service</th>
      <th>Protocol</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>20/21</td><td>FTP (File Transfer)</td><td>TCP</td></tr>
    <tr><td>22</td><td>SSH (Secure Shell)</td><td>TCP</td></tr>
    <tr><td>23</td><td>Telnet</td><td>TCP</td></tr>
    <tr><td>25</td><td>SMTP (Simple Mail Transfer)</td><td>TCP</td></tr>
    <tr><td>53</td><td>DNS (Domain Name System)</td><td>TCP/UDP</td></tr>
    <tr><td>67/68</td><td>DHCP (Dynamic Host Configuration Protocol)</td><td>UDP</td></tr>
    <tr><td>69</td><td>TFTP (Trivial File Transfer Protocol)</td><td>UDP</td></tr>
    <tr><td>80</td><td>HTTP (Hypertext Transfer Protocol)</td><td>TCP</td></tr>
    <tr><td>110</td><td>POP3 (Post Office Protocol version 3)</td><td>TCP</td></tr>
    <tr><td>443</td><td>HTTPS (HTTP Secure)</td><td>TCP</td></tr>
    <tr><td>3306</td><td>MySQL Database</td><td>TCP</td></tr>
  </tbody>
</table>

***

### Пример результата

```bash
nmap scan report for 10.1.1.10
Host is up, received echo-reply ttl 62 (0.024s latency).
Scanned at 2023-03-06 13:31:28 CET for 573s
Not shown: 993 closed tcp ports (reset)
PORT     STATE SERVICE     REASON         VERSION
22/tcp   open  ssh         syn-ack ttl 62 OpenSSH 8.9p1 Ubuntu 3ubuntu0.1 (Ubuntu Linux; protocol 2.0)
53/tcp   open  domain      syn-ack ttl 62 dnsmasq 2.86
80/tcp   open  http        syn-ack ttl 62 Apache httpd 2.4.52 ((Ubuntu))
139/tcp  open  netbios-ssn syn-ack ttl 62 Samba smbd 4.6.2
445/tcp  open  netbios-ssn syn-ack ttl 62 Samba smbd 4.6.2
631/tcp  open  ipp         syn-ack ttl 62 CUPS 2.4
3306/tcp open  mysql       syn-ack ttl 62 MySQL (unauthorized)
Aggressive OS guesses: HP P2000 G3 NAS device (90%), Linux 2.6.32 - 3.13 (88%), Linux 2.6.32 (88%), Linux 2.6.32 - 3.1 (88%), Ubiquiti AirMax NanoStation WAP (Linux 2.6.32) (88%), Linux 3.7 (88%), Linux 5.1 (88%), Linux 5.4 (88%), Netgear RAIDiator 4.2.21 (Linux 2.6.37) (88%), Ubiquiti Pico Station WAP (AirOS 5.2.6) (88%)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.93%E=4%D=3/6%OT=22%CT=1%CU=33670%PV=Y%DS=3%DC=I%G=Y%TM=6405DF5D
OS:%P=x86_64-pc-linux-gnu)SEQ(SP=F8%GCD=1%ISR=104%TI=Z%CI=Z%II=I%TS=A)OPS(O
OS:1=M564ST11NW7%O2=M564ST11NW7%O3=M564NNT11NW7%O4=M564ST11NW7%O5=M564ST11N
OS:W7%O6=M564ST11)WIN(W1=FB28%W2=FB28%W3=FB28%W4=FB28%W5=FB28%W6=FB28)ECN(R
OS:=Y%DF=Y%T=40%W=FD5C%O=M564NNSNW7%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S=O%A=S+%F=AS%
OS:RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T5(R=Y
OS:%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R
OS:%O=%RD=0%Q=)T7(R=N)U1(R=Y%DF=N%T=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RU
OS:CK=11AA%RUD=G)IE(R=Y%DFI=N%T=40%CD=S)
```

***

## Задание

- [ ] 1. Опишите используемые методы по их назначению, как они функционируют и какие результаты могут дать для оценки. Используйте сноску из материалов выше по флагам команд.

# 1. Методы сканирования портов и хостов

| Метод | Флаг | Назначение | Как работает | Результаты | Особенности / Преимущества |
|------|------|------------|--------------|------------|----------------------------|
| TCP Connect Scan | `-sT` | Определение открытых TCP-портов с полным соединением | Полное TCP-рукопожатие: SYN → SYN/ACK ← ACK → | `open`, `closed`, `filtered` | Легко обнаруживается, не требует root |
| TCP SYN Scan (Stealth) | `-sS` | Скрытое определение TCP-портов | SYN → SYN/ACK ← (open), RST ← (closed), ACK не отправляется | `open`, `closed`, `filtered` | Менее заметен, быстрее `-sT`, стандарт для пентеста |
| UDP Scan | `-sU` | Поиск UDP-сервисов | UDP-пакет → ICMP Port Unreachable = closed, нет ответа = open\|filtered | `open`, `closed`, `open\|filtered` | Медленный, много ложных срабатываний |
| FIN Scan | `-sF` | Обход простых фильтров | TCP FIN → RST = closed, нет ответа = open\|filtered | `closed`, `open\|filtered` | Не работает против Windows |
| NULL Scan | `-sN` | Скрытое сканирование без флагов | TCP без флагов → RST = closed, нет ответа = open\|filtered | `closed`, `open\|filtered` | Использует особенности RFC |
| Xmas Tree Scan | `-sX` | Обход IDS/Firewall | TCP FIN + PSH + URG | `closed`, `open\|filtered` | Аналог FIN/NULL |
| ACK Scan | `-sA` | Определение firewall и фильтрации | TCP ACK → RST = unfiltered, нет ответа = filtered | `filtered`, `unfiltered` | Не определяет открытость порта |
| ICMP Ping Scan | `-sn` | Проверка доступности хостов | ICMP Echo, Timestamp, Netmask | Host up / Host down | При блокировке ICMP использовать `-Pn` |
| FTP Proxy Scan | `-b` | FTP-bounce сканирование | Использование команды PORT на FTP-сервере | Открытые порты | Устаревшая техника |
| Idle Scan | `-sI` | Анонимное сканирование | Использование зомби-хоста с предсказуемым IPID | Open / Closed | Максимальная скрытность |

---

# 2. Возможности Nmap (оценка безопасности)

| Возможность | Флаг | Назначение | Принцип работы | Результаты |
|------------|------|------------|----------------|------------|
| OS Fingerprinting | `-O` | Определение ОС | Анализ TCP/IP-стека (TTL, Window Size, TCP Options) | Linux, Windows, FreeBSD |
| Определение версий сервисов | `-sV` | Определение версии сервиса | Анализ баннеров и ответов | OpenSSH 8.9p1 |
| Управление таймингом | `-T0…T5` | Баланс скорость/скрытность | Управление задержками | Параноидальный → агрессивный |
| Обнаружение firewall | `-sA`, `-f`, `--mtu` | Выявление фильтрации | Анализ ответов и фрагментации | Filtered / Unfiltered |
| Traceroute | `--traceroute` | Определение маршрута | Анализ TTL-ответов | Route hops |
| Nmap Scripting Engine | `--script` | Поиск уязвимостей | Автоматизированные скрипты | SQLi, XSS, CVE |
| Обход обнаружения | `-D`, `--spoof-mac`, `-f`, `-sI` | Сокрытие сканирования | Ложные хосты, фрагментация | Снижение детекта |
| Массовое сканирование | `-iL` | Сканирование множества целей | Списки и диапазоны | Массовый аудит |
| Интерпретация портов | — | Анализ открытых портов | Анализ состояния | Точка атаки |

---

# 3. Используемые команды (сноска)

| Команда | Назначение |
|-------|------------|
| `-iL targets.txt` | Сканирование списка целей |
| `-sL` | List Scan |
| `-sn` | Ping Scan |
| `-Pn` | Считать все хосты online |
| `-PS/-PA/-PU/-PY` | TCP / UDP / SCTP probes |
| `-PE/-PP/-PM` | ICMP Echo / Timestamp / Netmask |
| `-PO` | IP Protocol Scan |
| `-n` / `-R` | Управление DNS |
| `--dns-servers` | Кастомный DNS |
| `--system-dns` | DNS ОС |
| `--traceroute` | Определение маршрута |



- [x] 2. Выведите на терминале и проанализируйте следующие команды консоли

```bash
$ nmap localhost

acher@LAPTOP-G8JP4BBC:~/course_labs/labs/lab03% nmap localhost
Starting Nmap 7.80 ( https://nmap.org ) at 2025-12-15 18:46 MSK
Nmap scan report for localhost (127.0.0.1)
Host is up (0.000081s latency).
All 1000 scanned ports on localhost (127.0.0.1) are closed

Nmap done: 1 IP address (1 host up) scanned in 0.06 seconds

$ nmap -sC localhost

acher@LAPTOP-G8JP4BBC:~/course_labs/labs/lab03% nmap -sC localhost
Starting Nmap 7.80 ( https://nmap.org ) at 2025-12-15 18:46 MSK
Nmap scan report for localhost (127.0.0.1)
Host is up (0.000063s latency).
All 1000 scanned ports on localhost (127.0.0.1) are closed

Nmap done: 1 IP address (1 host up) scanned in 0.34 seconds


$ nmap -p localhost

acher@LAPTOP-G8JP4BBC:~/course_labs/labs/lab03% nmap -p 8080 localhost
Starting Nmap 7.80 ( https://nmap.org ) at 2025-12-15 18:47 MSK
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00013s latency).

PORT     STATE  SERVICE
8080/tcp closed http-proxy

Nmap done: 1 IP address (1 host up) scanned in 0.03 seconds


$ nmap -O localhost

acher@LAPTOP-G8JP4BBC:~/course_labs/labs/lab03% sudo nmap -O localhost
Starting Nmap 7.80 ( https://nmap.org ) at 2025-12-15 18:47 MSK
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00016s latency).
All 1000 scanned ports on localhost (127.0.0.1) are closed
Too many fingerprints match this host to give specific OS details
Network Distance: 0 hops

OS detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 1.68 seconds


$ nmap -p 80 localhost
$ nmap -p 443 localhost

acher@LAPTOP-G8JP4BBC:~/course_labs/labs/lab03% nmap -p 443 localhost
Starting Nmap 7.80 ( https://nmap.org ) at 2025-12-15 18:47 MSK
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00014s latency).

PORT    STATE  SERVICE
443/tcp closed https

Nmap done: 1 IP address (1 host up) scanned in 0.03 seconds

$ nmap -p 8443 localhost

acher@LAPTOP-G8JP4BBC:~/course_labs/labs/lab03% nmap -p 8443 localhost
Starting Nmap 7.80 ( https://nmap.org ) at 2025-12-15 18:48 MSK
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00012s latency).

PORT     STATE  SERVICE
8443/tcp closed https-alt

Nmap done: 1 IP address (1 host up) scanned in 0.03 seconds

$ nmap -p "*" localhost

acher@LAPTOP-G8JP4BBC:~/course_labs/labs/lab03% nmap -p "*" localhost
Starting Nmap 7.80 ( https://nmap.org ) at 2025-12-15 18:48 MSK
Nmap scan report for localhost (127.0.0.1)
Host is up (0.000066s latency).
All 8320 scanned ports on localhost (127.0.0.1) are closed

Nmap done: 1 IP address (1 host up) scanned in 0.13 seconds


$ nmap -sV -p 22,8080 localhost

acher@LAPTOP-G8JP4BBC:~/course_labs/labs/lab03% nmap -sV -p 22,8080 localhost
Starting Nmap 7.80 ( https://nmap.org ) at 2025-12-15 18:48 MSK
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00013s latency).

PORT     STATE  SERVICE    VERSION
22/tcp   closed ssh
8080/tcp closed http-proxy

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 0.33 seconds

$ nmap -sP 192.168.1.0/24

acher@LAPTOP-G8JP4BBC:~/course_labs/labs/lab03% nmap -sP 192.168.1.0/24
Starting Nmap 7.80 ( https://nmap.org ) at 2025-12-15 18:49 MSK
Nmap done: 256 IP addresses (0 hosts up) scanned in 103.23 seconds

$ nmap --open 192.168.1.1

acher@LAPTOP-G8JP4BBC:~/course_labs/labs/lab03% nmap --open 192.168.1.1
Starting Nmap 7.80 ( https://nmap.org ) at 2025-12-15 18:51 MSK
Note: Host seems down. If it is really up, but blocking our ping probes, try -Pn
Nmap done: 1 IP address (0 hosts up) scanned in 3.04 seconds

$ nmap --packet-trace 192.168.1.1

acher@LAPTOP-G8JP4BBC:~/course_labs/labs/lab03% nmap --open 192.168.1.1
Starting Nmap 7.80 ( https://nmap.org ) at 2025-12-15 18:51 MSK
Note: Host seems down. If it is really up, but blocking our ping probes, try -Pn
Nmap done: 1 IP address (0 hosts up) scanned in 3.04 seconds
acher@LAPTOP-G8JP4BBC:~/course_labs/labs/lab03% nmap --packet-trace 192.168.1.1
Starting Nmap 7.80 ( https://nmap.org ) at 2025-12-15 18:51 MSK
CONN (0.0324s) TCP localhost > 192.168.1.1:80 => Operation now in progress
CONN (0.0325s) TCP localhost > 192.168.1.1:443 => Operation now in progress
CONN (2.0346s) TCP localhost > 192.168.1.1:443 => Operation now in progress
CONN (2.0348s) TCP localhost > 192.168.1.1:80 => Operation now in progress
Note: Host seems down. If it is really up, but blocking our ping probes, try -Pn
Nmap done: 1 IP address (0 hosts up) scanned in 3.04 seconds

$ nmap --packet-trace scanme.nmap.org 

acher@LAPTOP-G8JP4BBC:~/course_labs/labs/lab03% nmap --packet-trace scanme.nmap.org
Starting Nmap 7.80 ( https://nmap.org ) at 2025-12-15 18:52 MSK
CONN (0.2730s) TCP localhost > 45.33.32.156:80 => Operation now in progress
CONN (0.2736s) TCP localhost > 45.33.32.156:443 => Operation now in progress
CONN (0.5136s) TCP localhost > 45.33.32.156:80 => Connected
NSOCK INFO [0.5170s] nsock_iod_new2(): nsock_iod_new (IOD #1)
NSOCK INFO [0.5170s] nsock_connect_udp(): UDP connection requested to 1.1.1.1:53 (IOD #1) EID 8
NSOCK INFO [0.5170s] nsock_read(): Read request from IOD #1 [1.1.1.1:53] (timeout: -1ms) EID 18
NSOCK INFO [0.5170s] nsock_iod_new2(): nsock_iod_new (IOD #2)
NSOCK INFO [0.5180s] nsock_connect_udp(): UDP connection requested to 8.8.8.8:53 (IOD #2) EID 24
NSOCK INFO [0.5180s] nsock_read(): Read request from IOD #2 [8.8.8.8:53] (timeout: -1ms) EID 34
NSOCK INFO [0.5180s] nsock_write(): Write request for 43 bytes to IOD #1 EID 43 [1.1.1.1:53]
NSOCK INFO [0.5190s] nsock_trace_handler_callback(): Callback: CONNECT SUCCESS for EID 8 [1.1.1.1:53]
NSOCK INFO [0.5190s] nsock_trace_handler_callback(): Callback: WRITE SUCCESS for EID 43 [1.1.1.1:53]
NSOCK INFO [0.5190s] nsock_trace_handler_callback(): Callback: CONNECT SUCCESS for EID 24 [8.8.8.8:53]
NSOCK INFO [0.8980s] nsock_trace_handler_callback(): Callback: READ SUCCESS for EID 18 [1.1.1.1:53] (72 bytes): .e...........156.32.33.45.in-addr.arpa..............,...scanme.nmap.org.


$ nmap --iflist


acher@LAPTOP-G8JP4BBC:~/course_labs/labs/lab03% nmap --iflist
Starting Nmap 7.80 ( https://nmap.org ) at 2025-12-15 18:53 MSK
************************INTERFACES************************
DEV  (SHORT) IP/MASK                     TYPE     UP MTU   MAC
lo   (lo)    127.0.0.1/8                 loopback up 65536
lo   (lo)    10.255.255.254/8            loopback up 65536
lo   (lo)    ::1/128                     loopback up 65536
eth0 (eth0)  172.23.232.16/20            ethernet up 1500  00:15:5D:8D:1B:B7
eth0 (eth0)  fe80::215:5dff:fe8d:1bb7/64 ethernet up 1500  00:15:5D:8D:1B:B7

**************************ROUTES**************************
DST/MASK                     DEV  METRIC GATEWAY
172.23.224.0/20              eth0 0
0.0.0.0/0                    eth0 0      172.23.224.1
::1/128                      lo   0
fe80::215:5dff:fe8d:1bb7/128 eth0 0
fe80::/64                    eth0 256
ff00::/8                     eth0 256


$ nmap -iL scanme.nmap.org 

acher@LAPTOP-G8JP4BBC:~/course_labs/labs/lab03% nmap -iL exmp_targets.txt
Starting Nmap 7.80 ( https://nmap.org ) at 2025-12-15 18:54 MSK
Nmap scan report for localhost (127.0.0.1)
Host is up (0.000075s latency).
All 1000 scanned ports on localhost (127.0.0.1) are closed

Nmap done: 4 IP addresses (1 host up) scanned in 1.26 seconds

$ nmap -A -iL scanme.nmap.org

acher@LAPTOP-G8JP4BBC:~/course_labs/labs/lab03%  nmap -A -iL exmp_targets.txt
Starting Nmap 7.80 ( https://nmap.org ) at 2025-12-15 18:55 MSK
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00013s latency).
All 1000 scanned ports on localhost (127.0.0.1) are closed

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 4 IP addresses (1 host up) scanned in 1.67 seconds

$ nmap -sA scanme.nmap.org

acher@LAPTOP-G8JP4BBC:~/course_labs/labs/lab03% sudo nmap -sA scanme.nmap.org
Starting Nmap 7.80 ( https://nmap.org ) at 2025-12-15 18:56 MSK
Nmap scan report for scanme.nmap.org (45.33.32.156)
Host is up (0.27s latency).
Other addresses for scanme.nmap.org (not scanned): 2600:3c01::f03c:91ff:fe18:bb2f
All 1000 scanned ports on scanme.nmap.org (45.33.32.156) are filtered

Nmap done: 1 IP address (1 host up) scanned in 19.00 seconds


$ nmap -PN scanme.nmap.org 

acher@LAPTOP-G8JP4BBC:~/course_labs/labs/lab03% nmap -PN scanme.nmap.org
Starting Nmap 7.80 ( https://nmap.org ) at 2025-12-15 18:56 MSK
Nmap scan report for scanme.nmap.org (45.33.32.156)
Host is up (0.26s latency).
Other addresses for scanme.nmap.org (not scanned): 2600:3c01::f03c:91ff:fe18:bb2f
Not shown: 995 closed ports
PORT      STATE SERVICE
21/tcp    open  ftp
22/tcp    open  ssh
80/tcp    open  http
9929/tcp  open  nping-echo
31337/tcp open  Elite

Nmap done: 1 IP address (1 host up) scanned in 22.18 seconds

$ nmap --script=vuln IP_addr -vv

acher@LAPTOP-G8JP4BBC:~/course_labs/labs/lab03% nmap --script=vuln IP_addr -vv
Starting Nmap 7.80 ( https://nmap.org ) at 2025-12-15 18:56 MSK
NSE: Loaded 105 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 2) scan.
Initiating NSE at 18:56
Completed NSE at 18:57, 10.01s elapsed
NSE: Starting runlevel 2 (of 2) scan.
Initiating NSE at 18:57
Completed NSE at 18:57, 0.00s elapsed
Failed to resolve "IP_addr".
NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 2) scan.
Initiating NSE at 18:57
Completed NSE at 18:57, 0.00s elapsed
NSE: Starting runlevel 2 (of 2) scan.
Initiating NSE at 18:57
Completed NSE at 18:57, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
WARNING: No targets were specified, so 0 hosts scanned.
Nmap done: 0 IP addresses (0 hosts up) scanned in 10.41 seconds


$ nmap -sV --script vuln -oN nmapres_new.txt localhost

acher@LAPTOP-G8JP4BBC:~/course_labs/labs/lab03% nmap -sV --script vuln -oN nmapres_new.txt localhost
Starting Nmap 7.80 ( https://nmap.org ) at 2025-12-15 18:57 MSK
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00011s latency).
All 1000 scanned ports on localhost (127.0.0.1) are closed

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 10.54 seconds

$ cat > ./nmapres_new.txt # сделать подобный пример файлу exmp_targets.txt
$ grep "VULNERABLE" nmapres_new.txt

$ mkdir -p ~/project/reports
$ nmap -sV -p 8080 --script vuln -oN ~/project/reports/nmapres_new.txt -oX ~/project/reports/nmapres_new.xml localhost

acher@LAPTOP-G8JP4BBC:~/course_labs/labs/lab03% nmap -sV -p 8080 --script vuln -oN ~/project/reports/nmapres_new.txt -oX ~/project/reports/nmapres_new.xml localhost
Starting Nmap 7.80 ( https://nmap.org ) at 2025-12-15 18:58 MSK
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00017s latency).

PORT     STATE  SERVICE    VERSION
8080/tcp closed http-proxy

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 10.45 seconds

$ xsltproc ~/project/reports/nmapres_new.xml -o ~/project/reports/nmapres_new.html

<img width="1588" height="1288" alt="image" src="https://gist.github.com/user-attachments/assets/a7b60f89-765d-4e02-b080-5f8a50a013c5" />


```

- [x] 3. Используйте команду `tree` и выведите все вложенные файлы по директориям.


```bash
acher@LAPTOP-G8JP4BBC:~/course_labs/labs/lab03% tree
.
├── README.md
├── exmp_targets.txt
└── nmapres_new.txt

0 directories, 3 files
```
- [x] 4.Найдите IP сетевой карты `Ethernet`, которая соответствует вашей виртуальной машине используя `ifconfig` и выполните команду

```bash
    inet 172.23.232.16/20 brd 172.23.239.255 scope global eth0

$ nmap -sP inet_addr

acher@LAPTOP-G8JP4BBC:~/course_labs/labs/lab03% nmap -sP 172.23.232.16  Starting Nmap 7.80 ( https://nmap.org ) at 2025-12-15 19:02 MSK
Nmap scan report for 172.23.232.16
Host is up (0.00031s latency).
Nmap done: 1 IP address (1 host up) scanned in 0.07 seconds
```

- [x] 5. Определите ОС, данные ssh, telnet  с помощью `nmap` и выведитео них информацию.

```bash
acher@LAPTOP-G8JP4BBC:~/course_labs/labs/lab03% sudo nmap -O -sV -p 22,23 localhost
Starting Nmap 7.80 ( https://nmap.org ) at 2025-12-15 19:03 MSK
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00013s latency).

PORT   STATE  SERVICE VERSION
22/tcp closed ssh
23/tcp closed telnet
Too many fingerprints match this host to give specific OS details
Network Distance: 0 hops

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 2.05 seconds
```

- [x] 6. Результаты из `nmapres_new.txt` надо перенести в `nmapres.txt` и оставить оба файла рядом в локальном репозитории. Желательно использовать `cp` в консоли через редактор.

```bash
acher@LAPTOP-G8JP4BBC:~/course_labs/labs/lab03% cp nmapres_new.txt nmapres.txt
acher@LAPTOP-G8JP4BBC:~/course_labs/labs/lab03% ls
README.md  exmp_targets.txt  nmapres.txt  nmapres_new.txt
acher@LAPTOP-G8JP4BBC:~/course_labs/labs/lab03%
```

- [ ] 7. Оформить `README.md` по аналогии и использовать `shield`, etc.
- [ ] 8. Составить `gist` отчет и отправить ссылку личным сообщением

***

## Links

- [Markdown](https://stackedit.io)
- [GitHub CLI](https://cli.github.com)
- [Gist](https://gist.github.com)
- [IANA](https://www.iana.org)
- [IANA Port Numbers](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml)
- [Nmap GitHub](https://github.com/nmap/nmap)
- [Официальная документация nmap](https://nmap.org/book/)
- [Nmap Reference Guide](https://nmap.org/book/man.html)
- [Nmap Script (NSE) Reference](https://nmap.org/nsedoc/)
- [Nmap Tutorial (Hackers-Arise)](https://nmap.org/docs.html)
- [OWASP Testing Guide – Network Scanning](https://owasp.org/www-project-web-security-testing-guide/)

Copyright (c) 2025 Elijah S Shmakov

![Logo](../../assets/logotype/logo.jpg)
