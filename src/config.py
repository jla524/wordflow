"""
Package wide configurations

Adapted from:
https://github.com/mattcoding4days/kickstart/blob/main/src/kickstart/
"""
from pathlib import Path
import sys
from threading import Lock
from typing import Any, Dict

from dotenv import dotenv_values


class ThreadSafeMeta(type):
    """
    This is a thread-safe implementation of Singleton.
    """
    _instances: Dict[Any, Any] = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        # Now, imagine that the program has just been launched. Since there's
        # no Singleton instance yet, multiple threads can simultaneously pass
        # the previous conditional and reach this point almost at the same
        # time. The first of them will acquire lock and will proceed further,
        # while the rest will wait here.
        with cls._lock:
            # The first thread to acquire the lock, reaches this conditional,
            # goes inside and creates the Singleton instance. Once it leaves
            # the lock block, a thread that might have been waiting for the
            # lock release may then enter this section. But since the Singleton
            # field is already initialized, the thread won't create a new
            # object.
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class Config(metaclass=ThreadSafeMeta):
    """
    @description: Global program configuration, uses the dotenv package
     to load runtime configuration from a .env file, once and
     only once into this object, this object can be used through-out
     the code base
    """
    try:
        __config: Dict[str, Any] = dotenv_values('.env')
        __version = '0.1.0'
        __package: str = __package__
        __base_dir = Path(__file__).resolve(strict=True).parent.parent
        __data_dir = __base_dir / 'data'
        __image_dir = __base_dir / 'image'
        __posts_file = __data_dir / 'posts.csv'
        __wordcloud_file = __image_dir / 'wordcloud.png'
    except KeyError as error:
        sys.stderr.write(f"Dotenv config error: {error} is missing\n")
        sys.exit(1)

    @classmethod
    def config(cls) -> Path:
        """
        @description: getter for config
        """
        return cls.__config

    @classmethod
    def version(cls) -> str:
        """
        @description: getter for version of package
        """
        return cls.__version

    @classmethod
    def package(cls) -> str:
        """
        @description: getter for package name
        """
        return cls.__package

    @classmethod
    def base_dir(cls) -> Path:
        """
        @description: getter for base directory
        """
        return cls.__base_dir

    @classmethod
    def data_dir(cls) -> Path:
        """
        @description: getter for data directory
        """
        return cls.__data_dir

    @classmethod
    def image_dir(cls) -> Path:
        """
        @description: getter for image directory
        """
        return cls.__image_dir

    @classmethod
    def posts_file(cls) -> Path:
        """
        @description: getter for posts file
        """
        return cls.__posts_file

    @classmethod
    def wordcloud_file(cls) -> Path:
        """
        @description: getter for wordcloud file
        """
        return cls.__wordcloud_file
