#include<iostream>
#include<cstdlib> 
using namespace std;

string TB(int s1,int s2,string p1,string p2);

int main(){
	int s1,s2; string p1,p2;
	
	cout<<"Input the first person's name and Sn: ";
	cin>>p1>>s1;
	cout<<"Input the seconnd person's name and Sn: ";
	cin>>p2>>s2;
	cout<<TB(s1,s2,p1,p2);
	system("pause");
	return 0;
	
	
}
string TB(int s1,int s2,string p1,string p2){
	int a1,b1,a2,b2,det;
	a1=s1/10;
	b1=s1%10;
	a2=s2/10;
	b2=s2%10;
	det=a1*b2-a2*b1;
	
	if(a1>100)return ("GODLIKE");
	
	else if(det==0){
		return ("You are extremely orgiastic.\n");
	}
	else if(det>0){
		return (p1+" is Top.\n");
	}
	else return (p2+" is Top.\n");
	
	
	
} 
