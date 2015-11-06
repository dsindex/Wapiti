#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <sys/time.h>

#include "api.h"

#define	LINE_SIZE		10240

int main(int	argc, char	*argv[])
{
	int		        size;
	char	        string[LINE_SIZE+1];
	int		        cnt_line;

	mdl_t*			model;
	opt_t			opt = opt_defaults;
	char*			out;

	struct timeval t1,t2;
	
	if(argc != 2) {
		fprintf(stderr,"%s <model path>\n",argv[0]);
		exit(1);
	}

	opt.mode = 1;		// label
	opt.outsc = true;	// output score
	model = api_load_model(argv[1], &opt);
	if( !model ) {
		fprintf(stderr,"load fail : %s \n",argv[1]);
		exit(1);
	}

	gettimeofday(&t1, NULL);

	cnt_line = 0;
	while(fgets(string, LINE_SIZE, stdin) != NULL) {
		size = strlen(string);
		if(string[size-1] == '\n'){
			string[size-1] = '\0';
			--size;
		}
		if(size > 1 && string[size-1] == '\r'){
			string[size-1] = '\0';
			--size;
		}
		if(string[0] == '\0')
			continue;
		
		out = NULL;
		out = api_label_seq(model, string, true);
		if( out ) {
			fprintf(stdout, "%s\n", out);
			free(out);
		}

		cnt_line++;
	}

	gettimeofday(&t2, NULL);
	fprintf(stderr,"elapsed time = %lf sec\n",((t2.tv_sec - t1.tv_sec)*1000000 + t2.tv_usec - t1.tv_usec)/(double)1000000);

	if( model ) api_free_model(model);

	return 0;

}
