# Autoconf configuration for wapiti
#

AC_INIT([wapiti],[1.1.0],[https://github.com/dsindex],[wapiti])
PACKAGE=wapiti

AC_PREREQ(2.50)

AC_CONFIG_AUX_DIR([build])

AC_CANONICAL_TARGET

AM_INIT_AUTOMAKE([foreign])
AC_CONFIG_HEADERS([include/auto_config.h])

AC_PREFIX_DEFAULT(`pwd`/install)
AC_MSG_RESULT("prefix is $prefix.")

AC_ARG_ENABLE(debug,
   [  --enable-debug=val remove optimization option gcc, val=yes or no],
   [case "${enableval}" in
      yes) debug=true CFLAGS="-g";;
      no)  debug=false CFLAGS="-g -O2" ;;
      *) AC_MSG_ERROR(bad value ${enableval} for --enable-debug) ;;
    esac],[debug=false])
AM_CONDITIONAL(DEBUG,test x"$debug" = xtrue)


dnl ---------------------------------------------------------------------------
AH_TOP([#ifndef AUTO_CONFIG_H
#define AUTO_CONFIG_H 1
])

AH_BOTTOM([
#endif /* AUTO_CONFIG_H */
])

AH_VERBATIM([1_NEAR_TOP__],[
/* example */
#undef WAPITI_HOME
])

AC_DEFINE(WAPITI_HOME,`pwd`)

dnl ---------------------------------------------------------------------------
dnl Checks for programs
AC_PROG_CC
AC_PROG_INSTALL
AC_PROG_LIBTOOL


dnl should fail configure when followings headers does not exist.
AC_CHECK_HEADERS( \
	string.h stdlib.h stdio.h sys/types.h sys/stat.h fcntl.h \
    getopt.h \
)

AC_CHECK_FUNCS( \
	getopt \
	getopt_long \
)
WAPITI_RELEASE_DATE=`LANG=C date "+%a %b %d %T %Z %Y"`

AC_SUBST(PACKAGE)
AC_SUBST(WAPITI_RELEASE_DATE)

AC_SUBST(LIBTOOL)

AC_SUBST(AM_CFLAGS)
AC_SUBST(AM_CPPFLAGS)
AC_SUBST(AM_LDFLAGS)
AC_SUBST(AM_LIBTOOLFLAGS)

AC_CONFIG_FILES([
	Makefile
	src/Makefile
	include/Makefile
]) 

AC_OUTPUT


