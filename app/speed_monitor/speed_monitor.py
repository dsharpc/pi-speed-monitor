"""speed_monitor.py
Functions to fetch the internet download and upload speed and ping
"""
from typing import Dict, Union
import speedtest

def measure_speed():
    s = speedtest.Speedtest()
    s.get_best_server()
    s.download()
    s.upload()
    res = s.results.dict()
    return res

def extract_relevant_data(data: Dict[str, Union[str, float]]) -> Dict[str, Union[str, float]]:
    RELEVANT_KEYS = ['timestamp', 'download', 'bytes_received', 'upload',
                     'bytes_sent', 'ping', 'server:url', 'server:name',
                     'server:country', 'server:sponsor', 'server:host',
                     'client:isp', 'client:isprating']
    out_dict = {}
    for key in RELEVANT_KEYS:
        if ':' not in key:
            out_dict[key] = data[key]
        else:
            key1, key2 = key.split(':')
            out_dict[f"{key1}_{key2}"] = data[key1][key2]
    return out_dict