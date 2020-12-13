#
# voice-skill-sdk
#
# (C) 2020, YOUR_NAME (YOUR COMPANY), Deutsche Telekom AG
#
# This file is distributed under the terms of the MIT license.
# For details see the file LICENSE in the top directory.
#
#
from cachecontrol.controller import logger
from skill_sdk import skill, Response, tell, context
from state import selectRecipe

def setStateAndGetText(target):
    if target.lower() == 'salat':
        selectRecipe(target.lower())
        return 'Salat ausgewählt'
    elif target.lower() == 'spaghetti':
        selectRecipe(target.lower())
        return 'Spaghetti ausgewählt';
    else:
        return 'nicht gefunden'

@skill.intent_handler('TEAM_17_SELECT')
def handler() -> Response:
    """ A very basic handler of SMALLTALK__GREETINGS intent,
        SMALLTALK__GREETINGS intent is activated when user says 'Hello'
        returns translated 'Hello' greeting

    :return:        Response
    """
    try:
        target = context.attributes['target'][0]
        response = tell(setStateAndGetText(target))
        # We return the response
        return response
    except:
        return tell('')
