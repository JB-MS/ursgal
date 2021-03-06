#!/usr/bin/env python3

from distutils.core import setup
import distutils
from distutils.command.install_lib import install_lib
import os
import sys
from ursgal.version import ursgal_version

executable_list = [
    'makeblastdb',
    'tandem',
    'tandem.exe',
    'qvality',
    'percolator',
    'percolator_2_08',
    'omssacl',
    'myrimatch_2_1_138',
    'myrimatch.exe',
    'MSAmanda.exe',
    'PepNovo_bin',
    'novor.bat',
    'novor.sh',
    'PepNovo.exe',
]

if sys.platform in ['win32']:
    class my_install_lib(distutils.command.install_lib.install_lib):
        pass
else:
    class my_install_lib(distutils.command.install_lib.install_lib):
        def run(self):
            distutils.command.install_lib.install_lib.run(self)
            for fn in self.get_outputs():
                print('>>>>>>>>>>>>>>>>>>>', fn )
                if os.path.basename(fn) in executable_list:
                    # copied from distutils source - make the binaries executable
                    mode = ((os.stat(fn).st_mode) | 0o555) & 0o7777
                    distutils.log.info("changing mode of %s to %o", fn, mode)
                    os.chmod(fn, mode)


# # We store our version number in a simple text file:
# version_path = os.path.join(
#     os.path.dirname(__file__),
#     'ursgal', 'version.txt'
# )
# with open(version_path, 'r') as version_file:
#     ursgal_version = version_file.read().strip()


setup(
    name='ursgal',
    version = ursgal_version,
    packages = ['ursgal'],
    package_dir = {'ursgal': 'ursgal'},
    description='ursgal',
    package_data = {
        'ursgal' : [
            # 'version.txt',
            'wrappers/*.py',
            'resources/*/*/*',
            'resources/*/*/*/*',
            'resources/*/*/*/*/*',
        ]
    },
    requires = ['pymzml'],
    long_description = 'Universal Python module combining common bottom-up proteomics tools for large-scale analysis',
    author = 'Lukas P. M. Kremer, Purevdulam Oyunchimeg, Johannes Barth, Stefan Schulze and Christian Fufezan',
    author_email = 'christian@fufezan.net',
    url = 'http://ursgal.github.com',
    license = 'Lesser GNU General Public License (LGPL)',
    platforms = 'any that supports python 3.4',
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: SunOS/Solaris',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Chemistry',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',
        'Topic :: Scientific/Engineering :: Education',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    cmdclass= {'install_lib':my_install_lib }
)

