# Import the Active Directory module
Import-Module ActiveDirectory

# Define user information
$FirstName = "John"
$LastName = "Doe"
$UserName = "johnd"
$Password = "P@ssw0rd"  # Set the initial password
$OU = "OU=Users,DC=example,DC=com"  # Specify the Organizational Unit (OU) where you want to create the user
$EmailAddress = "johnd@example.com"
$SamAccountName = $UserName

# Create a new user
New-ADUser -Name "$FirstName $LastName" `
           -GivenName $FirstName `
           -Surname $LastName `
           -SamAccountName $SamAccountName `
           -UserPrincipalName "$UserName@example.com" `
           -DisplayName "$FirstName $LastName" `
           -Path $OU `
           -AccountPassword (ConvertTo-SecureString $Password -AsPlainText -Force) `
           -EmailAddress $EmailAddress `
           -Enabled $true
