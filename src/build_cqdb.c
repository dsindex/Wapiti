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

	int				ret;
	FILE*			fp = NULL;
	cqdb_writer_t*	dbw = NULL;
	int				count=0;

	struct timeval t1,t2;
	
	if(argc != 2) {
		fprintf(stderr,"%s <db path>\n",argv[0]);
		exit(1);
	}

	// create CQDB for writing
	if( !open_cqdb(argv[1], &fp, &dbw) ) exit(1);

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

		ret = cqdb_writer_put(dbw, string, count);
		if( ret ) {
			fprintf(stderr, "fail to put a pair (%s,%d)\n", string, count);
			break;
		}
		count++;

		cnt_line++;
	}

	gettimeofday(&t2, NULL);
	fprintf(stderr,"elapsed time = %lf sec\n",((t2.tv_sec - t1.tv_sec)*1000000 + t2.tv_usec - t1.tv_usec)/(double)1000000);

	// close CQDB
	close_cqdb(fp, dbw);

	return 0;

}
