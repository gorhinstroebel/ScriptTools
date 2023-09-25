# Define the target host and range of ports to scan
$targetHost = "example.com"
$portsToScan = 1..1024  # You can adjust this range as needed

# Loop through the specified ports and test each one
foreach ($port in $portsToScan) {
    $result = Test-NetConnection -ComputerName $targetHost -Port $port
    
    # Check if the port is open
    if ($result.TcpTestSucceeded) {
        Write-Host "Port $port is open"
    }
    else {
        Write-Host "Port $port is closed"
    }
}
