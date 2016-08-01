#!/usr/bin/env python
# coding: utf-8

import libs.requests as requests
import config
import Queue
import threading


class Dirbrute(object):
    def __init__(self, scan_target, scan_thread, scan_status, scan_timeout):
        print 'Start Scan...'
        self.scan_target = scan_target
        self.scan_thread = scan_thread
        self.scan_status = scan_status
        self.scan_timeout = scan_timeout
        self._loadHeaders()
        self._urlstatus()
        self._loadDict()
        self.lock = threading.Lock()
        # print self.scan_thread

    def _loadHeaders(self):
        self.headers = {
            'Accept': '*/*',
            'Referer': self.scan_target,
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; ',
            'Cache-Control': 'no-cache',
        }

    def _urlstatus(self):
        if self.scan_status == 1:
            self.code_match = 200
        elif self.scan_status == 2:
            self.code_match = 302

    def _loadDict(self):
        self.dirlist = Queue.Queue()
        # s = 0
        with open(config.directory_dict) as f:
            for line in f.readlines():
                if line.find('#') == -1 and line != '':
                    self.dirlist.put(self.scan_target + line.strip())
                    # s = s + 1
                    # print line.strip()
        print '文件数量:',
        print self.dirlist.qsize()
        # print s

    def _notfound(self):
        pass

    def _scan(self):
        while self.dirlist.empty() is False:
            url = self.dirlist.get()
            try:
                res = requests.get(url, headers=self.headers, timeout=self.scan_timeout, allow_redirects=False)
                # print res.url
                if res.status_code == self.code_match or res.status_code == requests.codes.ok:
                    print '[' + str(res.status_code) + ']' + " " + url
                    self.lock.acquire()
                    with open(config.report_path, 'a') as infile:
                        infile.write(url + '\n')
                    self.lock.release()
            except Exception, e:
                # print e
                pass
            self.dirlist.task_done()

    def run(self):
        for i in range(self.scan_thread):
            t = threading.Thread(target=self._scan, name=str(i))
            t.setDaemon(True)
            t.start()
            # t.join()

        while True:
            if threading.activeCount() <= 1:
                break
        print 'Scan End!'
