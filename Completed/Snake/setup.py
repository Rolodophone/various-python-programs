from cx_Freeze import setup, Executable

setup(name = 'Snake',
      version = '1.0',
      description = 'A recreation of the classic "Snake" arcade game with 2 player modes as well.',
      executables = [Executable('Snake.py')]
      )
