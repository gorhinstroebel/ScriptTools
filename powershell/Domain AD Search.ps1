Import-Module ActiveDirectory

$domainController = "example.domain.com"  # Replace with the actual domain controller you want to target

Get-ADUser -Identity example.username" -Properties * -Server $domainController |
Select-Object AccountExpirationDate, AccountExpires, AccountLockoutTime, BadLogonCount, PadPwdCount, LastBadPasswordAttempt, LastLogonDate, LockedOut, PasswordExpired, PasswordLastSet, PwdLastSet |
Format-List
