# __init__.py
""" __init__.py """

try:
    from importlib import metadata
except ImportError:
    # Running on pre-3.8 Python; use importlib-metadata package
    import importlib_metadata as metadata

__all__ = ["__version__", "core"]
package_name = "bbtq"
__version__ = metadata.version(package_name)

from .core import (  # noqa
    main,
    filter_toml,
    BTQInvalidIndexException,
    BTQInvaildArrayFilterException,
    BTQInvalidKeyException,
)
