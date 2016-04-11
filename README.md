# hep-ipython-tools
[![Build Status](https://travis-ci.org/hep-ipython-tools/hep-ipython-tools.svg?branch=master)](https://travis-ci.org/hep-ipython-tools/hep-ipython-tools)
[![Coverage Status](https://coveralls.io/repos/github/hep-ipython-tools/hep-ipython-tools/badge.svg?branch=master)](https://coveralls.io/github/hep-ipython-tools/hep-ipython-tools?branch=master)

Package with reusable ipython tools and widgets typically used for HEP experiment code.

This package summerizes tools and widgets used for accessing the Belle2 software framework with ipython/jupyter. 
It can be reused for other experiments. To implement the functionality for your local software stack, overload the corresponding 
classes. For a simple example, see `simple`; for a more advanced setup see `ipython_handler_basf2`.

Setup with 

    git checkout https://github.com/hep-ipython-tools/hep-ipython-tools.git
    python setup.py install
  
or

    pip install git+https://github.com/hep-ipython-tools/hep-ipython-tools.git
