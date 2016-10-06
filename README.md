# hep-ipython-tools
[![Build Status](https://travis-ci.org/hep-ipython-tools/hep-ipython-tools.svg?branch=master)](https://travis-ci.org/hep-ipython-tools/hep-ipython-tools)
[![Coverage Status](https://coveralls.io/repos/github/hep-ipython-tools/hep-ipython-tools/badge.svg?branch=master)](https://coveralls.io/github/hep-ipython-tools/hep-ipython-tools?branch=master)

Package with generic ipython tools and widgets typically to be used in HEP experiment code.

This package summerizes tools and widgets used for accessing/controlling you HEP software within your jupyter/ipython notebook. As an example, it is used for the Belle2 software framework (basf2; not included). 
However, the framework can be reused for other experiments. To implement the functionality for your local software stack, overload the corresponding 
classes. For a simple example, see `simple`; for a more advanced setup see `ipython_handler_basf2`.

Setup with 

    git checkout https://github.com/hep-ipython-tools/hep-ipython-tools.git
    python setup.py install
  
or

    pip install git+https://github.com/hep-ipython-tools/hep-ipython-tools.git
    
For more information, please have a look on [http://hep-ipython-tools.github.io/](http://hep-ipython-tools.github.io/).
