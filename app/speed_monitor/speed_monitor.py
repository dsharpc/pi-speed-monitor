"""speed_monitor.py
Functions to fetch the internet download and upload speed and ping
"""

import speedtest

def measure_speed():
    s = speedtest.Speedtest()
    s.download()
    s.upload()
    res = s.results.dict()
    return res