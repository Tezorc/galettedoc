.. _developerguide:

.. only:: builder_html or readthedocs

   .. rst-class:: docs devel_doc

   :doc:`developer guide <index>`

.. rst-class:: doc_main_page

================
Developer manual
================

The Galette project is kindly hosted by `TuxFamily <https://www.tuxfamily.org>`_:

* `Galette website <https://galette.eu/dc/?navlang=en>`_,
* :doc:`a GIT repository to manage Galette source code <git>`,
* mailing lists,
* ...

There are also a few external services:

* `a bug tracker <https://bugs.galette.eu/projects/galette/>`_, to declare issues or to ask for evolutions,
* `a wonderfull :p documentation <https://doc.galette.eu>`_, you are currently reading,
* `a voting system <https://vote.galette.eu>`_, you can vote for features,
* `a Github organization <https://github.com/galette>`_, used to run unit tests or documentation on readthedocs, among others,
* `a continous integration system <https://travis-ci.org/galette/galette>`_, that runs a bunch of tests each time a commit is done on the github mirror.
* `a Telemetry application <https://telemetry.galette.eu>`_ which handles and displays Telemetry data received from volunteer Galette instances.

This documentation aims to help you understand the development rules of Galette, how the code is managed, ...

.. toctree::
   :maxdepth: 2

   git.rst
   contributor.rst
   codage.rst
   plugins.rst
   i18n.rst
   controllers.rst
   debug.rst
