from cachecontrol.controller import logger
from skill_sdk import skill, Response, tell
from skill_sdk.l10n import _
from state import getIngredients

@skill.intent_handler('TEAM_17_INGREDIENTS')
def handler() -> Response:
    """ Find sense of life

    :return:        Response
    """
    try:
        msg = getIngredients()
    except:
        msg = ''
    return tell(msg)
