# Prompt the user to enter a list of ports separated by commas
$ports = Read-Host "Enter a list of ports to block (e.g., 80,443,8080)"

# Split the input into an array of individual ports
$portArray = $ports -split ','

# Create a Windows Firewall rule for each port to block
foreach ($port in $portArray) {
    $ruleName = "Block Port $port"
    $portNumber = [int]$port

    # Check if a rule with the same name already exists
    if (-not (Get-NetFirewallRule -Name $ruleName -ErrorAction SilentlyContinue)) {
        New-NetFirewallRule -DisplayName $ruleName -Direction Inbound -Action Block -Protocol TCP -LocalPort $portNumber
        Write-Host "Port $port blocked."
    } else {
        Write-Host "Rule for Port $port already exists."
    }
}
