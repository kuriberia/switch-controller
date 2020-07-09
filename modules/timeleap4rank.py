#!/usr/bin/env python3
import argparse
import serial
import time
from time import sleep
import datetime

def send(ser, msg, duration=0, slp=0):
    now = datetime.datetime.now()
    print(f'[{now}] {msg}')
    ser.write(f'{msg}\r\n'.encode('utf-8'))
    sleep(duration)
    ser.write(b'RELEASE\r\n')
    sleep(slp)

def day4rank(ser):
    send(ser, 'Button HOME', 0.1, 0.5) # ホームに戻る
    send(ser, 'LY MAX',   0.05, 0.05)
    send(ser, 'LX MAX',   0.05, 0.05)
    send(ser, 'LX MAX',   0.05, 0.05)
    send(ser, 'LX MAX',   0.05, 0.05)
    send(ser, 'LX MAX',   0.05, 0.05)
    send(ser, 'Button A', 0.1, 0.2) # 設定を開く
    send(ser, 'LY MAX',   1.8, 0.1)
    send(ser, 'Button A', 0.1, 0.2) # 「本体」
    send(ser, 'LY MAX',   0.05, 0.05)
    send(ser, 'LY MAX',   0.05, 0.05)
    send(ser, 'LY MAX',   0.05, 0.05)
    send(ser, 'LY MAX',   0.05, 0.05)
    send(ser, 'Button A', 0.1, 0.2) # 「日付と時刻」
    send(ser, 'LY MAX',   0.05, 0.05)
    send(ser, 'LY MAX',   0.05, 0.05)
    send(ser, 'Button A', 0.1, 0.2) # 「現在の日付と時刻」
    send(ser, 'LX MAX',   0.05, 0.05)
    send(ser, 'LX MAX',   0.05, 0.05)
    send(ser, 'LY MIN',   0.05, 0.05) # 1日進める
    send(ser, 'LX MAX',   0.05, 0.05)
    send(ser, 'LX MAX',   0.05, 0.05)
    send(ser, 'LX MAX',   0.05, 0.05)
    send(ser, 'Button A', 0.1, 0.2) # OK

    send(ser, 'Button HOME', 0.1, 0.5)
    send(ser, 'Button HOME', 0.1, 0.5) # ゲームに戻る

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', default="/dev/ttyS7")
    args = parser.parse_args()
    ser = serial.Serial(args.port, 9600)
    try:
        print("Start")
        send(ser, 'Button B', 0.1, 0.5)
        cnt = 0
        while(cnt < 1):
            day4rank(ser)
            cnt += 1

    except KeyboardInterrupt:
        send(ser, 'RELEASE')
        print("Count :", cnt)
        print("End.")
        ser.close()
