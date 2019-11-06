


#include <stdio.h>
#include <math.h>

int main(void)
{
float a,x,s,f,g,y;
int funct;
printf("Введите x: ");
scanf("%f", &x);
printf("Введите a: ");
scanf("%f", &a);
printf("Введите Функцию ф-ию посчитать: g-1,f-2,y-3:  ");
scanf("%i", &funct);

switch(funct) {
    case 1:
        if(a ){
        g=((3*(4*a*a+13*a*x+9*x*x))/(10*a*a-51*a*x+5*x*x));
        printf("%f\n", g);
        break;
}
    case 2:
      f=(cos(6*a*a+a*x-2*x*x));
      printf("%f\n", f);
      break;
    case 3:
      y = (acos(14*a*a+37*a*x+5*x*x+1));
      printf("%f\n", y);
      break;
    default:
        printf("ERROR");
}
return 0;
}

