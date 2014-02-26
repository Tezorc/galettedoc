# -*- coding: utf-8 -*-
#
# Galette documentation build configuration file, created by
# sphinx-quickstart on Wed Jun 22 13:49:01 2011.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.todo']

todo_include_todos = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_styles/templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Galette'
author = u'Johan Cwiklinski'
copyright = u'2011-2019, Johan Cwiklinski'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '0.9.3'
# The full version, including alpha/beta/rc tags.
release = '0.9.3'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = 'fr'

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
today_fmt = '%d/%m/%Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'galette'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = ['_styles/templates']

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = '_styles/static/images/galette.png'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = 'favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_styles/static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%d/%m/%Y - %H:%M'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
html_domain_indices = False

# If false, no index is generated.
html_use_index = False

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'Galettedoc'


# -- Options for epub output --------------------------------------------

# The HTML theme for the epub output. Since the default themes are not
# optimized for small screen space, using the same theme for HTML and epub
# output is usually not wise. This defaults to 'epub', a theme designed to save
# visual space.
# epub_theme = 'epub'

# The description of the document. The default value is 'unknown'.
epub_description = 'Documentation de Galette'

# The language of the document. This is put in the Dublin Core metadata. The 
# default is the language option or 'en' if unset.
epub_language = 'fr'

# An identifier for the document. This is put in the Dublin Core metadata.
# For published documents this is the ISBN number, but you can also use an 
# alternative scheme, e.g. the project homepage. 
# The default value is 'unknown'.
epub_identifier = 'https://galette.eu'

# The publication scheme for the epub_identifier. This is put in the Dublin 
# Core metadata. For published books the scheme is 'ISBN'. If you use the 
# project homepage, 'URL' seems reasonable. The default value is 'unknown'.
epub_scheme = 'URL'

# The cover page information. This is a tuple containing the filenames of the
# cover image and the html template. The rendered html cover page is inserted
# as the first item in the spine in content.opf. If the template filename is
# empty, no html cover page is created. No cover at all is created if the tuple
# is empty.
epub_cover = ('_static/images/epub_cover.png', '')

# Control whether to display URL addresses. This is very useful for readers 
# that have no other means to display the linked URL. The settings can have the
# following values:
#    'inline' – display URLs inline in parentheses (default)
#    'footnote' – display URLs in footnotes
#    'no' – do not display URLs
# The display of inline URLs can be customized by adding CSS rules for the
# class link-target.
# epub_show_urls = 'no'

# A list of files that are generated/copied in the build directory but should 
# not be included in the epub file. The default value is [].
epub_exclude_files = [
  '_static/favicon.ico',
  'installation/unix.xhtml',
  'installation/ftp.xhtml',
  'installation/windows.xhtml',
]


# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
'papersize': 'a4paper',

# The font size ('10pt', '11pt' or '12pt').
'pointsize': '12pt',

# Font package inclusion.
'fontpkg': '\usepackage{newcent}',

# Additional stuff for the LaTeX preamble.
#'preamble': '',

# Maximum allowed nested levels in lists.
'maxlistdepth': '8',

# LaTeX-type customization interface.
'sphinxsetup': 'verbatimwithframe=false,VerbatimColor={rgb}{0.98,0.94,0.9},warningBorderColor={rgb}{0.84,0.23,0.24},warningBgColor={rgb}{0.87,0.68,0.69},noteBorderColor={rgb}{0.56,0.74,0.56},noteborder=3pt',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index', 'Galette.tex', u'Galette Documentation',
   u'Johan Cwiklinski', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = 'pdf_cover.pdf'

# A list of file names, relative to the configuration directory, to copy to the
# build directory when building LaTeX output. This is useful to copy files that 
# Sphinx doesn’t copy automatically, e.g. if they are referenced in custom
# LaTeX added in latex_elements. Image files that are referenced in source
# files (e.g. via .. image::) are copied automatically.
#
# You have to make sure yourself that the filenames don’t collide with those of
# any automatically copied files.
latex_additional_files = ['pdf_cover.pdf']

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
latex_show_pagerefs = True

# If true, show URL addresses after external links.
latex_show_urls = 'footnote' 

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'galette', u'Galette Documentation',
     [u'Johan Cwiklinski'], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False

# -- Options for PDF output --------------------------------------------------

#Grouping the document tree into PDF files. List of tuples
#(source start file, target name, title, author, options).
#If there is more than one author, separate them with \\.
#For example: r'Guido van Rossum\\Fred L. Drake, Jr., editor'
#The options element is a dictionary that lets you override
#this config per-document.
#For example,
#('index', u'MyProject', u'My Project', u'Author Name',
#dict(pdf_compressed = True))
#would mean that specific document would be compressed
#regardless of the global pdf_compressed setting.
pdf_documents = [
('index', u'galette', u'Documentation de Galette', u'Johan Cwiklinski'),
('usermanual/index', u'usermanual', u'Manuel Utilisateur de Galette', u'Johan Cwiklinski'),
('installation/index', u'installation', u'Installation de Galette', u'Johan Cwiklinski'),
('plugins/index', u'plugins', u'Plugins de Galette', u'Johan Cwiklinski'),
]

# A comma-separated list of custom stylesheets. Example:
pdf_stylesheets = ['sphinx','kerning','a4']

# Create a compressed PDF
# Use True/False or 1/0
# Example: compressed=True
pdf_compressed = True

# A colon-separated list of folders to search for fonts. Example:
# pdf_font_path = ['/usr/share/fonts', '/usr/share/texmf-dist/fonts/']

# Language to be used for hyphenation support
pdf_language = "fr_FR"

# Mode for literal blocks wider than the frame. Can be
# overflow, shrink or truncate
#pdf_fit_mode = "shrink"

# Section level that forces a break page.
# For example: 1 means top-level sections start in a new page
# 0 means disabled
pdf_break_level = 2

# When a section starts in a new page, force it to be 'even', 'odd',
# or just use 'any'
#pdf_breakside = 'any'

# Insert footnotes where they are defined instead of
# at the end.
#pdf_inline_footnotes = True

# verbosity level. 0 1 or 2
#pdf_verbosity = 0

# If false, no index is generated.
#pdf_use_index = True

# If false, no modindex is generated.
#pdf_use_modindex = False

# If false, no coverpage is generated.
#pdf_use_coverpage = True

# Name of the cover page template to use
#pdf_cover_template = 'sphinxcover.tmpl'
pdf_cover_template = '_styles/templates/galette_cover.tmpl'

# Documents to append as an appendix to all manuals.
#pdf_appendices = []

# Enable experimental feature to split table cells. Use it
# if you get "DelayedTable too big" errors
#pdf_splittables = False

# Set the default DPI for images
#pdf_default_dpi = 72

# Enable rst2pdf extension modules (default is empty list)
# you need vectorpdf for better sphinx's graphviz support
#pdf_extensions = ['vectorpdf']
pdf_extensions = ['dotted_toc']

# Page template name for "regular" pages
#pdf_page_template = 'cutePage'

locale_dirs = ["locale"]
gettext_uuid = True
gettext_compact = False
