#include <stdio.h>
#include <math.h>

int main(void)
{
float a,x,g,f,y,h;
printf("Введите x ");
scanf("%f", &x);
printf("Введите a ");
scanf("%f", &a);
printf("Выбирите функцию g=1,f=2,y=3 ");
scanf("%f", &h);
if (h==1){
	g=(3*(4*a*a+13*a*x+9*x*x))/(10*a*a-51*a*x+5*x*x);
	printf("g=%f\n\n",g);
}
else if (h==2){
	f=cos(6*a*a+a*x-2*x*x);
	printf("f=%f\n\n",f);
}
else{
	y=acos(14*a*a+37*a*x+5*x*x+1);
	printf("y=%f\n\n",y);
}

}
