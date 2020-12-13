#
# voice-skill-sdk
#
# (C) 2020, YOUR_NAME (YOUR COMPANY), Deutsche Telekom AG
#
# This file is distributed under the terms of the MIT license.
# For details see the file LICENSE in the top directory.
#
#
from skill_sdk import skill, Response, tell
from state import setStep

import requests


@skill.intent_handler('TEAM_17_START')
def handler() -> Response:
    try:
        msg = setStep(0)
    except requests.exceptions.RequestException as err:
        msg = ''
    return tell(msg)
