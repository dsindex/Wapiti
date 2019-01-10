#!/bin/bash

set -o nounset
set -o errexit
function readlink()
{
    TARGET_FILE=$2
    cd `dirname $TARGET_FILE`
    TARGET_FILE=`basename $TARGET_FILE`

    # Iterate down a (possible) chain of symlinks
    while [ -L "$TARGET_FILE" ]
    do
        TARGET_FILE=`readlink $TARGET_FILE`
        cd `dirname $TARGET_FILE`
        TARGET_FILE=`basename $TARGET_FILE`
    done

    # Compute the canonicalized name by finding the physical path
    # for the directory we're in and appending the target file.
    PHYS_DIR=`pwd -P`
    RESULT=$PHYS_DIR/$TARGET_FILE
    echo $RESULT
}
export -f readlink

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

GETOPT=`getopt vh $*`
if [ $? != 0 ] ; then print_usage_and_exit 1; fi

eval set -- "${GETOPT}"

while true
do case "$1" in
     -v)            let VERBOSE_MODE+=1; shift;;
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
python='env python'
perl='env perl'

cp -rf ${CDIR}/train.txt ${CDIR}/crf.train
cp -rf ${CDIR}/dev.txt ${CDIR}/crf.dev

${wapiti} train -t 8 -c -p ${CDIR}/crf.pattern ${CDIR}/crf.train ${CDIR}/crf.model
rm -rf ${CDIR}/crf.cqdb
${wapiti} label -m ${CDIR}/crf.model -q ${CDIR}/crf.cqdb -s ${CDIR}/crf.dev ${CDIR}/crf.dev.out
${python} ${CDIR}/conv2conll.py < ${CDIR}/crf.dev.out > ${CDIR}/crf.dev.out.conll
${perl}   ${CDIR}/conlleval.pl < ${CDIR}/crf.dev.out.conll > ${CDIR}/crf.dev.out.eval

# end main
# -----------------------------------------------------------------------------
