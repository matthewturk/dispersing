.. highlight:: shell

============
Installation
============


Stable release
--------------

To install The Dispersing, run this command in your terminal:

.. code-block:: console

    $ pip install dispersing

This is the preferred method to install The Dispersing, as it will always install the most recent stable release.

If you don't have `pip`_ installed, this `Python installation guide`_ can guide
you through the process.

.. _pip: https://pip.pypa.io
.. _Python installation guide: http://docs.python-guide.org/en/latest/starting/installation/


From sources
------------

The sources for The Dispersing can be downloaded from the `Github repo`_.

You can either clone the public repository:

.. code-block:: console

    $ git clone https://github.com/matthewturk/dispersing

Or download the `tarball`_:

.. code-block:: console

    $ curl -OL https://github.com/matthewturk/dispersing/archive/refs/heads/main.tar.gz

Once you have a copy of the source, install the package with `uv`_ (or ``pip``).
This builds the Cython extension automatically:

.. code-block:: console

    $ cd dispersing
    $ uv sync --dev

For development, ``uv sync`` creates a virtualenv (``.venv``) with the package
installed in editable mode plus the development tools. Run the tests with
``uv run pytest`` and the linter with ``uv run ruff check .``.

.. _uv: https://docs.astral.sh/uv/

.. _Github repo: https://github.com/matthewturk/dispersing
.. _tarball: https://github.com/matthewturk/dispersing/tarball/main
