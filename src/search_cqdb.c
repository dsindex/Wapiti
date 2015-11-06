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

	int				i;
	char*			block = NULL;
	cqdb_t*			db = NULL;

	struct timeval t1,t2;
	
	if(argc != 2) {
		fprintf(stderr,"%s <db path>\n",argv[0]);
		exit(1);
	}

	// open and read CQDB
	if( !load_cqdb(argv[1], &block, &db) ) exit(1);

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

		i = cqdb_to_id(db, string);
		if( i != CQDB_ERROR_NOTFOUND )
			fprintf(stdout,"%s\t%d\n", string, i);

		cnt_line++;
	}

	gettimeofday(&t2, NULL);
	fprintf(stderr,"elapsed time = %lf sec\n",((t2.tv_sec - t1.tv_sec)*1000000 + t2.tv_usec - t1.tv_usec)/(double)1000000);

	// close CQDB
	unload_cqdb(block, db);

	return 0;

}
