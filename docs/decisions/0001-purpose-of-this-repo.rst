0001 Purpose of This Repo
#########################

Status
******

**Draft**

.. TODO: When ready, update the status from Draft to Provisional or Accepted.

.. Standard statuses
    - **Draft** if the decision is newly proposed and in active discussion
    - **Provisional** if the decision is still preliminary and in experimental phase
    - **Accepted** *(date)* once it is agreed upon
    - **Superseded** *(date)* with a reference to its replacement if a later ADR changes or reverses the decision

    If an ADR has Draft status and the PR is under review, you can either use the intended final status (e.g. Provisional, Accepted, etc.), or you can clarify both the current and intended status using something like the following: "Draft (=> Provisional)". Either of these options is especially useful if the merged status is not intended to be Accepted.

Context
*******

Currently, RG OeX contains all required changes in the GitLab fork of the
upstream repository. The RG's are collected over the upstream named releases
branches. All customisations, fixes, enhancements, are proposed to the upstream,
but the pace they lands is pretty slow, so there are some changes that differ
RG OeX from vanilla.

The code hat has some pain consequences in the development process. The commit
history of RG's code hat is rewritten every time synchronization with the
upstream repository occurs. Sub-releases to the main RG OeX versions has the
same side-effect to the Delivery projects that are forked from the RG OeX
Products.

The goal is to make the layer of the RG customizations in RG OeX as thin as
possible.

.. This section describes the forces at play, including technological, political, social, and project local. These forces are probably in tension, and should be called out as such. The language in this section is value-neutral. It is simply describing facts.

Decision
********

To go ahead with the installable Open edX Plugin which is collects all (almost
all) RG refinements on permanent or temporary manner.

The functions, class methods and even classes could be overriden in OeX with
the help of `@pluggable_override` decorator (changes with decorating are required
to the RG OeX).

The classes used by the Open edX as Enum, dict like objects, can be overriden
only with the MonkeyPatching of the class object during the plugin
initialization.

`override_monkey` module will be used for that purpose.

.. This section describes our response to these forces. It is stated in full sentences, with active voice. "We will …"

Consequences
************

RG Products will maintaining two repositories to :

* edx-platform - override decorators and changes that cannot be moved to the
  plugin.
* rg-openedx-plugin - all (major) RG OeX refinements.

.. This section describes the resulting context, after applying the decision. All consequences should be listed here, not just the "positive" ones. A particular decision may have positive, negative, and neutral consequences, but all of them affect the team and project in the future.

Rejected Alternatives
*********************

Continue with the superstructure over the vanilla Open edX.

.. This section lists alternate options considered, described briefly, with pros and cons.

References
**********

TODO: If applicable, add any references. If not applicable, remove section.

.. (Optional) List any additional references here that would be useful to the future reader. See `Documenting Architecture Decisions`_ and `OEP-19 on ADRs`_ for further input.

.. _Documenting Architecture Decisions: https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions
.. _OEP-19 on ADRs: https://open-edx-proposals.readthedocs.io/en/latest/best-practices/oep-0019-bp-developer-documentation.html#adrs
