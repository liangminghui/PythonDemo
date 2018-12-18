#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#不是ps是process and system utilities
import psutil;
print("CPU逻辑数量:",psutil.cpu_count()) # CPU逻辑数量
print("CPU物理核心:",psutil.cpu_count(logical=False))# CPU物理核心
print("分区信息:",psutil.disk_partitions())
print("分区使用信息:",psutil.disk_usage("/"))
#其他案例用到再写到这里吧
