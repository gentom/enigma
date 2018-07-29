# enigma [![Build Status](https://travis-ci.org/gentom/enigma.svg?branch=master)](https://travis-ci.org/gentom/enigma) 
Enigma Machine in Python.

### Docker
```
# build image "enigma_image"
docker build -t enigma_image .

# run
docker run --name enigma_container -t -i enigma_image
```

### Result
```
Enigma Setup:
Cogs:  7 
Cog arrangement:
[11, 22, 1, 24, 8, 16, 17, 9, 20, 25, 12, 14, 21, 5, 19, 23, 10, 4, 2, 7, 0, 6, 18, 3, 15, 13]
[6, 9, 15, 19, 17, 7, 4, 10, 12, 0, 18, 5, 8, 24, 21, 20, 1, 16, 13, 23, 11, 25, 22, 3, 2, 14]
[1, 0, 22, 13, 20, 23, 12, 9, 24, 19, 6, 4, 16, 2, 10, 18, 7, 5, 11, 21, 17, 15, 3, 8, 25, 14]
[0, 14, 3, 20, 23, 8, 18, 1, 22, 12, 5, 11, 24, 2, 25, 10, 17, 13, 16, 7, 6, 21, 15, 9, 19, 4]
[15, 14, 8, 9, 5, 7, 16, 11, 24, 22, 4, 10, 6, 25, 2, 0, 18, 19, 12, 1, 23, 21, 17, 20, 3, 13]
[1, 3, 21, 25, 13, 14, 22, 15, 0, 16, 2, 11, 23, 5, 7, 19, 12, 20, 6, 10, 18, 8, 4, 9, 24, 17]
[17, 12, 8, 22, 21, 3, 10, 19, 7, 13, 23, 4, 9, 24, 18, 6, 2, 11, 16, 1, 5, 25, 14, 0, 20, 15]
Reflector arrangement:
 [14, 9, 6, 5, 22, 3, 2, 20, 11, 1, 18, 8, 19, 24, 0, 16, 15, 25, 10, 12, 7, 23, 4, 21, 13, 17] 

Plaintext:
The Enigma machines were a series of electro-mechanical rotor cipher machines developed and used in the early- to mid-20th century to protect commercial, 
diplomatic and military communication. Enigma was invented by the German engineer Arthur Scherbius at the end of World War I. 
Early models were used commercially from the early 1920s, and adopted by military and government services of several countries, 
most notably Nazi Germany before and during World War II. Several different Enigma models were produced, 
but the German military models, having a plugboard, were the most complex. Japanese and Italian models were also in use.

Encrypted text:
ntb mtoijo isnedaxk qzzo j paymzc ww vuqmvxz-gunxliwici csmai hesvyi blqshghp kbqgocqky btv yvxw ey gbr rvefa- fi kyj-20qq ymziqvj jm ipqaspm pbkykkipgs, fvodyyrgnwy zrf gmhqelcj amhtvlpmmcdts. dxyanb fxf zzwamslk vj zwb akwpvs wtoxaxma yjoptj rrnuxvzmd hk xls iqs lh jkfzw mza d. fnpubg gkjtrf cygy kexw qssjjvhffvil qudi afg ytuim 1920j, quu dejrukj ez ojdrmikm dtu acjuyjiody hoqkdhfq jy bfcjmqt fakfmmjzc, fphtx tinchxm medu eiwkhcf wgdqvg brj jdpmrs bbode krk hm. afcrhuq bdgqpqods iljfcx xmiqyz jzgj guvlxjut, irrd bmu zlhuzz yaujxmyk uplhmk, suqkei v dsxeqhcom, lbqc sfg upkb aysnvvr. kcrypfyy cmi zjopjys rktgqo cifq wjpr kl trh.

Plaintext:
the enigma machines were a series of electro-mechanical rotor cipher machines developed and used in the early- to mid-20th century to protect commercial, kdiplomatic and military communication. enigma was invented by the german engineer arthur scherbius at the end of world war i. kearly models were used commercially from the early 1920s, and adopted by military and government services of several countries, kmost notably nazi germany before and during world war ii. several different enigma models were produced, kbut the german military models, having a plugboard, were the most complex. japanese and italian models were also in use.
```