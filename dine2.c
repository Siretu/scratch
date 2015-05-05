#include <stdio.h>
#include <stdlib.h> 
#include <time.h> 
#include <limits.h>
#include <pthread.h>
#include <unistd.h>

#define NUM_FORKS 5
#define NUM_PHILS 5
#define NOTHING 0
#define EATING 1
#define THINKING 2

/*Dine Function headers*/
void dawdle();
void philosopher(void *num);

/*Print Function headers*/
void print_top();
void print_status();

/*Philosopher status struct*/

typedef struct 
{
  int activity;
  char forks[NUM_FORKS];

} Status;


/*Globals*/
int phil_count = 1;
int eat_count = 1;


/*Forks*/
pthread_mutex_t fork1;
pthread_mutex_t fork2;
pthread_mutex_t fork3;
pthread_mutex_t fork4;
pthread_mutex_t fork5;

pthread_mutex_t printlock;
pthread_mutex_t philNumLock;

Status *philosopherList[NUM_PHILS];



int main(int argc, char *argv[]) {

  /*Philosopher threads*/
  pthread_t phil_1;
  pthread_t phil_2;
  pthread_t phil_3;
  pthread_t phil_4;
  pthread_t phil_5;

  /*Get eat count*/
  if (argc > 1) {
    eat_count = (int)argv[1];
  }


  /*Initialize fork semiphores*/
  pthread_mutex_init(&fork1, NULL);
  pthread_mutex_init(&fork2, NULL);
  pthread_mutex_init(&fork3, NULL);
  pthread_mutex_init(&fork4, NULL);
  pthread_mutex_init(&fork5, NULL);

  /*Initialize print semaphore*/
  pthread_mutex_init(&printlock, NULL);

  pthread_mutex_init(&philNumLock, NULL);

  pthread_mutex_lock(&printlock);
  print_top();
  pthread_mutex_unlock(&printlock);

  /*Start the threads*/
  pthread_create(&phil_1, NULL, (void *)&philosopher, (void *)1);
  pthread_create(&phil_2, NULL, (void *)&philosopher, (void *)2);
  pthread_create(&phil_3, NULL, (void *)&philosopher, (void *)3);
  pthread_create(&phil_4, NULL, (void *)&philosopher, (void *)4);
  pthread_create(&phil_5, NULL, (void *)&philosopher, (void *)5);


  pthread_join(phil_1, NULL);
  pthread_join(phil_2, NULL);
  pthread_join(phil_3, NULL);
  pthread_join(phil_4, NULL);
  pthread_join(phil_5, NULL);

  pthread_mutex_destroy(&printlock);

  return 0;
}


void philosopher(void *my_num) {

  int philNum = (int)my_num;
  Status *mystatus = malloc(sizeof(Status));
  int i;

  // pthread_mutex_lock(&philNumLock);
  // philNum = phil_count++;
  // pthread_mutex_unlock(&philNumLock);

  // pthread_mutex_lock(&printlock);
  // printf("Philosopher %d!\n", philNum);
  // pthread_mutex_unlock(&printlock);

  // switch (philNum) {
  // case 1:
  // mystatus = &status1;
  // break;
  // case 2:
  // mystatus = &status2;
  // break;
  // case 3:
  // mystatus = &status3;
  // break;
  // case 4:
  // mystatus = &status4;
  // break;
  // case 5:
  // mystatus = &status5;
  // break;
  // default:
  // return;
  // }

  philosopherList[philNum - 1] = mystatus;

  /*initialize struct status*/
  mystatus->activity = NOTHING;
  for(i = 0; i < NUM_FORKS; i++) {
    mystatus->forks[i] = '-';
  }




  // pthread_mutex_lock(&printlock);
  // if(philNum == 1){print_status(); }
  // pthread_mutex_unlock(&printlock);

  pthread_mutex_lock(&printlock);
  print_status();
  pthread_mutex_unlock(&printlock);

  //print_status();

  

  return;


}


/*
 * sleep for a random amount of time between 0 and 999
 * milliseconds. This routine is somewhat unreliable, since it
 * doesn’t take into account the possiblity that the nanosleep
 * could be interrupted for some legitimate reason. *
 * nanosleep() is part of the realtime library and must be linked
 * with –lrt 
 */
void dawdle() { 
  struct timespec tv;
  int msec = (int)(((double)random() / INT_MAX) * 1000);

  tv.tv_sec = 0;
  tv.tv_nsec = 1000000 * msec;
  if ( -1 == nanosleep(&tv,NULL) ) {
    perror("nanosleep"); 
  }
}



/*-------------printing functions-----------------*/

void print_top() {
  printf("|=============|=============|=============|=============|=============|\n");
  printf("|      A      |      B      |      C      |      D      |      E      |\n");
  printf("|=============|=============|=============|=============|=============|\n");
}


void print_status() {
  int i, j;
  for (i = 0; i < NUM_PHILS; i++) {
    printf("| ");
    for (j = 0; j < NUM_FORKS; j++) {
      printf("%c", philosopherList[i]->forks[j]);
    }
    if (philosopherList[i]->activity == NOTHING) {
      printf("       ");
    }
    else if(philosopherList[i]->activity == EATING) {
      printf(" Eat   ");
    }
    else {
      printf(" Think ");
    }
  }
  printf("|\n");


}

// void old_print_status() {
// int i;
// //pthread_mutex_lock(&printlock);
// /*print A*/
// printf("| ");
// for (i = 0; i < NUM_FORKS; i++) {
// if(status1.forks[i]) {
// printf("%d", i);
// }
// else {
// printf("-");
// }
// }
// switch (status1.activity) {
// case 'n':
// printf("       ");
// break;
// case 'e':
// printf(" Eat   ");
// break;
// case 't':
// printf(" Think ");
// }
// /*print B*/
// printf("| ");
// for (i = 0; i < NUM_FORKS; i++) {
// if(status2.forks[i]) {
// printf("%d", i);
// }
// else {
// printf("-");
// }
// }
// switch (status2.activity) {
// case 'n':
// printf("       ");
// break;
// case 'e':
// printf(" Eat   ");
// break;
// case 't':
// printf(" Think ");
// }
// /*print C*/
// printf("| ");
// for (i = 0; i < NUM_FORKS; i++) {
// if(status3.forks[i]) {
// printf("%d", i);
// }
// else {
// printf("-");
// }
// }
// switch (status3.activity) {
// case 'n':
// printf("       ");
// break;
// case 'e':
// printf(" Eat   ");
// break;
// case 't':
// printf(" Think ");
// }
// /*print D*/
// printf("| ");
// for (i = 0; i < NUM_FORKS; i++) {
// if(status4.forks[i]) {
// printf("%d", i);
// }
// else {
// printf("-");
// }
// }
// switch (status4.activity) {
// case 'n':
// printf("       ");
// break;
// case 'e':
// printf(" Eat   ");
// break;
// case 't':
// printf(" Think ");
// }
// /*print E*/
// printf("| ");
// for (i = 0; i < NUM_FORKS; i++) {
// if(status5.forks[i]) {
// printf("%d", i);
// }
// else {
// printf("-");
// }
// }
// switch (status5.activity) {
// case 'n':
// printf("       |\n");
// break;
// case 'e':
// printf(" Eat   |\n");
// break;
// case 't':
// printf(" Think |\n");
// }
// //pthread_mutex_unlock(&printlock);
// }
