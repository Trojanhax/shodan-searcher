# Shodan Dorks for Exploration
Shodan dorks that can be used to discover various devices and services on the internet. Please note that these dorks are for educational and research purposes only. Always use Shodan and similar tools responsibly, and do not engage in any illegal or malicious activities.

## Webcams and IoT Devices
```bash
webcam
port:554 has_screenshot:true
port:80 title:"netcam"
port:80 title:"webcamXP"
port:80 title:"Axis 200+"
port:1025 os:"Linux 2.6.13 - 2.6.32"
port:81 "Server: GoAhead-Webs"
```
## Industrial Control Systems (ICS)
```bash
port:502 product:"Modbus"
port:502 product:"S7-300"
port:44818 product:"DNP3"
port:2404 os:"WinPAC"
port:4911 "WAGO"
```
## Network Attached Storage (NAS)
```bash
port:80 "Server: Synology"
port:5000 "DiskStation"
port:5000 title:"DiskStation"
port:5000 "Synology RackStation"
port:7000 "Server: Buffalo"
port:8090 "Synology"
```
## Databases and Servers
```bash
port:1433
port:3306
port:5432
port:1521
port:27017
port:5984
```
## VoIP Systems
```bash
port:5060 "Server: Asterisk"
port:5060 "Cisco/SPA"
port:5060 "Elastix"
port:5060 "3CX"
port:5060 "Yealink"
port:5060 "Grandstream"
```
## Remote Desktop Protocol (RDP)
```bash
port:3389
port:3389 "authentication disabled"
port:3389 "Server: RFB"
port:3389 "Microsoft Terminal Server"
port:3389 os:"Windows"
```
## Vulnerable Services
```bash
port:445
port:135
port:139
port:5900
port:11211 "stats" 
```
## HTTP Server Banner
```bash
port:80 "Server: Apache"
port:80 "Server: Microsoft-IIS"
port:80 "Server: nginx"
port:80 "Server: lighttpd"
port:80 "Server: Tomcat"
```
## Open FTP Servers
```bash
port:21
port:21 "220 (vsFTPd"
port:21 "220 Microsoft FTP Service"
port:21 "220 Welcome to Pure-FTPd"
port:21 "220 ProFTPD"
```
## Printers and Fax Machines
```bash
port:515
port:9100
port:9101
port:631
port:3390 "Server: CUPS"
```
## Web Vulnerabilities
```bash
port:80 "powered by PHP"
port:80 "powered by ASP.NET"
port:80 "powered by JBoss"
port:80 "powered by Ruby"
port:80 "powered by Python"
```
## Elasticsearch Servers
```bash
port:9200 "Server: Elasticsearch"
port:9300 "Server: Elasticsearch"
```
## Unsecured Redis Servers
```bash
port:6379
port:6379 "redis_version"
```
## MongoDB Databases
```bash
port:27017
port:27017 "MongoDB Server Information"
```
## MySQL Databases
```bash
port:3306
port:3306 "Server: MySQL"
```
## PostgreSQL Databases
```bash
port:5432
port:5432 "Server: PostgreSQL"
```
## Cassandra Databases
```bash
port:9042
port:9160
```
## Open Telnet Services
```bash
port:23
port:2323
port:23230
port:992
```
## Remote Desktop Protocol (RDP)
```bash
port:3389
port:3389 "authentication disabled"
```
## VNC Services
```bash
port:5900
port:5901
port:5800
port:5902
```
## Insecure Webmin Instances
```bash
port:10000
port:10000 "MiniServ"
port:10000 "Webmin"
```
## Cisco Devices
```bash
port:23 "Cisco"
port:80 "Cisco HTTP server"
```
## Network Cameras
```bash
port:554 "RTSP/1.0"
port:554 "Server: Hikvision"
```
## Printers
```bash
port:9100 "HP JetDirect"
port:9100 "Server: Kyocera"
```
## Jenkins Servers
```bash
port:8080 "Server: Jetty"
```
## Network Attached Storage (NAS)
```bash
port:5000 "DiskStation"
port:5001 "DSM"
```
## Git Web Interfaces
```bash
port:80 "Server: git"
```
## ginx Web Servers
```bash
port:80 "Server: nginx"
port:443 "Server: nginx"
```
## Jenkins Servers
```bash
port:8080 "Server: Jenkins"
port:8080 "title:Dashboard [Jenkins]"
port:8080 "X-Jenkins"
```
