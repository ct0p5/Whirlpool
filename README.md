usage：
whirlpool.py [-h] -u SCAN_TARGET [-t SCAN_THREAD] [-s SCAN_STATUS]
                    [--timeout SCAN_TIMEOUT]

optional arguments:
  -h, --help            
            show this help message and exit
  -u,--url SCAN_TARGET
            Website for scan, eg: http://www.example.com
  -t,--thread SCAN_THREAD
            Scan threads, default is 20
  -s,--status_code SCAN_STATUS
            option "1":Return urls of 200 status_code. 
            option "2":Return urls of 200+403 status_code. 
            default is 1
  --timeout SCAN_TIMEOUT
            Set Timeout,default is 3
