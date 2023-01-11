#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#include <fcntl.h>
#include <string.h>
#include <ctype.h> 
#include <time.h>


int cronline =  0;
int estline = 0;
char *months[24] = {
    "JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC",
    "0","1","2","3","4","5","6","7","8","9","10","11"};


struct cronfileStruct{
//if any int = -1 that means *, negative value will never appear so no worries for misuse
  int min;
  int hour;
  int day;
  int month;
  int weekDay;
  char command[40];
  int minutes;
  int runs;};

struct estimatefileStruct{
  char command[40];
  int minutes;};

struct estimatefileStruct estimate[20];
struct cronfileStruct crons[20];

int length_time[20];//array of start times of processes
char names[20][40];//array of names of processes, matches order of start_time
struct tm start_time[20];//array of length to complete process, matches order of start_time

int max_running = 0;//most processes running at once
char most_ran_command[40];//name of command that ran the most
int num_runs = 0;//overall number of processes running


void simulation(int month_int){//simulates cron testing min by min
    int total = 0;//current processes running
    int command_runs = 0;//number of runs of the most ran process

    if(time(NULL) == (time_t)(-1)){//if time can be retrieved
        printf("Time: current time can't be accesed\n");
        return;
    }

    struct tm current_time = *localtime(&(time_t){time(NULL)});//date by sec since epoc (note: OS dependable due to epoch)
    

    //sets data type struct tm as: year, month, day, hour, minute, second
    //with starting conditions of current year, and start of given month
    struct tm sim_time = {.tm_year = current_time.tm_year, .tm_mon = month_int, .tm_mday = 1};
    bool first_invoked;

    while (sim_time.tm_mon == month_int){//every minute
        first_invoked = true;
        for (int i = 0; i <= cronline; i++){//loops through crons commands structure 

            if ((crons[i].month == sim_time.tm_mon || crons[i].month == -1) && (crons[i].day == sim_time.tm_mday || crons[i].day == -1) 
            && (crons[i].hour == sim_time.tm_hour || crons[i].hour == -1) && (crons[i].min == sim_time.tm_min || crons[i].min == -1)
            && (crons[i].weekDay == sim_time.tm_wday || crons[i].weekDay == -1)){//if time to execute command

                if (first_invoked){//only need to terminate if commands are being invoked
                    for (int j = 0; j < 19; j++){//at most 20 processes running so 0-19
                        if ((difftime(mktime(&sim_time), mktime(&start_time[j]))) >= length_time[j]*60 && length_time[j] != 0){
                            length_time[j] = 0;
                            printf("terminated %s\n", names[j]);
                            total--;
                        }
                    }
                }

                first_invoked = false;

                printf("invoked %s: %s", crons[i].command, asctime(&sim_time));
                total++;
                num_runs++;
                crons[i].runs++;

                for (int j = 0; j < 19; j++){//loops for running array
                    if(length_time[j] == 0){//adds command name to array if spot is empty
                        length_time[j] = crons[i].minutes;
                        start_time[j] = sim_time;//assings sim_time to same spot of running array to length_time
                        strcpy(names[j], crons[i].command);
                        break;
                    }
                }

                if (max_running < total){//if current num of proccesses running is greater than prev max running at moment
                    max_running = total;
                }
            }
        }
        
        sim_time.tm_min++;//+1 min
        mktime(&sim_time);
    }
    for (int i = 0; i <= cronline; i++){
        if (crons[i].runs > command_runs){//if command number of runs is greater than the previous max
            command_runs = crons[i].runs;
             strcpy(most_ran_command, crons[i].command);
        }
    }
}

char *trim(char *str){//trims string of begining whitespaces ("    hello world " ---> "hello world")

    size_t len = strlen(str);//length of string

    while(isspace(str[len - 1])){//if end char is white space
        len--;//-1 to account full null byte
    }

    while(*str && isspace(*str)){//starts string +1 ahead if white space, -1 len to account for shorter string
        str++;
        len--;
    }
    
    str[strcspn(str, "\n")] = 0;//removes \n at end of line if exist 

    return strndup(str, len);//returns shortened star of str - the length of white spaces at end 
}

