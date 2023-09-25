# SPDX-FileCopyrightText: 2023 Alliander
#
# SPDX-License-Identifier: Apache-2.0


class DataclassConfig:  # pylint: disable=too-few-public-methods
    """
    Used to configure pydantic dataclasses.

    See doc at
    https://docs.pydantic.dev/latest/usage/model_config/#options
    """

    # By default, with pydantic extra arguments given to a dataclass are silently ignored.
    # This matches the default behaviour by failing noisily.
    extra = "forbid"
