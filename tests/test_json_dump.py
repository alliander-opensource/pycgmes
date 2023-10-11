# SPDX-FileCopyrightText: 2023 Alliander
#
# SPDX-License-Identifier: Apache-2.0

import json

from pycgmes.resources.Bay import Bay
from pycgmes.utils.base import Base

descr = "A bay, but not at sea."


class TestJsonification:
    def test_round_robin_json_class_json(self):
        # initial_string=
        initial_json = json.loads(f'{{"__class__":"Bay", "description":"{descr}"}}')
        as_class = Base.parse_json_as(initial_json)
        final_json = as_class.to_dict()

        # Validates that the given parameters (initial_json) is in the dict of final class,
        # ignoring the other defaults params.
        # items() is actuallly a set view, and sets can be compared with <=. This line
        # thus means: make sure that initial_json is a subset of final_json.
        assert initial_json.items() <= final_json.items()

    def test_round_robin_class_json_class(self):
        initial_class = Bay(description=descr)
        as_json = initial_class.to_dict()
        final_class = Base.parse_json_as(as_json)

        # Pydantic rewrites the == to check dataclasses element.
        assert initial_class == final_class
