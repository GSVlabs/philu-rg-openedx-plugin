Change Log
##########

..
   All enhancements and patches to oex_plugin will be documented
   in this file.  It adheres to the structure of https://keepachangelog.com/ ,
   but in reStructuredText instead of Markdown (for ease of incorporation into
   Sphinx documentation and the PyPI description).

   This project adheres to Semantic Versioning (https://semver.org/).

.. There should always be an "Unreleased" section for changes pending release.

Unreleased
**********

Added
=====

* moved favicon-related changes `RGOeX-26060 <https://youtrack.raccoongang.com/issue/RGOeX-26060>`_

  * move RG-specific settings from the edx-platform `RGOeX-25959 <https://youtrack.raccoongang.com/issue/RGOeX-25959>`_

Changed
=======

* changed course visibility setting for the about page `RGOeX-26179 <https://youtrack.raccoongang.com/issue/RGOeX-26179>`_

Removed
=======

* revert POC commit 1db8682b `RGOeX-25959 <https://youtrack.raccoongang.com/issue/RGOeX-25959>`_

[0.1.0] - 2023-??-??
********************

Port from Nutmeg-RG
===================

* fix: main page course listing by Eugene Dyudyunov

  * should be swept out in Palm release if upstream PR
    `edx-platform #30954 <https://github.com/openedx/edx-platform/pull/30954>`_
    is merged.

Added
=====

* Start Project with cookiecutter-django-app
