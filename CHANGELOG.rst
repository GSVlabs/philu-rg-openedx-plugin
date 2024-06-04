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

Fixed
=====
* Fix incorrect logo for bulk email `PhU-261 <https://youtrack.raccoongang.com/issue/PhU-261>`_

Added
=====
* Extend the Account-related fields `PhU-295 <https://youtrack.raccoongang.com/issue/PhU-295>`_
* Changes for the Welcome Form `PhU-231 <https://youtrack.raccoongang.com/issue/PhU-231>`_

[1.2.0] - 2024-03-13
********************

Added
=====
* Django 4 support [RGOeX-26348]

Fixed
=====

* Fix settings override for social media links in the email footer. Settings should be defined in the deployment instead `RGOeX-26461 <https://youtrack.raccoongang.com/issue/RGOeX-26461>`_
* MFEs' POST requests CSRF failures `RGOeX-26352 <https://youtrack.raccoongang.com/issue/RGOeX-26352>`_

Changed
=======

* Add the MR template (includes the DoR section) `OX-3406 https://youtrack.raccoongang.com/issue/OX-3406`_

[1.1.0] - 2023-11-06
********************

Changed
=======

* Allowed users to save social links with URL parameters `RGOeX-26082 <https://youtrack.raccoongang.com/issue/RGOeX-26082>`_

  * Changes should be reverted when changes are accepted in the upstream: https://github.com/openedx/edx-platform/pull/33565 (master), https://github.com/openedx/edx-platform/pull/33610 (Quince)
  * NOTE: we can't just drop the commit because it includes general refactoring that might be used in the future changes. But the final decision shold be made when rebasing.

* "Twitter.com" changed to "x.com" `RGOeX-26082 <https://youtrack.raccoongang.com/issue/RGOeX-26083>`_

  * Changes should be reverted when rebasing on Quince if upstream PR will be merged at the moment `quince#33613 <https://github.com/openedx/edx-platform/pull/33613>`_ is merged.
  * NOTE: we can't just drop the commit because it includes general refactoring that might be used in the future changes. But the final decision shold be made when rebasing.

Fixed
=====

* Add the user full name length validation for the registration form `RGOeX-26076 <https://youtrack.raccoongang.com/issue/RGOeX-26076>`_. This fixes 500 error when full name is longer than 255 characters.

  * Should be dropped when upstream PR (`master#33501 <https://github.com/openedx/edx-platform/pull/33501>`_, `quince#33615 <https://github.com/openedx/edx-platform/pull/33615>`_) will be merged

[1.0.0] - 2023-11-03
********************

Added
=====

* add the Edx Info Pages app `RGOeX-26048 <https://youtrack.raccoongang.com/issue/RGOeX-26048>`_

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
