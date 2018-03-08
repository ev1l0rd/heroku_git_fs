from setuptools import setup

setup(name='heroku_git_fs',
      version='0.1dev',
      packages=['heroku_git_fs'],
      license='GNU GPLv3.0',
      install_requires=[
          'PythonGit',
      ],
      long_description=open('README.md').read())