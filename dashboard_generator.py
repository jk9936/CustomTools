#!/usr/bin/env python3
"""
Dashboard Generator Service
A Python console application that takes JSON data and generates HTML dashboards.
"""

import json
import argparse
import sys
import os
from datetime import datetime
from pathlib import Path
from jinja2 import Template
import webbrowser
from tools.dashboard import main

if __name__ == "__main__":
    main() 