from my_socket import emit

state = {
    'step': 0,
    'target': None
}

steps = {
    'salat': [
        'Gurke in Scheiben schneiden',
        'Tomaten in Scheiben schneiden',
        'Eier hinzufügen',
        'In einer Schüssel mischen',
        'Olivenöl hinzufügen und genießen!'
    ],
    'spaghetti': [
        'Die Nudeln 10 Minuten kochen lassen',
        'Tomatensauce hinzufügen',
        'Käse hinzufügen und genießen!',
    ]
}

indigirents = {
    'salat': 'Gurken, Tomaten, Eier, Feta Käse, Olivenöl',
    'spaghetti': 'Die Pasta, Tomatensauce, Der Käse',
}


def selectRecipe(target):
    state['step'] = None
    state['recipe'] = target
    emit('select', target)
    emit('select-step', None)

def setStep(step):
    state['step'] = step
    if state['recipe']:
        emit('select-step', step)
        return steps[state['recipe']][step]
    return ''

def nextStep():
    if state['recipe']:
        state['step'] = state['step'] + 1
        emit('select-step', state['step'])
        return steps[state['recipe']][state['step']]
    return ''

def currentStep():
    if state['recipe']:
        emit('select-step', state['step'])
        return steps[state['recipe']][state['step']]
    return ''

def getIngredients():
    if state['recipe']:
        return indigirents[state['recipe']]
    return ''