Write-Host Running PowerShell script to update tweets dataset . . .

# Get day of week; do not run if day of week is not Wednesday
$updateDay = "Wednesday"
$dayOfWeek = (Get-Date).DayOfWeek
if($dayOfWeek -ne $updateDay){
	Write-Host Today is $dayOfWeek. Dataset can only be updated on $updateDay.
	Write-Host Exiting . . .
}else{
	# Get date in variable for week number
	$fullDate = Get-Date
	Write-Host Date: $fullDate
	$currentDate = Get-Date -UFormat %d
	$weekNumber = $currentDate/7
	
	# Get month name in variable
	$monthNumber = Get-Date -UFormat %m
	$monthName = (Get-Culture).DateTimeFormat.GetMonthName($monthNumber)
	
	# Create directory if weekNumber==1
	$directoryName = $monthName
	if($weekNumber -eq 1){
		Write-Host Creating directory for $monthName . . .
		mkdir $directoryName
		Write-Host Directory for $monthName created.
	}else{
		Write-Host Directory for $monthName already exists.
	}
	
	# Run Python file for creating dataset with command line arguments
	Write-Host Running Python script to create dataset . . .
	$fileSuffix = $monthNumber + "-" + $weekNumber
	python update-dataset.py $directoryName $fileSuffix
	Write-Host Dataset updated!
	Write-Host Exiting . . .
}
