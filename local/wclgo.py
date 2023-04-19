# -*- coding: utf-8 -*-
from wowclass import *
import pprint
import sys
import json
import time

file = 'WoWCombatLog-041323_103627.txt'
raid = 'tianqu.json'
new_file = 'WoWCombatLog-040123_124499.txt'

with open(raid, 'r', encoding='utf-8') as f:
    raid_dict = json.load(f)

def _fileflow(filename):

    with open(filename, 'r', encoding='utf-8') as ff:
        while True:
            yield ff.readline()

def _standerlize_log(line):

    l = line.split()
    ll = l[2].split(',')
    ll.insert(0, l[1])
    ll.insert(0, l[0])
    return ll

def _list_to_log(l):
    log = ''
    log += l[0]
    log += ' '
    log += l[1]
    log += '  '
    for i in range(2, len(l)-1):
        log += l[i]
        log += ','
    log += l[len(l)-1]
    log += '\n'
    return log

def _enumerate_count(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        for count, _ in enumerate(f, 1):
            pass
    return count


def list_player():

    player_dict = dict()
    ff = _fileflow(file)
    for line in ff:
        if len(line) == 0:
            continue
        line_list = _standerlize_log(line)
        for i in range(len(line_list)):
            if line_list[i].find('Player') == 0:
                if line_list[i+1].find('-逐風者') >= 0 :
                    if line_list[i] not in black_list:
                        if line_list[i] not in player_dict.keys():
                            player_dict[line_list[i]] = {'name': line_list[i+1]}
                            if len(player_dict.keys()) == 25:
                                break
        if len(player_dict.keys()) == 25:
            break
    return player_dict

def class_player(player_id):

    log_type = ['SPELL_CAST_START', 'SPELL_AURA_REFRESH', 'SPELL_AURA_REMOVED', 'SPELL_AURA_APPLIED']
    spell_list_fs = ['42897', '42891']
    spell_list_ms = ['48072', '25375', '48168']
    spell_list_ss = ['47809', '47811','47843']
    spell_list_dz = ['57970']
    spell_list_d = ['48465', '48451', '48441']
    spell_list_lr = ['49052', '34501']
    spell_list_sm = ['49271', '16280']
    spell_list_zs = ['47475', '12970', '12721']
    spell_list_qs= ['48782', '48785', '53742', '26017']
    spell_list_dk = ['51714', '55078']
    ff = _fileflow(file)
    for line in ff:
        if len(line) == 0:
            continue
        line_list = _standerlize_log(line)
        if line_list[2] in log_type :
            if line_list[3] == player_id:
                if line_list[11] in spell_list_fs:
                    return 'fs'
                if line_list[11] in spell_list_ms:
                    return 'ms'                
                if line_list[11] in spell_list_ss:
                    return 'ss' 
                if line_list[11] in spell_list_dz:
                    return 'dz'
                if line_list[11] in spell_list_d:
                    return 'd'
                if line_list[11] in spell_list_lr:
                    return 'lr'                
                if line_list[11] in spell_list_sm:
                    return 'sm'
                if line_list[11] in spell_list_zs:
                    return 'zs'  
                if line_list[11] in spell_list_qs:
                    return 'qs'
                if line_list[11] in spell_list_dk:
                    return 'dk'

def write_log(newfile):

    count = _enumerate_count(file)
    print(str(count))
    with open(newfile, mode='w', encoding='utf-8') as f:
        ff = _fileflow(file)
        c = 0
        for line in ff:
            c += 1
            if (c%5000) == 0:
                print('\r', end='')
                p = format(float(c)/float(count)*100, '.2f')
                print('write log progress: {}% '.format(p), end='')
                sys.stdout.flush()
            if len(line) == 0:
                break
            line_list = _standerlize_log(line)
            line_list[0] = '4/1'
            l = len(line_list)
            for i in range(2, l):
                if line_list[i].find('Player') == 0:
                    if line_list[i] in player_dict.keys():
                            id = line_list[i]
                            line_list[i] = player_dict[id]['new_id']
                            if (line_list[i+1].find('-逐風者') >= 0) | (line_list[i+1].find('未知目标') >= 0):
                                line_list[i+1] = player_dict[id]['new_name']                 
            new_line = _papadin_enhance(line_list, 'Player-5743-0026F9FD')
            f.write(_list_to_log(new_line))
    f.close()
                
def healer_check(player_id):

    h = 0
    oh = 0
    ff = _fileflow(new_file)
    for line in ff:
        if len(line) == 0:
            print(str(h-oh))
            print(format(float(oh)/float(h),'.2f'))
            break
        line_list = _standerlize_log(line)
        if line_list[2] == "SPELL_HEAL":
            if line_list[3] == player_id:
                if line_list[11] == '48782':
                    print(line_list[4] + ':' +  line_list[8] + ':' + line_list[30] + ':' + line_list[31] + ':' + line_list[32])
                    heal = int(line_list[31])
                    overheal = int(line_list[32])
                    h += heal
                    oh += overheal

def _papadin_enhance(line_list, player_id):

    if line_list[2] == "SPELL_HEAL":
            if line_list[3] == player_id:
                if line_list[11] == '48782':
                    #print(line_list[4] + ':' +  line_list[8] + ':' + line_list[31] + ':' + line_list[32])
                    heal = line_list[31]
                    new_heal = str(int(float(int(heal))*1.1))
                    line_list[31] = new_heal
                    line_list[30] = new_heal
    return line_list

black_list = []

player_dict = list_player()
pprint.pprint(player_dict) 

for id in player_dict.keys():
    print("try to class:" + player_dict[id]['name'] + '  | ' + id)
    player_dict[id]['class'] = class_player(id)
    print(player_dict[id]['class'])
pprint.pprint(player_dict) 

for id in player_dict.keys():
    if id == 'Player-5743-00000000':
        new_player = raid_dict['me']
        player_dict[id]['new_name'] = new_player['name'] + '-逐風者'
        player_dict[id]['new_id'] = new_player['player_id']
        pprint.pprint(player_dict[id]) 
        continue
    classes = player_dict[id]['class']
    new_player = raid_dict[classes][0]
    raid_dict[classes].pop(0)
    player_dict[id]['new_name'] = new_player['name'] + '-逐風者'
    player_dict[id]['new_id'] = new_player['player_id']
    pprint.pprint(player_dict[id]) 

write_log(new_file)






