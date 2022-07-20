"""
Configuration module
"""
from importlib import import_module

from dynaconf import FlaskDynaconf
from flask import Flask


def load_extensions(app: Flask):
    """
    Dynamicle load all extentions and plugns declared into EXTENTIONS array in settings.toml
    """
    for extension in app.config.EXTENSIONS:
        # Split data in form `extension.path:factory_function`
        module_name, factory = extension.split(":")
        # Dynamically import extension module.
        ext = import_module(module_name)
        # Invoke factory passing app.
        getattr(ext, factory)(app)


def init_app(app, **config):
    """
    Load configurations from settings.toml
    """
    FlaskDynaconf(app, **config)
