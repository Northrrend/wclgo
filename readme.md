upload wcllog to oss wcl-raw
sls pull log from oss to logstore wcl_raw
sls split log to wcl_split

trigger fc

fc get player list
fc get player class
fc get top paladin
fc generate mapping table
fc generate sls log deal script to oss


mannual start log deal task to wcl_ready

trigger fc
fc write wcl_ready to oss wcl-ready


