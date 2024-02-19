# FreqText
### This script does a frequency analysis with a encrypted text, it gives you details like the most repeated character, pair and trio

I did this bc sometimes I like to code things, also I was doing some challenges related to encryption, and wanted to code this, frequency analysis in cryptography is some analysis to see the most repeated letters, pairs and trios in a text with simple encryption, this helps you to know what may be the letter that is hidden, bc in every language exists letters, pairs and trios that are repeated constantly, for example in english one of the most repeated trios are "the", one of the most repeated couples are "th" and one of the most repeated letters are "t", if you know in a text encrypted with simple encryption the language and have the most used characters, you can get what the text originally said!

This script works well, the only failure is that with the trios you may have errors, for example if the script gives you 26 repetitions of one trio, that result might be incorrect and the real amount of repetitions are 27 repetitions, the script might be incorrect by 1 or 2 repetitions, but it only happens with the most frequent trios, with the pairs this script works well and also works well with the letters, by the way with the information this script gives you, you can already decrypt the text

<span>![</span><span>FreqText Banner</span><span>]</span><span>(</span><span>https://raw.githubusercontent.com/0therAnon/FreqText/main/banner.png</span><span>)</span>

```text
Usage ./freqtext.py <path_to_file> 
This script does a frequency analysis with encrypted texts
doing some analysis to the text to give you details like
the most repeated character, pair and trio in a file. The
options are these:

   -l      This option gives you details about the letters
   -p      This option gives you details about pairs
   -t      This option gives you details about trios
   -a      This option gives you all the details of the above options
   -x      Print the content of the file
   -h      This help message

Example usage:
./freqtext.py encrypted_file -a -x
```
