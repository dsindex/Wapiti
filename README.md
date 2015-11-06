wapiti
===

- Description
  - CRF tool Wapiti alternative
    - [Wapiti](https://github.com/Jekub/Wapiti)
    - [Wapiti python wrapper](https://github.com/adsva/python-wapiti)
    - [CQDB](https://github.com/ninjin/cqdb)
  - combine above sources for convenience

- Modification
  - add functions to cqdb.c, cqdb.h
  ```
  int  open_cqdb(char* db_path, FILE** fp, cqdb_writer_t** dbw);
  void close_cqdb(FILE* fp, cqdb_writer_t* dbw);
  int  load_cqdb(char* db_path, char** block, cqdb_t** db);
  int  unload_cqdb(char* block, cqdb_t* db);
  ```
  - add test programs build_cqdb.c, search_cqdb.c
  - use CQDB for fast lookup feature to id
    - labeling mode only
    - modify quark.c, quark.h, model.c, reader.c, reader.h, options.h, options.c
  - remove fatal() in pat_exec()

- Installation
```
- version of aclocal, automake, libtoolize, autoheader, autoconf 
  aclocal (GNU automake) 1.11.1
  automake (GNU automake) 1.11.1
  libtoolize (GNU libtool) 2.2.6b 
  autoheader (GNU Autoconf) 2.63
  autoconf (GNU Autoconf) 2.63
- command
  ./builfconf
  ./configure
  make
  make install
```

- Usage
```
[train]
./wapiti train -p ../data/nppattern.txt ../data/nptrain.txt npmodel

[label] - file
./wapiti label -m npmodel -s ../data/nptest.txt nptest.txt.out

[label] - file, using cqdb
rm -rf npmodel.cqdb
./wapiti label -m npmodel -q npmodel.cqdb -s ../data/nptest.txt nptest.txt.out
* be careful
  if npmodel.cqdb not exists, create npmodel.cqdb.
  if npmodel.cqdb exists, load npmodel.cqdb.
  therefore, 'rm -rf npmodel.cqdb' first for sync npmodel with npmodel.cqdb

[label] - line
./test_api npmodel < test.txt

Confidence NN B	B	2.154
in IN O	O	4.383
the DT B	B	6.857
pound NN I	I	6.401
is VBZ O	O	5.749
widely RB O	O	4.075
expected VBN O	O	5.823
to TO O	O	5.354
take VB O	O	4.769
another DT B	B	3.915
sharp JJ I	I	5.207
dive NN I	I	4.537
if IN O	O	6.485
trade NN B	B	5.647
figures NNS I	I	3.444
for IN O	O	5.886
September NNP B	B	6.540
, , O	O	3.573
due JJ O	O	4.372
for IN O	O	5.148
release NN B	B	5.449
tomorrow NN B	I	3.280
, , O	O	6.205
fail VB O	O	3.811
to TO O	O	4.987
show VB O	O	4.286
a DT B	B	4.584
substantial JJ I	I	7.425
improvement NN I	I	5.843
from IN O	O	7.715
July NNP B	B	4.780
and CC I	O	3.766
August NNP I	B	5.370
's POS B	B	1.334            # ', comment
near-record JJ I	I	4.467
deficits NNS I	I	6.043
. . O	O	7.700

```

- Pattern description
```
U:wrd-2 L=%X[-1,0]/%X[ 0,0]
=> u,U      : unigram feature
   b,B      : bigram  feature
   *        : unigram and bigram feature
=> name     : 'wrd-2 L'
=> template : %X[-1,0]/%X[0,0]
              (previous position, first column + current position first column)
=> %x,%X    : use token string itself as feature
   %t       : test regular expression. if matched, set true or false
   %m       : match regular expression. if matched, use first match as feature

ex) nppattern.txt
*

U:Wrd-1 X=%x[ 0,0]

U:wrd-1LL=%X[-2,0]
U:wrd-1 L=%X[-1,0]
U:wrd-1 X=%X[ 0,0]
U:wrd-1 R=%X[ 1,0]
U:wrd-1RR=%X[ 2,0]

U:wrd-2 L=%X[-1,0]/%X[ 0,0]
U:wrd-2 R=%X[ 0,0]/%X[ 1,0]

*:Pos-1LL=%x[-2,1]
*:Pos-1 L=%x[-1,1]
*:Pos-1 X=%x[ 0,1]
*:Pos-1 R=%x[ 1,1]
*:Pos-1RR=%x[ 2,1]

U:Pos-2 L=%X[-1,1]/%X[ 0,1]
U:Pos-2 R=%X[ 0,1]/%X[ 1,1]

*:Pre-1 X=%m[ 0,0,"^.?"]
*:Pre-2 X=%m[ 0,0,"^.?.?"]
*:Pre-3 X=%m[ 0,0,"^.?.?.?"]
*:Pre-4 X=%m[ 0,0,"^.?.?.?.?"]

*:Suf-1 X=%m[ 0,0,".?$"]
*:Suf-2 X=%m[ 0,0,".?.?$"]
*:Suf-3 X=%m[ 0,0,".?.?.?$"]
*:Suf-4 X=%m[ 0,0,".?.?.?.?$"]

*:Caps? L=%t[-1,0,"\u"]
*:Caps? X=%t[ 0,0,"\u"]
*:Caps? R=%t[ 1,0,"\u"]

*:AllC? X=%t[ 0,0,"^\u*$"]
*:BegC? X=%t[ 0,0,"^\u"]

*:Punc? L=%t[-1,0,"\p"]
*:Punc? X=%t[ 0,0,"\p"]
*:Punc? R=%t[ 1,0,"\p"]

*:AllP? X=%t[ 0,0,"^\p*$"]
*:InsP? X=%t[ 0,0,".\p."]

*:Numb? L=%t[-1,0,"\d"]
*:Numb? X=%t[ 0,0,"\d"]
*:Numb? R=%t[ 1,0,"\d"]

*:AllN? X=%t[ 0,0,"^\d*$"]
```

- About CQDB
```
- string to int(0 ~ (2^31)-1), int to string

- build db
$ wc -l query.txt
11278376 query.txt

$ ./build_cqdb query.db < query.txt
elapsed time = 4.264002 sec
246M 2015-11-05 12:57 query.txt
547M 2015-11-05 13:00 query.db

- search db
$ ./search_cqdb query.db < query.txt > t
elapsed time = 8.970917 sec
$ wc -l t
11278376 t
```
