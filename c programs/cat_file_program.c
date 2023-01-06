#include <stdio.h>

int main(int argc, char *argv[])
{
    if (argc != 2 )  // argc should be 2 for correct execution
    {
        //We print argv[0] assuming its the program name
        printf("usage: %s", argv[0]);
    }
    else
    {
        // We assume argv[1] is the file to open
        FILE *file = fopen(argv[1], "r");

        // if fopen returns 0, the NULL pointer, on failure
        // We say the file could not be opened.
        if (file == 0)
        {
            printf("File could not open!\n");
        }
        else
        {
            int x;
             /* read one character at a time from file, stopping at EOF, which
               indicates the end of the file.  Note that the idiom of "assign
               to a variable, check the value" used below works because
               the assignment statement evaluates to the value assigned. */
            while ((x = fgetc(file)) != EOF )
            {
                printf("%c", x);
            }
            fclose(file);
        }
    }
}
