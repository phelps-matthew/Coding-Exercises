import re

def getDeviceModel(data):
    u_max, m_max = 0, ""
    for d in data:
        m, u = d.split(",")
        if int(u) > u_max:
            u_max, m_max = int(u), m
    return m_max


data = ["iqttt,0077", "obvhd,0093", "flohd,0075"]
print(getDeviceModel(data))
