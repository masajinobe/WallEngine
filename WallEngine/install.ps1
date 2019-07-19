function Get-ScriptDirectory
{
    $Invocation = (Get-Variable MyInvocation -Scope 1).Value
    Split-Path $Invocation.MyCommand.Path
}

$scriptdir = $(Get-ScriptDirectory)

$oldpath = [Environment]::GetEnvironmentVariable("PATH", "User")
$newpath = "$scriptdir\;$oldpath".Split(";")
$newpath = $newpath | Select-Object -uniq
$newpath = $newpath -join ";"
[Environment]::SetEnvironmentVariable("PATH", "$newpath", "User")