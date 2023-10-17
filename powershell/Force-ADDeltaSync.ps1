# Import the Azure Active Directory Module if not already imported
Import-Module AzureAD

# Attempt to force a delta synchronization
try {
    Start-ADSyncSyncCycle -PolicyType Delta
    Write-Host "Delta synchronization initiated successfully."
} catch {
    Write-Host "An error occurred while attempting to force delta synchronization:"
    Write-Host $_.Exception.Message
}
