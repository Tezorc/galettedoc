.. _installation:

.. rst-class:: docs install_doc

:doc:`manuel d'installation <index>`

.. rst-class:: doc_main_page

================================
Manuel d'installation de Galette
================================

L'installation de Galette consiste simplement, après avoir effectué quelques tâches préalables, à vous laisser guider par l'interface et renseigner les quelques informations qui vous seront demandées.

Dans un premier temps, vous allez `télécharger Galette <http://download.tuxfamily.org/galette/galette-0.9.tar.bz2>`_ et décompresser l'archive. Si vous êtes sous Linux, ça donnera quelque chose comme :

.. code-block:: bash

   $ cd /var/www/html/
   $ wget http://download.tuxfamily.org/galette/galette-0.9.tar.bz2
   $ tar xjvf galette-0.9.tar.bz2

Si vous êtes sous windows, vous devrez préalablement installer un logiciel capable de gérer les archives tar, comme le `logiciel libre 7zip <http://www.7-zip.org/>`_.

La version 0.9 de Galette est l'actuelle version stable. Il existe une archive mise à jour quotidiennement (`nightly <http://download.tuxfamily.org/galette/galette-dev.tar.bz2>`_) de la version de développement, et vous pouvez également choisir de  :doc:`récupérer la version de développement de Galette <../development/git>` comme expliqué dans la documentation de développement.

Pré-requis et hébergement
-------------------------

Pour installer Galette, vous aurez besoin que les composants suivants soient installés  :

* un serveur web Apache,
* PHP en version 5.6 ou supérieure (PHP 7.1 ou plus recommandé),

  * le module PHP `gd`,
  * le module PHP `PDO` `mysql` ou `postgresql`,
  * le module PHP `curl`,
  * le support SSL,
  * le module PHP `tidy` (optionnel, mais recommandé),
  * le module PHP `gettext` (optionnel).

* un serveur `MySQL <http://mysql.com>`_  en version  5.1 minimum ou `PostgreSQL <http://postgresql.org>`_ en version 9.1 minimum.

Sachez enfin que du côté des hébergeurs, si certains (que je ne nommerai pas :p) ne fournissent pas PHP 5.6 (loin s'en faut !) ; c'est désormais disponible sur la plupart des hébergement « professionnels » (`OVH <http://ovh.com>`_, etc.), et que des hébergeurs gratuits tels que `LegTux <http://legtux.org/>`_, `KegTux <http://www.kegtux.org/>`_, `Kind Hosting <http://www.kind-hosting.fr/>`_ (un grand bravo à eux :-)). Il reste aussi toujours la solution de l'auto-hébergement que je vous laisse la joie de découvrir ;-)

Galette ne fonctionne pas sur les hébergements suivants :

* Free (versions de PHP antédiluviennes),
* Olympe Networks (en raisons de limitations PHP trop importantes, et de plantages de l'application).

Galette est régulièrement testé avec des versions récentes de ces composants, si vous rencontrez des difficultés avec une version particulière, n'hésitez pas à nous le faire savoir ;-)

Table des matières
------------------

.. toctree::
   :maxdepth: 2

   preparation.rst
   galette.rst
   postinstall.rst
   update.rst


