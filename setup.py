from setuptools import setup

setup(name='heroku_git_fs',
      version='0.4dev',
      packages=['heroku_git_fs'],
      license='GNU GPLv3.0',
      install_requires=[
          'GitPython',
      ],
      long_description=open('README.md').read())
