# Configuration file for the Sphinx documentation builder.

import os
import sys
from datetime import datetime
#import sphinx_rtd_theme

sys.path.insert(0, os.path.abspath('.'))




numfig = True

numfig_format = {'figure': 'Figure %s', 'table': 'Table %s',
                 'code-block': 'Listing %s', 'section': 'Section %s'}

numfig_secnum_depth = 1

# -- Project information -----------------------------------------------------

project = 'Clinically-Oriented Psychology'
author = 'Justpsychiatry'
copyright = "2021-{datetime.now().year}, {author}"


source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'restructuredtext',
    '.md': 'myst',
}


myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]
#release = 'latest'
#version = 'latest'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.todo',
    'sphinx_sitemap',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosectionlabel',
    'sphinxcontrib.bibtex',
    'sphinxcontrib.apa',
    "myst_parser",
    'sphinxcontrib.datatemplates',
    'sphinx_rtd_theme',
    "sphinx_design",
    'sphinx_search.extension',
    'hoverxref.extension',
]


templates_path = ['_templates']


# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output

html_theme = "furo"
html_static_path = ['_static']
html_title = "Clinically-Oriented Psychology"
html_logo = "jpsy.png"
html_baseurl ='https://psychology.mrcpsych.uk/'
bibtex_bibfiles = ['refs.bib']
bibtex_reference_style = 'author_year'
sitemap_filename = "psychsitemap.xml"
sitemap_url_scheme = "{link}"
hoverxref_auto_ref = True
html_css_files = ['rootcss.css']
autosectionlabel_prefix_document = True

html_theme_options = {

  "logo_only": True,
}

hoverxref_roles = [
    'numref',
    'term',
    'abbr',
    'ref',
    'doc',
    'cite',
]


html_use_opensearch = 'https://psychology.mrcpsych.uk/'

# -- Options for EPUB output
epub_show_urls = 'footnote'

# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.



rst_epilog= """

.. admonition:: Copyright Notice
   :class: caution
 
   This work is (being) adapted from on OpenStax Psychology 2e which is licensed under creative commons attribution 4.0 license. We license our work under a similar license.
   If you copy, adapt, remix or build up on work, you must give appropriate credit, provide a link to the license, and indicate if changes were made. 
   You may do so in any reasonable manner, 
   but not in any way that suggests the licensor endorses you or your use.
"""