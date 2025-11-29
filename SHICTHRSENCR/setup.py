from setuptools import setup, find_packages

setup(name='SHICTHRSENCR',
      version='1.3.0',
      description='SHICTHRS ENCR system',
      url='https://github.com/JNTMTMTM/SHICTHRS_ENCR',
      author='SHICTHRS',
      author_email='contact@shicthrs.com',
      license='GPL-3.0',
      packages=find_packages(),
      include_package_data=True,
      install_requires=['colorama==0.4.6'],
      zip_safe=False)
