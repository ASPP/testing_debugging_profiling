from Cython.Build import cythonize
import numpy
from setuptools import setup, find_packages
from setuptools.extension import Extension


extensions = [
    Extension(
        'noiser.utils',
        ["noiser/utils.pyx"],
        include_dirs=[numpy.get_include()],
    )
]


setup(
    name='Noiser',
    version='1.0',
    packages=find_packages(),
    ext_modules=cythonize(extensions),
    entry_points={
        'console_scripts': [
            'baboon=noiser.main:main',
        ]
    },
    package_data={
        'noiser': ['images/*.png'],
    }
)
