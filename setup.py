# This script was automatically generated by distutils2
import os
from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.rst')) as f:
    README = f.read()

requires = [
    'docutils',
]

extras_require = {
    'test': [
        'tox',
    ]
}

setup(name='rst2textile',
      version='0.2.0',
      description='rst2textile is docutils textile writer convert reStructuredText(rst) to Textile format.',
      long_description=README,
      classifiers=[
          "Development Status :: 3 - Alpha",
          "Topic :: Utilities",
          "Environment :: Other Environment",
          "License :: OSI Approved :: Apache Software License",
          "Topic :: Documentation",
          "Topic :: Text Processing :: General",
          "Programming Language :: Python :: 2",
          "Programming Language :: Python :: 2.4",
          "Programming Language :: Python :: 2.5",
          "Programming Language :: Python :: 2.6",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.1",
          "Programming Language :: Python :: 3.2",
          "Programming Language :: Python :: 3.3",
      ],
      author='Takayuki SHIMIZUKAWA',
      author_email='shimizukawa@gmail.com',
      url='https://bitbucket.org/shimizukawa/rst2textile',
      keywords='docutils reStructuredText textile',
      packages=find_packages(),
      py_modules=['rst2textile'],
      scripts=['rst2textile.py'],
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      extras_require=extras_require,
)
