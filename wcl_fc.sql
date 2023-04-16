-- class player
SPELL_AURA_REFRESH
SPELL_DAMAGE
SPELL_PERIODIC_HEAL
SPELL_AURA_APPLIED
SPELL_AURA_REMOVED
SPELL_CAST_SUCCESS
SPELL_PERIODIC_DAMAGE
SPELL_PERIODIC_ENERGIZE
SWING_DAMAGE
SWING_DAMAGE_LANDED
SPELL_ENERGIZE
SPELL_HEAL

-- for fc
*| select distinct u02, u01 where type='SPELL_CAST_SUCCESS' and u01 like 'Player%'

*| select u09, u10, count(*) as nums where u01= 'Player-5743-0025111C' and type='SPELL_CAST_SUCCESS' group by u10, u09 order by nums desc limit 10

*| select u09, u10, u29, u30 where type in('SPELL_HEAL', 'SPELL_PERIODIC_HEAL') and u01='Player-5743-0026F9FD'

*| select u09, u10, sum(u29) as heal, sum(u30) as overheal where type in('SPELL_HEAL', 'SPELL_PERIODIC_HEAL') and u01='Player-5743-0026F9FD' group by u09, u10 order by heal desc 


-- for monitor
*| select distinct u02, u01 where type='SPELL_CAST_SUCCESS' and u01 like 'Player%'

*| select DISTINCT u02, u01 where u09=53563

*| select u09, u10, sum(u29) as heal, sum(u30) as overheal where type in('SPELL_HEAL', 'SPELL_PERIODIC_HEAL') and u01='Player-5743-0026F9FD' group by u09, u10 order by heal desc 

select DISTINCT u01 from log where u09=53563

select u02 as player, u01 as id, sum(u29) as heal, sum(u30) as overheal from log where u09 in(48782, 53652, 54968, 48785, 48821, 53653, 53654, 66922, 64891) group by u02, u01

*| select player, id, (heal-overheal) as h, (overheal/heal) as r from(select u02 as player, u01 as id, sum(u29) as heal, sum(u30) as overheal from log where u09 in(48782, 53652, 54968, 48785, 48821, 53653, 53654, 66922, 64891) group by u02, u01) order by h desc

*| select player, id, (cast(overheal as double)/cast(heal as double)) as r from(select u02 as player, u01 as id, sum(u29) as heal, sum(u30) as overheal from log where u09 in(48782, 53652, 54968, 48785, 48821, 53653, 53654, 66922, 64891) group by u02, u01) order by r 