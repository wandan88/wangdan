#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later

"""Simple PySide6 launcher for qutebrowser.

Usage:
    python run.py [url ...]
    python run.py --qt-wrapper PySide6 [url ...]
"""

import sys
import os

# Ensure PySide6 is selected by default when launching via this script
os.environ.setdefault('QUTE_QT_WRAPPER', 'PySide6')

# Add project root to path so imports work when running directly
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from qutebrowser.qutebrowser import main

if __name__ == '__main__':
    sys.exit(main())
