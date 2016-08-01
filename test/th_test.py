#!/usr/bin/env python
# coding: utf-8

import Queue
import threading
import requests


class th(threading.Thread):
    def __init__(self, url, urllist, name):
        super(th, self).__init__()
        self.url = url
        self.urllist = urllist
        self.name = name

    def run(self):
        print 'Start thread' + self.name
        scan(self.url, self.urllist)


def loaddict(path):
    urllist = Queue.Queue()
    with open(path, 'r') as f:
        for line in f.readlines():
            urllist.put(line.strip())
        # print self.urllist.qsize()
        # 为10，没有问题
    return urllist


def scan(url, urllist):
    while not urllist.empty():
        scan_url = url + urllist.get()
        print scan_url

if __name__ == '__main__':
    url = 'http://www.example.com/'
    path = './dir/test.txt'
    thread_num = 3
    urllist = loaddict(path)
    print 'Scan start!'
    for i in range(thread_num):
        test = th(url, urllist, i)
        test.start()
    test.join()
    print 'Scan done!'