bool estimate_valid(FILE *est, char estimates_file[]){//if estimate file info valid and adds to structure
    int bufferLength = 100;
    char buffer[bufferLength];

    //read Each line will be at most 100 characters long, 20 command lines at most 
    while( fgets(buffer, bufferLength, est)){//reads line by line until end of file

        char *trimline = trim(buffer);

        if (trimline[0] != '#'){//skip line if comment line
        	char *commandName = strtok(trimline, " \t");//splits string by char ' ', will return null if no ' '
            char *time = strtok(NULL, " \t");
            char *final = strtok(NULL, " \t");

            if (commandName == NULL || time == NULL || strtok(NULL, " \t") != NULL){
                //if no ' ' or 2 or more ' ' 
                printf("Error in: '%s'\n", buffer);
                printf("File: %s is not properly formated\n", estimates_file);

                return false;
            }

            if (!isdigit(*time)){//if time is not an int 
                printf("Error in: '%s'\n", buffer);
                printf("File: %s is not properly formated\n", estimates_file);
                return false;
            }

            strcpy(estimate[estline].command, commandName);
            estimate[estline].minutes = atoi(time);
            
            estline++;
        }
    }
    for (int i = 0; i < estline; i++){//printing all of estimate file 
        printf("%s %d\n", estimate[i].command , estimate[i].minutes);
    }
    printf("\n");
    fclose(est);
    return true;
}

bool cron_valid(FILE *cron, char crontab_file[]){//if cron file info valid and adds to structure
    int bufferLength = 100;
    char buffer[bufferLength];
    char *weekDays[14] = {
    "SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT",
    "0","1","2","3","4","5","6"};
    
    while( fgets(buffer, bufferLength, cron)){//reads line by line until end of file

        char *trimline = trim(buffer);
        bool is_month = false;
        bool is_weekday = false;
        bool stars[5] = {false};
        
        if (trimline[0] != '#'){//skip line if comment line
            char *min = strtok(trimline, " \t");//splits string by char ' ', will return null if no ' '
            char *hour = strtok(NULL, " \t");
            char *day = strtok(NULL, " \t");
            char *month = strtok(NULL, " \t");
            char *weekDay = strtok(NULL, " \t");
            char *commandName = strtok(NULL, " \t");

        
            if (min == NULL || hour == NULL || day == NULL || month == NULL || weekDay == NULL || commandName == NULL ||
            strtok(NULL, " \t") != NULL){//if less than 5 ' ' or less than 5 ' '
                printf("Error in: '%s'\n", buffer);
                printf("File: %s is not properly formated\n", crontab_file);
                return false;
            }

            if (strcmp("*", min) == 0){//assings -1 if *
                    min = "-1";
                    stars[0] = true;
            }
            if (strcmp("*", hour) == 0){//assings -1 if *
                    hour = "-1";
                    stars[1] = true;
            }
            if (strcmp("*", day) == 0){//assings -1 if *
                    day = "-1";
                    stars[2] = true;
            }

            for (size_t i = 0 ; month[i] != '\0' ; ++i)//capitalises all char of month
                month[i] = toupper((unsigned char) month[i]);
            
            for (size_t i = 0 ; weekDay[i] != '\0' ; ++i)//capitalises all char of weekday
                weekDay[i] = toupper((unsigned char) weekDay[i]);


            //iterate through month's elements and compares to argument month
            for (int i = 0; i < 24; i++){
                
                if (strcmp("*", month) == 0){//assings -1 if *
                    month = "-1";
                    stars[3] = true;
                    is_month = true;
                    break;
                }

                if (strcmp(months[i], month) == 0){
                    is_month = true;
                    if (i < 12){//month_int equals index of matching month if "JAN"-"DEC"
                        sprintf(month, "%d", i);
                    }
                    else{//month_int equals int of matching if "0"-"11"
                        month = months[i];
                    }
                    break;
                }
            }

            //iterate through week days's elements and compares to argument month
            for (int i = 0; i < 14; i++){
                if (strcmp("*", weekDay) == 0){//assings -1 if *
                    stars[4] = true;
                    is_weekday = true;
                    weekDay = "-1";
                    break;
                }
                if (strcmp(weekDays[i], weekDay) == 0){
                    is_weekday = true;
                    if (i < 7){//month_int equals index of matching month if "SUN" - "SAT"
                        sprintf(weekDay, "%d", i);
                    }
                    else{//month_int equals int of matching if "0"-"6"
                        weekDay = weekDays[i];
                    }
                    break;
                }
            }
            
            if (is_weekday == false || is_month == false){
                printf("Error in: '%s'\n", buffer);
                printf("File: %s is not properly formated\n", crontab_file);
                return false;
            }

            if (!(isdigit(*min) || stars[0])|| !(isdigit(*hour) || stars[1]) || !(isdigit(*day) || stars[2])
            || !(isdigit(*month) || stars[3]) || !(isdigit(*weekDay) || stars[4])){//if time is not an int or begining char '-'
                printf("File: %s is not properly formated\n", crontab_file);
                return false;
            }

            //assigns commands info to associated structure
            crons[cronline].min = atoi(min);
            crons[cronline].hour = atoi(hour);
            crons[cronline].day = atoi(day);
            crons[cronline].month = atoi(month);
            crons[cronline].weekDay = atoi(weekDay);
            strcpy(crons[cronline].command, commandName);
            cronline++;
        }
    }
      
    for (int i = 0; i < cronline; i++){//printing all of estimate file 
        printf("%d %d %d %d %d %s\n", crons[i].min, crons[i].hour, crons[i].day, crons[i].month, crons[i].weekDay, crons[i].command);
    }

    fclose(cron);
    return true;
}

