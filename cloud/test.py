# encoding: utf-8
from __future__ import print_function
import time
from datetime import datetime
from aliyun.log import *
import pprint


def main():

    endpoint = 'cn-beijing.log.aliyuncs.com'
    access_key_id = ''
    access_key = ''
    project_name = 'xjqtest'
    logstore_name = 'test9-1'

    #创建日志服务Client。
    client = LogClient(endpoint, access_key_id, access_key)

    starttime = '2023-04-01 00:00:00'
    at = time.strptime(starttime, "%Y-%m-%d %H:%M:%S")
    ts = int(time.mktime(at))

    def _sls_query(sql):
        #在指定的Logstore内执行SQL分析。
        res = client.execute_logstore_sql(project_name, logstore_name, ts, int(time.time()), sql, True)
        #打印计算结果的统计信息。
        #res.log_print()
        #处理的日志行数。
        #print("processed_rows: %s" % res.get_processed_rows())
        #SQL分析执行的时长。
        #print("elapsed_mills: %s" % res.get_elapsed_mills())
        #是否使用了SQL语句。
        #print("has_sql: %s" % res.get_has_sql())
        #竖线（|）前的WHERE语句。
        #print("where_query: %s" % res.get_where_query())
        #竖线（|）后的SELECT聚合计算语句。
        #print("agg_query: %s" % res.get_agg_query())
        #开启SQL独享版后，执行SQL分析所花费的CPU时间，单位为秒。SQL独享版按照CPU时间计费，更多信息，请参见计费项。
        #print("cpu_sec: %s" % res.get_cpu_sec())
        #开启SQL独享版后，执行SQL分析所使用的CPU核数。
        #print("cpu_cores: %s" % res.get_cpu_cores())
        body = res.get_body()
        return body

    def list_player():
        
        player_dict = dict()
        sql = "*| select distinct u02, u01 where type='SPELL_CAST_SUCCESS' and u01 like 'Player%'"
        res = _sls_query(sql)
        for player in res:
            player_dict[player['u01']] = {'name': player['u02']}
        return player_dict
    
    def class_player(player_id):
        spell_set_fs = {47610, 48108}
    
    def create_spell_map(player_id):
        spell_string = []
        sql = "*| select u09, u10, count(*) as nums where u01= 'Player-5743-0032D63A' and type='SPELL_CAST_SUCCESS' group by u10, u09 order by nums desc limit 15"
        res = _sls_query(sql)
        for spell in res:
            spell_string.append(spell['u09'])
        print(spell_string)


    #pd = list_player()
    #pprint.pprint(a)
    create_spell_map('Player-5743-0032D63A')
    

if __name__ == '__main__':
    main()