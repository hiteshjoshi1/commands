find a file with name pom.xml
find ./ -name pom.xml


replace a text in a file

example

replace Cash wth Trash in songs.txt and put the result in songs2.txt
sed 's/Cash/Trash/' songs.txt > songs2.txt


replace all occurrences of 1.1.0-Snapshot with 1.0.70-Snapshot
sed -i 's/1.1.0-SNAPSHOT/1.0.70-SNAPSHOT/' `find ./ -name pom.xml`


sed -i 's/1.0.76-SNAPSHOT/1.1.0-SNAPSHOT/' `find ./ -name pom.xml`


Finding Files BY Name-

find . -name somefile.txt