bool validity_files(char crontab_file[], char estimates_file[]){//if files can be open, calls function to valididate of whats in the files
    FILE   *cron, *est;
    cron = fopen(crontab_file, "r");//returns a FILE pointer of crontab_file
    est = fopen(estimates_file, "r");//returns a FILE pointer of estimates_file

    bool valid = true;
    if(cron==NULL){//if crontab_file can't be opened for read only
        printf("Usage: file %s can not be read\n", crontab_file); 
        valid = false;//not return so est can be tested before function ends
    }

    if(est==NULL){//if estimates_file can't be opened for read only
        printf("Usage: file %s can not be read\n", estimates_file); 
        valid = false;
    }

    if (valid == false) return false;
    
    if (estimate_valid(est, estimates_file) == false) return false;

    if (cron_valid(cron, crontab_file) == false ) return false;

    return true;
}

int validity_month(char month[]){//function to check if month is valid
    //return false if args not valid, true if args are valid

    int month_int = -1;//will remain -1 if not valid month
    //iterate through month's elements and compares to argument month
    for (int i = 0; i < 24; i++){
        if (strcmp(months[i], month) == 0){
            if (i < 12){//month_int equals index of matching month if "JAN"-"DEC"
                month_int = i;
            }
            else{//month_int equals int of matching if "0"-"11"
                month_int = atoi(months[i]);
            }
            break;
        }
    }

    if (month_int == -1){//no matching month
        printf("Usage: invalid month, %s\n", month); 
    }
    
    //passes all validity of arguments checks
    return month_int;
}

void est_to_cron(){//adding estimate time to corrisponding cron command structure
    for (int i = 0; i < cronline; i++){//every cron command
        for (int j = 0; j < estline; j++){//every est command
            if (strcmp(crons[i].command, estimate[j].command) == 0){//if names are equal
                crons[i].minutes = estimate[j].minutes;//assigns the est minutes to cron struct
            }
        } 
    }
}

int main(int argc, char *argv[]){

    //checking for 4 argument count, terminate if not
    if (argc != 4){
        printf("Usage: %s invalid argument count\n", argv[0]+2);
		return EXIT_FAILURE;
    }

    //change char of month to upper, char by char
    int i = 0;
    while (argv[1][i]) { 
        argv[1][i] = toupper(argv[1][i]);
        i++; 
    }


    int month_int = validity_month(argv[1]);//month as 0-11
    if (month_int == -1){//if not valid month
        return EXIT_FAILURE;
    }
    
    if (!validity_files(argv[2],argv[3])){
        return EXIT_FAILURE;
    }

    est_to_cron();

    simulation(month_int);

    printf("%s %d %d\n",most_ran_command, num_runs, max_running);

    return EXIT_SUCCESS;
   
}
