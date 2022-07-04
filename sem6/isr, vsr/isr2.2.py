"""
    ИСР 2.2
    Разработать программу, позволяющую генерировать уникальные идентификаторы: UUID (universally unique identifier)
"""

import time
import os

def create_uuid():
    rand = os.urandom(16).hex()
    uuid = '-'.join([rand[0:8], rand[8:12], rand[12:20], rand[20:24], rand[24:32]])
    return uuid
    
if __name__ == '__main__':
    print(create_uuid())
