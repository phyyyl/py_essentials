#!/usr/bin/env python3
# -*- coding: utf-8 -*-#
import exceptions

def checkup():
    fails = ["json"]
    try:
        import json
    except:
        fails.append("json")

    try:
        import os
    except:
        fails.append("os")

    try:
        import platform
    except:
        fails.append("platform")

    try:
        import random
    except:
        fails.append("random")

    try:
        import sys
    except:
        fails.append("sys")

    try:
        import hashlib
    except:
        fails.append("hashlib")

    if len(fails) != 0:
        raise exceptions.ImportError(fails)