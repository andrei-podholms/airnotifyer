#!/usr/bin/python3

import daemon
import argparse
import requests

def routine(args):
    pass

def get_args():
    parser = argparse.ArgumentParser(description='AIRMQ notification daemon.')
    parser.add_argument('--ip',
                        '-i',
                        type=str,
                        default='192.168.4.1',
                        required=True,
                        help='IP address of AIRMQ sensor')

    args = parser.parse_args()
    return args

def main():
    args = get_args()
    resp = requests.get('http://{}/json'.format(args.ip))
    data = resp.json()
    print("
    print('Hello world')

    #with daemon.DaemonContext():
    #    routine()

if __name__ == '__main__':
    main()

