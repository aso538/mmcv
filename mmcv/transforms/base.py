# Copyright (c) OpenMMLab. All rights reserved.
from abc import ABCMeta, abstractmethod
from typing import Dict, List, Optional, Tuple, Union


class BaseTransform(metaclass=ABCMeta):
    """Base class for all transformations."""

    def __call__(self,
                 results: Dict, reverse: bool = False) -> Optional[Union[Dict, Tuple[List, List]]]:
        if reverse:
            return self.reverse(results)
        return self.transform(results)

    @abstractmethod
    def transform(self,
                  results: Dict) -> Optional[Union[Dict, Tuple[List, List]]]:
        """The transform function. All subclass of BaseTransform should
        override this method.

        This function takes the result dict as the input, and can add new
        items to the dict or modify existing items in the dict. And the result
        dict will be returned in the end, which allows to concate multiple
        transforms into a pipeline.

        Args:
            results (dict): The result dict.

        Returns:
            dict: The result dict.
        """

    def reverse(self, results: Dict) -> Optional[Union[Dict, Tuple[List, List]]]:
        """The reverse function. All subclasses of BaseTransform that require
        reverse should override this method.

        Args:
            results (dict): The result dict.

        Returns:
            dict: The result dict.
        """
        return results
