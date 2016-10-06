from setuptools import setup

setup(name='hep_ipython_tools',
      version='1.0',
      packages=['hep_ipython_tools',
                "hep_ipython_tools.simple",
                "hep_ipython_tools.ipython_handler_basf2",
                "hep_ipython_tools.basic"],
      tests_require=['pytest', "pytest-cov", "mock"],
      setup_requires=['pytest-runner'],
      install_requires=['funcsigs'],
      )
