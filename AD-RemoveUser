Import-Module ActiveDirectory

$domainController = "example.domain.com"  # Replace with the actual domain controller you want to target
$username = "example.username"  # Replace with the username of the user you want to delete

# Check if the user exists
$user = Get-ADUser -Identity $username -Server $domainController -ErrorAction SilentlyContinue

if ($user -ne $null) {
    # Remove the user
    Remove-ADUser -Identity $user -Server $domainController -Confirm:$false
    Write-Host "User $username has been deleted."
} else {
    Write-Host "User $username does not exist."
}
