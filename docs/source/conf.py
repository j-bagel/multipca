import os
import sys
sys.path.insert(0, os.path.abspath('../../src'))

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'multipca'
copyright = '2024, Jialin Ouyang'
author = 'Jialin Ouyang'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',  # Automatically generate API documentation
    'sphinx.ext.napoleon',  # Support for NumPy and Google style docstrings
    'sphinx.ext.viewcode',  # Add links to highlighted source code
    'sphinx.ext.mathjax',   # Render math equations
    'sphinx_copybutton',    # Add copy button to code blocks
    'myst_parser',          # Support Markdown files
]

templates_path = ['_templates']
exclude_patterns = []

language = 'en'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Napoleon settings
napoleon_google_docstring = False
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = False
napoleon_use_admonition_for_examples = True
napoleon_use_admonition_for_notes = True
napoleon_use_admonition_for_references = True
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_type_aliases = None

# AutoDoc settings
autodoc_member_order = 'bysource'
autodoc_typehints = 'description'
autodoc_typehints_description_target = 'documented'

# MyST settings
myst_enable_extensions = [
    "dollarmath",      # Support for inline math using $ and $$
    "amsmath",         # Support for AMS math environments
    "colon_fence",     # Support for ::: fences
]
