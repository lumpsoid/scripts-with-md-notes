#!/bin/bash

for file in *; do 
    if [ -f "$file" ]; then 
        fileBaseNames="$(basename -- $file)"
        [[ $fileBaseNames =~ [0-9]+ ]]
        if [[ ${BASH_REMATCH[0]} ]]; then
            match="${match:+$match }${BASH_REMATCH[0]}"
            read -r headerLine < $file
            echo $headerLine $fileBaseNames 
        fi
    fi 
done > zettel_search.md | iconv -t UTF-8