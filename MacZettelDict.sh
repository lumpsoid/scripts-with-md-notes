search_dir=/Dropbox/Obsidian
for entry in "$search_dir"/*
do
  id=$entry | awk '[0-9]+{print0}'
  header=$(head -n 1 $entry)
  # ну и что то, чтобы запринтить в порядке "$header $id"
done
$zettelDict = @{}
$listOfFiles = (Get-ChildItem -File C:\Users\mmgee\Dropbox\Obsidian).FullName

foreach($file in $listOfFiles)
{
    $fileBaseNames = [System.IO.Path]::GetFileNameWithoutExtension($file)
    headerLine=$(head -n 1 filename) # заменено
    $zettelDict.Add( $fileBaseNames, $headerLine)
}
$zettelDict.GetEnumerator() | ForEach-Object {"{0} {1}" -f $_.Name,$_.Value} |
Add-Content C:\Users\mmgee\Dropbox\Obsidian\1111test.md