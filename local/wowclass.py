

def check_fs(ll, player):
    spell_list = ['42897', '42891']
    if ll[2] == 'SPELL_CAST_START':
        if ll[3] == player:
            if ll[11] in spell_list:
                return True
    return False

def check_d(ll, player):
    if ll[2] == 'SPELL_CAST_START':
        if ll[3] == player:
            if ll[11] == '42897':
                return True
            if ll[11] == '42891':
                return True
    return False