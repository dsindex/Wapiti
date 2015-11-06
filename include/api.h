#ifdef __cplusplus
extern "C" {
#endif

#ifndef WAPITI_H
#define WAPITI_H

#include <ctype.h>
#include <float.h>
#include <stddef.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <inttypes.h>

#include "wapiti.h"
#include "gradient.h"
#include "model.h"
#include "quark.h"
#include "reader.h"
#include "sequence.h"
#include "thread.h"
#include "tools.h"
#include "decoder.h"
#include "progress.h"
#include "trainers.h"

char*	api_label_seq(mdl_t *mdl, char *strseq, bool input);
void	api_load_patterns(mdl_t *mdl, char *lines);
void	api_add_train_seq(mdl_t *mdl, char *lines);
void	api_train(mdl_t *mdl);
void	api_save_model(mdl_t *mdl, char *filename);
mdl_t*	api_load_model(char *filename, opt_t *options);
mdl_t*	api_new_model(opt_t *options, char *patterns);
void	api_free_model(mdl_t *mdl);

void	inf_log(char *msg);
void	wrn_log(char *msg);
void	err_log(char *msg);

#endif

#ifdef __cplusplus
}
#endif
