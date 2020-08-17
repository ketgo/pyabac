"""
    File storage implementation
"""

import os
from typing import Union, Generator

from ..base import Storage
from ...policy import Policy


class FileStorage(Storage):
    """
        Stores and retrieves policies from files on disk.

        .. important::

            This storage does not yet perform ACID transactions. Do not
            use it in multi-threaded or multiprocess setting.

        :param storage_dir: path to directory where storage files
            are to be saved.
        :param cache_size: internal cache size to store indexes. Default
            set to 100 key-value pairs.
    """
    # Default target IDs
    DEFAULT_TARGET_IDS = ("*", "*", "*")

    # Policy index file name
    POLICY_INDEX_FILE = "index"

    # Target index file name
    TARGETS_INDEX_FILE = "target"

    # Policy storage file name
    POLICY_FILE = "policy"

    def __init__(self, storage_dir: str, cache_size=100):
        # Create path directory if not exists
        os.makedirs(storage_dir, exist_ok=True)
        self._storage_dir = storage_dir

    def add(self, policy: Policy):
        pass

    def get(self, uid: str) -> Union[Policy, None]:
        pass

    def get_all(self, limit: int, offset: int) -> Generator[Policy, None, None]:
        pass

    def get_for_target(
            self,
            subject_id: str,
            resource_id: str,
            action_id: str
    ) -> Generator[Policy, None, None]:
        pass

    def update(self, policy: Policy):
        pass

    def delete(self, uid: str):
        pass
