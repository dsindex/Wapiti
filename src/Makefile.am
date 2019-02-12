
INCLUDES  =
OSX_LDFLAGS = -Wl,-undefined -Wl,dynamic_lookup

STD=gnu99
OPTS = #-DDEBUG

lib_LTLIBRARIES = libwapiti.la libwapiti_static.la

libwapiti_la_SOURCES = api.c  bcd.c  decoder.c  gradient.c  lbfgs.c  model.c  options.c  pattern.c  progress.c  quark.c  reader.c  rprop.c  sgdl1.c  thread.c  tools.c  vmath.c cqdb.c lookup3.c
libwapiti_la_LDFLAGS = -avoid-version -no-undefined
libwapiti_la_CFLAGS = -g -Wall -std=${STD} -Wextra -fPIC ${OPTS}

libwapiti_static_la_SOURCES = api.c  bcd.c  decoder.c  gradient.c  lbfgs.c  model.c  options.c  pattern.c  progress.c  quark.c  reader.c  rprop.c  sgdl1.c  thread.c  tools.c  vmath.c cqdb.c lookup3.c
libwapiti_static_la_LDFLAGS = -static -avoid-version -no-undefined
libwapiti_static_la_CFLAGS = -g -Wall -std=${STD} -Wextra -fPIC ${OPTS}

bin_PROGRAMS = wapiti test_api build_cqdb search_cqdb

wapiti_SOURCES    = wapiti.c
wapiti_LDFLAGS    = -static -avoid-version -no-undefined
wapiti_LDADD      = libwapiti.la -lm -lpthread
wapiti_CFLAGS     = -g -Wall -std=${STD} -Wextra -fPIC ${OPTS}

test_api_SOURCES  = test_api.c
test_api_LDFLAGS  = -static -avoid-version -no-undefined
test_api_LDADD    = -lwapiti -lm -lpthread
test_api_CFLAGS   = -g -Wall -std=${STD} -Wextra -fPIC ${OPTS}

build_cqdb_SOURCES  = build_cqdb.c
build_cqdb_LDFLAGS  = -static -avoid-version -no-undefined
build_cqdb_LDADD    = -lwapiti -lm -lpthread
build_cqdb_CFLAGS   = -g -Wall -std=${STD} -Wextra -fPIC ${opts}

search_cqdb_SOURCES  = search_cqdb.c
search_cqdb_LDFLAGS  = -static -avoid-version -no-undefined
search_cqdb_LDADD    = -lwapiti -lm -lpthread
search_cqdb_CFLAGS   = -g -Wall -std=${STD} -Wextra -fPIC ${opts}

