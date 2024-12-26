from enum import Enum


class Label(str, Enum):
    JUST_DO_IT = "just-do-it"
    STOP = "stop"


EXAMPLES = [
    {"text": "let's launch the project immediately and make progress", "label": Label.JUST_DO_IT},
    {"text": "we need to evaluate risks before proceeding", "label": Label.STOP},
    {"text": "take action now and seize the opportunity", "label": Label.JUST_DO_IT},
    {"text": "wait for additional data and review", "label": Label.STOP},
    {"text": "start building momentum and achieve goals", "label": Label.JUST_DO_IT},
    {"text": "careful consideration required at this stage", "label": Label.STOP},
    {"text": "move forward with implementation today", "label": Label.JUST_DO_IT},
    {"text": "postpone until we have more information", "label": Label.STOP},
    {"text": "begin execution of the plan immediately", "label": Label.JUST_DO_IT},
    {"text": "hold off and assess potential issues", "label": Label.STOP},
    {"text": "deploy the hotfix to production now to fix critical bug", "label": Label.JUST_DO_IT},
    {"text": "need more testing coverage before merging pull request", "label": Label.STOP},
    {"text": "market conditions are perfect lets launch the product", "label": Label.JUST_DO_IT},
    {"text": "review competitor analysis before pricing strategy change", "label": Label.STOP},
    {
        "text": "start the home renovation this weekend while materials are cheap",
        "label": Label.JUST_DO_IT,
    },
    {"text": "get multiple contractor quotes before bathroom remodel", "label": Label.STOP},
    {"text": "begin new workout routine today no excuses", "label": Label.JUST_DO_IT},
    {"text": "consult doctor before starting intense training program", "label": Label.STOP},
    {
        "text": "invest in emerging market opportunity with strong indicators",
        "label": Label.JUST_DO_IT,
    },
    {"text": "need to research market volatility before large investment", "label": Label.STOP},
]
