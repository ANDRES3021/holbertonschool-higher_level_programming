#!/usr/bin/python3
"""Module convert from JSON to Python"""
import json


def from_json_string(my_str):
    """convert from JSON to Python"""
    return json.loads(my_str)
