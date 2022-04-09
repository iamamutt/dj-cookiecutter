"""`datajoint-workflow-neuro`:
_A DataJoint SciOps Workflow for Science Institute, Neuro Lab_
"""

import logging


def get_version() -> str:
    """_Get version number for the package `datajoint-workflow-neuro`._

    Returns:
        str: Version number taken from the installed package version or `version.py`.
    """
    from importlib.metadata import PackageNotFoundError, version  # pragma: no cover

    __version__: str = "unknown"

    try:
        # Replace `version(__name__)` if project does not equal the package name
        __version__ = version("datajoint-workflow-neuro")
    except PackageNotFoundError:  # pragma: no cover
        from .version import __version__
    finally:
        del version, PackageNotFoundError

    return __version__


__version__: str = get_version()
version: str = __version__


# Root level logger for the 'neurowf' namespace
logging.getLogger("neurowf").addHandler(logging.NullHandler())
