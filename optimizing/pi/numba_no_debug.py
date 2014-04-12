"""Version 0.11.0 has debug turned on. Turn it off.
"""

import logging

import numba.codegen.debug

llvmlogger = logging.getLogger('numba.codegen.debug')
llvmlogger.setLevel(logging.INFO)