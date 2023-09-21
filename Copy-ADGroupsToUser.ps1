# Import the Active Directory module
Import-Module ActiveDirectory

# Define the source and target usernames
$sourceUsername = "source.user"
$targetUsername = "target.user"

# Specify the target domain controller
$domainController = "example.domain.com"  # Replace with the actual domain controller you want to target

# Get the user objects for the source and target users
$sourceUser = Get-ADUser -Identity $sourceUsername -Server $domainController -Properties MemberOf
$targetUser = Get-ADUser -Identity $targetUsername -Server $domainController -Properties MemberOf

if ($sourceUser -eq $null) {
    Write-Host "Source user $sourceUsername not found."
} elseif ($targetUser -eq $null) {
    Write-Host "Target user $targetUsername not found."
} else {
    # Copy group memberships from source to target user
    $sourceUser.MemberOf | ForEach-Object {
        $group = Get-ADGroup $_ -Server $domainController
        if ($group -ne $null) {
            Add-ADGroupMember -Identity $group -Members $targetUser -Server $domainController
            Write-Host "Added $targetUsername to group: $($group.Name)"
        } else {
            Write-Host "Group not found: $_"
        }
    }

    Write-Host "Group memberships copied from $sourceUsername to $targetUsername."
}
