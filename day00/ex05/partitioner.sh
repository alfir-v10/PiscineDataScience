#!/bin/bash

if [ -z "$1" ]
then
    echo "invalid number of arguments"
else
{
    awk ' BEGIN { FS = "\",\"|T" }
        {
            if (NR == 1)
                START = $0
            else
            {
                if (!($2 in files))
                {
                    f = $2".csv"
                    files[$2]
                    print START > f
                }
                print >> f
            }
        }
        ' $1
}
fi