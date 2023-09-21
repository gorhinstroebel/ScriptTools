Import-Module ActiveDirectory

get-aduser -identity example.username -properties * | 
select accountexpirationdate, accountexpires, accountlockouttime, 
badlogoncount, padpwdcount, lastbadpasswordattempt, lastlogondate, 
lockedout, passwordexpired, passwordlastset, pwdlastset | format-list
