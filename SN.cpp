#include<iostream>
#include<cmath>
#include<stdlib.h>

using namespace std;

float SnA(float S,float n);


int main(){
	float Sn,n;
	while(1){
	
		cout<<"Please input Sn(input 100 if you want to turn off the program): ";
		cin>>Sn;
		if(Sn==100){
			break;
		}
		else if (Sn<=0){
			cout<<"You a untouchable guy.\n";
			continue;
		}
		else if (Sn>=90){
			cout<<"I don't know what I can say\n";
			continue;
		}
		cout<<"Please input the number of GF: ";
		cin>>n;
		cout<<"Sn after caculated is "<<SnA(Sn,n)<<"\n";
	
	}
	system("pause");
	return 0;
}

float SnA(float S,float n){
	float r,a,sum=0;
	r=1+(10/(S-100));
	a=10*r;
	
	for(int i=0;i<=n-1;i++){
		sum+=10*pow(r,i);
	}
	
	return S+sum;
	
}
