#!/bin/bash

set -o nounset
set -o errexit

VERBOSE_MODE=0

function error_handler()
{
  local STATUS=${1:-1}
  [ ${VERBOSE_MODE} == 0 ] && exit ${STATUS}
  echo "Exits abnormally at line "`caller 0`
  exit ${STATUS}
}
trap "error_handler" ERR

PROGNAME=`basename ${BASH_SOURCE}`
DRY_RUN_MODE=0

function print_usage_and_exit()
{
  set +x
  local STATUS=$1
  echo "Usage: ${PROGNAME} [-v] [-v] [--dry-run] [-h] [--help]"
  echo ""
  echo " Options -"
  echo "  -v                 enables verbose mode 1"
  echo "  -v -v              enables verbose mode 2"
  echo "      --dry-run      show what would have been dumped"
  echo "  -h, --help         shows this help message"
  exit ${STATUS:-0}
}

function debug()
{
  if [ "$VERBOSE_MODE" != 0 ]; then
    echo $@
  fi
}

GETOPT=`getopt -o vh --long dry-run,help -n "${PROGNAME}" -- "$@"`
if [ $? != 0 ] ; then print_usage_and_exit 1; fi

eval set -- "${GETOPT}"

while true
do case "$1" in
     -v)            let VERBOSE_MODE+=1; shift;;
     --dry-run)     DRY_RUN_MODE=1; shift;;
     -h|--help)     print_usage_and_exit 0;;
     --)            shift; break;;
     *) echo "Internal error!"; exit 1;;
   esac
done

if (( VERBOSE_MODE > 1 )); then
  set -x
fi


# template area is ended.
# -----------------------------------------------------------------------------
if [ ${#} != 0 ]; then print_usage_and_exit 1; fi

# current dir of this script
CDIR=$(readlink -f $(dirname $(readlink -f ${BASH_SOURCE[0]})))
PDIR=$(readlink -f $(dirname $(readlink -f ${BASH_SOURCE[0]}))/..)

# -----------------------------------------------------------------------------
# functions


# end functions
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# main 

wapiti=${PDIR}/install/bin/wapiti
python=/usr/bin/python
perl=/usr/bin/perl

cp -rf ${CDIR}/train.txt ${CDIR}/crf.train
cp -rf ${CDIR}/dev.txt ${CDIR}/crf.dev
cp -rf ${CDIR}/test.txt ${CDIR}/crf.test

${wapiti} train --nthread 8 -c -d ${CDIR}/crf.dev -p ${CDIR}/crf.pattern ${CDIR}/crf.train ${CDIR}/crf.model

rm -rf ${CDIR}/crf.cqdb
${wapiti} label -m ${CDIR}/crf.model -q ${CDIR}/crf.cqdb -s ${CDIR}/crf.test ${CDIR}/crf.test.out
${python} ${CDIR}/conv2conll.py < ${CDIR}/crf.test.out > ${CDIR}/crf.test.out.conll
${perl}   ${CDIR}/conlleval.pl < ${CDIR}/crf.test.out.conll > ${CDIR}/crf.test.out.eval

# end main
# -----------------------------------------------------------------------------
