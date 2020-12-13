#
# voice-skill-sdk
#
# (C) 2020, YOUR_NAME (YOUR COMPANY), Deutsche Telekom AG
#
# This file is distributed under the terms of the MIT license.
# For details see the file LICENSE in the top directory.
#
#
from random import randint
from skill_sdk import skill, Response, ask, tell
from state import currentStep

#
# This implementation demonstrates a basic sample of "Guess Number" game:
#   user gives a number from 1 to 10 and we answer if we had it in mind :)
#

# The said number comes as a list of strings
# We'll use `intent_handler` decorator and type hints to convert it to integer value
@skill.intent_handler('TEAM_17_REPEAT')
def handler() -> Response:
    try:
        print('repeat')
        msg = currentStep()
        print(msg)
    except:
        msg = ''
    return tell(msg)
