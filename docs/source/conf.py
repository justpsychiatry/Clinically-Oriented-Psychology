# Configuration file for the Sphinx documentation builder.

import os
import sys
sys.path.insert(0, os.path.abspath('.'))
#import sphinx_rtd_theme


# -- Project information -----------------------------------------------------

project = 'Clinically Oriented Psychology'
copyright = '2022'
author = 'Justpsychiatry'



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

html_theme = 'sphinx_book_theme'
html_static_path = ['_static']
html_title = "Clinically-Oriented Psychology"
html_baseurl ='https://psychology.mrcpsych.uk/'
bibtex_bibfiles = ['refs.bib']
bibtex_reference_style = 'author_year'
sitemap_filename = "psychsitemap.xml"
sitemap_url_scheme = "{link}"
hoverxref_auto_ref = True
html_css_files = ['rootcss.css']
autosectionlabel_prefix_document = True

hoverxref_roles = [
    'numref',
    'term',
    'abbr',
    'ref',
    'doc',
    'cite',
]


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

.. meta::
   :keywords: reStructuredText, demonstration, demo, parser
   :description lang=en: A demonstration of the reStructuredText
   :author: Justpsychiatry,
   :date: 

.. admonition:: Copyright Notice
 
   This work is (being) adapted from on OpenStax Psychology-2e which is licesed under creative commons 4.0 license. 
"""