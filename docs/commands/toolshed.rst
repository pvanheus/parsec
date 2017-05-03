toolshed
========

``get_repositories`` command
----------------------------

This section is auto-generated from the help text for the parsec command
``toolshed``.

**Usage**::

    parsec toolshed get_repositories [OPTIONS]

**Help**

Get the list of all installed Tool Shed repositories on this Galaxy instance.

**Options**::


      --help  Show this message and exit.
    

``install_repository_revision`` command
---------------------------------------

This section is auto-generated from the help text for the parsec command
``toolshed``.

**Usage**::

    parsec toolshed install_repository_revision [OPTIONS] TOOL_SHED_URL NAME

**Help**

Install a specified repository revision from a specified Tool Shed into this Galaxy instance. This example demonstrates installation of a repository that contains valid tools, loading them into a section of the Galaxy tool panel or creating a new tool panel section. You can choose if tool dependencies or repository dependencies should be installed through the Tool Shed, (use ``install_tool_dependencies`` or ``install_repository_dependencies``) or through a resolver that supports installing dependencies (use ``install_resolver_dependencies``). Note that any combination of the three dependency resolving variables is valid.

**Options**::


      --install_tool_dependencies     Whether or not to automatically handle tool
                                      dependencies (see http://wiki.galaxyproject.or
                                      g/AToolOrASuitePerRepository for more details)
      --install_repository_dependencies
                                      Whether or not to automatically handle
                                      repository dependencies (see http://wiki.galax
                                      yproject.org/DefiningRepositoryDependencies
                                      for more details)
      --install_resolver_dependencies
                                      Whether or not to automatically install
                                      resolver dependencies (e.g. conda). This
                                      parameter is silently ignored in Galaxy
                                      ``release_2016.04`` and earlier.
      --tool_panel_section_id TEXT    The ID of the Galaxy tool panel section where
                                      the tool should be insterted under. Note that
                                      you should specify either this parameter or
                                      the ``new_tool_panel_section_label``. If both
                                      are specified, this one will take precedence.
      --new_tool_panel_section_label TEXT
                                      The name of a Galaxy tool panel section that
                                      should be created and the repository installed
                                      into.
      --help                          Show this message and exit.
    

``show_repository`` command
---------------------------

This section is auto-generated from the help text for the parsec command
``toolshed``.

**Usage**::

    parsec toolshed show_repository [OPTIONS] TOOLSHED_ID

**Help**

Get details of a given Tool Shed repository as it is installed on this Galaxy instance.

**Options**::


      --help  Show this message and exit.
    