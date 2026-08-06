#!/usr/bin/env python
"""Build configuration for the Cython extension.

All package metadata lives in ``pyproject.toml``; this file exists only
because the extension requires ``numpy``'s include directory, which cannot
be expressed statically in ``pyproject.toml``.
"""

import numpy as np
from Cython.Build import cythonize
from setuptools import setup
from setuptools.extension import Extension

ext_modules = [
    Extension(
        "dispersing.fast_utilities",
        ["dispersing/fast_utilities.pyx"],
        include_dirs=[np.get_include()],
        define_macros=[("NPY_NO_DEPRECATED_API", "NPY_1_7_API_VERSION")],
    ),
]

setup(ext_modules=cythonize(ext_modules, compiler_directives={"language_level": 3}))
