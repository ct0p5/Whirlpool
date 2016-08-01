#!/usr/bin/env python
# coding: utf-8

import argparse
import dirbrute
import config


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # parser.add_argument('-m', '--module', dest='scan_module', help='Choose scan module 1:brute 2:intale')
    parser.add_argument('-u', '--url', type=str, dest='scan_target', required=True, help='Website for scan, eg: http://www.wooyun.org | www.wooyun.org')
    # parser.add_argument('-f', '--file', dest='scan_file', help='Path of the urllist file')
    parser.add_argument('-t', '--thread', type=int, dest='scan_thread', default=config.thread_default, help='Scan thread, default is 20')
    # parser.add_argument('-o', '--output', dest='scan_output', help='Result of the whirlpool output')
    parser.add_argument('-s', '--status_code', dest='scan_status', default=config.code_default, help='1:Return urls of 200 status_code. 2:200+403  default is 1')
    # parser.add_argument('-c', '--file_choice', dest='scan_file_use', default=)
    parser.add_argument('--timeout', dest='scan_timeout', default=config.timeout_default, help='Set Timeout,default is 3')
    args = parser.parse_args()

    dirbrute.begin(args.scan_target, args.scan_thread, args.scan_status, args.scan_timeout)
