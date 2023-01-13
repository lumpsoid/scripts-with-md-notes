Remove-Item C:\Users\mmgee\Dropbox\Obsidian\zettel_search.md
$zettelDict = @{}
$listOfFiles = (Get-ChildItem -File C:\Users\mmgee\Dropbox\Obsidian).FullName  # получить полное название файлов в папке
foreach($file in $listOfFiles)
{
    $fileBaseNames = [System.IO.Path]::GetFileNameWithoutExtension($file)
    $fileBaseNames -match '[0-9]+'  # добавить regex выбрать только id
    $fileBaseNames = $Matches.Values  # то что совпало
    $headerLine = [IO.File]::ReadLines($file, [text.encoding]::UTF8) | Select-Object -first 1  # прочитать первую строку файла и сохранить
    $headerLine = $headerLine -ireplace "^#\s", ""  # удалить хэштег в начале строки и пробел после него
    $zettelDict.Add( $fileBaseNames, $headerLine)  # добавить в словарь
}
#$zettelDict.GetEnumerator() | ForEach-Object {"{0} : {1}" -f $_.Name,$_.Value} | Add-Content C:\Users\mmgee\Dropbox\Obsidian\!zettel_search.md
#$zettelDict | out-string | add-content C:\Users\mmgee\Dropbox\Obsidian\!zettel_search.md
$zettelDict.keys | %{ Add-Content C:\Users\mmgee\Dropbox\Obsidian\zettel_search.md "$($zettelDict.$_) [[$_]]" -Encoding UTF8 }