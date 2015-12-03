#!/usr/bin/env bash

# one bash liners to concat repeated page lists into a file
# sort the output file
# get repeated page list and also unique pagelist by page ids

outfile="allpage.lst"
sort=".sort"
for i in *.pagelist
do
    cat $i >> $outfile
done

sort -t $'\t' -k2 -n allpage.lst > $outfile$sort

cat allpage.lst.sort | awk -F '\t' '{print $2}' | sort | uniq -d > allpage.repeats
cat allpage.lst.sort | awk -F '\t' '{print $2}' | sort | uniq -c > allpage.uniq

# extract repeated pageid togher by its rule name to cross reference analysis of the page blocks
python rules_IDrepeats_map.py allpage.repeats allpage.lst.sort > allpage.repeats.map
python rules_IDrepeats_map.py allpage.uniq allpage.lst.sort > allpage.uniq.map
