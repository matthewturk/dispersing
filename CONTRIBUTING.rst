.. highlight:: shell

============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/matthewturk/dispersing/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix Bugs
~~~~~~~~

Look through the GitHub issues for bugs. Anything tagged with "bug"
and "help wanted" is open to whoever wants to implement it.

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the GitHub issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it.

Write Documentation
~~~~~~~~~~~~~~~~~~~

The Dispersing could always use more documentation, whether as part of the
official The Dispersing docs, in docstrings, or even on the web in blog posts,
articles, and such.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at https://github.com/matthewturk/dispersing/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

Get Started!
------------

Ready to contribute? Here's how to set up `dispersing` for local development. We
use `uv`_ for environment and dependency management.

1. Fork the `dispersing` repo on GitHub.
2. Clone your fork locally::

    $ git clone git@github.com:your_name_here/dispersing.git

3. Install `uv`_ (e.g. ``curl -LsSf https://astral.sh/uv/install.sh | sh``).
4. Create the environment and install the package (including the dev tools)::

    $ cd dispersing/
    $ uv sync --dev

   This creates a ``.venv`` and installs the Cython extension. The lockfile
   (``uv.lock``) pins the exact dependency set.

5. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

6. When you're done making changes, check that your changes pass ruff and the tests::

    $ uv run ruff check dispersing tests
    $ uv run pytest

   To run the tests on multiple Python versions, use ``uv run --python 3.11 pytest``
   (or simply rely on CI, which covers 3.10 through 3.13).

7. Commit your changes and push your branch to GitHub::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

8. Submit a pull request through the GitHub website.

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.rst.
3. The pull request should work for all supported Python versions (3.10 through
   3.13). Check
   https://github.com/matthewturk/dispersing/actions
   and make sure that the tests pass for all supported Python versions.

Tips
----

To run a subset of tests::


    $ uv run pytest tests/test_dispersing.py

To add or update dependencies, edit the ``dependencies`` (runtime) or
``dev`` group (tooling) in ``pyproject.toml``, then regenerate the lockfile::

    $ uv lock

.. _uv: https://docs.astral.sh/uv/
