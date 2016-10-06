=========================
hep_ipython_tools package
=========================

.. automodule:: hep_ipython_tools
    :members:
    :undoc-members:
    :show-inheritance:


Example implementations
-----------------------

To help you with your first steps, there are two possible implementations and use-cases of the package
already included in the code. Feel free to copy and use them for your own HEP software stack.

The basic package only overloads the very basic classes you will need to use your own software with the package.
It does not include any new functionality except the one already in the main package itself, except a single additional
variable (called `another variable`) which can be steered from the outside and is passed to the calculation process.
The calculation process itself does not do anything useful - it is just there for you to play around with the package.

A bit more advanced is the simple package, which includes a (more or less) meaningful process, log output, collections
output and an additional viewer. Use this example if you have understood the main principles of the package and want to
have a template for your own HEP software.

.. toctree::
    :maxdepth: 1

    hep_ipython_tools.basic
    hep_ipython_tools.simple

Also included in the repository is a full-fledged running example on how the hep_ipython_tools package is used in the
Belle II analysis and software framework (basf2). You can have a look into the code and see how everything comes
together. However, if you are not part of the Belle II collaboration, you probably do not have the correct software
installed to use the package (this is why you will also not find any documentation here in the API docu).


hep_ipython_tools.calculation module
------------------------------------

.. automodule:: hep_ipython_tools.calculation
    :members:
    :undoc-members:
    :show-inheritance:

hep_ipython_tools.calculation_list module
-----------------------------------------

.. automodule:: hep_ipython_tools.calculation_list
    :members:
    :undoc-members:
    :show-inheritance:

hep_ipython_tools.calculation_process module
--------------------------------------------

.. automodule:: hep_ipython_tools.calculation_process
    :members:
    :undoc-members:
    :show-inheritance:

hep_ipython_tools.calculation_queue module
------------------------------------------

.. automodule:: hep_ipython_tools.calculation_queue
    :members:
    :undoc-members:
    :show-inheritance:

hep_ipython_tools.entities module
---------------------------------

.. automodule:: hep_ipython_tools.entities
    :members:
    :undoc-members:
    :show-inheritance:

hep_ipython_tools.information module
------------------------------------

.. automodule:: hep_ipython_tools.information
    :members:
    :undoc-members:
    :show-inheritance:

hep_ipython_tools.ipython_handler module
----------------------------------------

.. automodule:: hep_ipython_tools.ipython_handler
    :members:
    :undoc-members:
    :show-inheritance:

hep_ipython_tools.viewer module
-------------------------------

.. automodule:: hep_ipython_tools.viewer
    :members:
    :undoc-members:
    :show-inheritance: