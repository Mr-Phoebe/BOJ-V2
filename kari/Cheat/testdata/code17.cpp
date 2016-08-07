#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
using namespace std;
const int maxn = 7100;    //����ֻ����sqrt(50000000)�Ϳ�����
const long long mod = 9901;
long long a,b,p,q;      //ȫ������Ϊlong long��
int cnt;
int prim[maxn];
long long tab[maxn][3];
void table()
{
    memset(prim,0,sizeof(prim));
//     memset(tab,0,sizeof(tab));
    for(int i = 2; i<=(int)sqrt(maxn); i++)
    {
        if(!prim[i])
        {
            for(int j =i*i; j<=maxn; j+=i)
                prim[j] = 1;
        }
    }
}
long long power(long long aa,long long bb,long long pp) //������a^b mod p
{
     int count = 0;
     long long xx = bb;
     while(xx)
     {
         count++;
         xx/=2;
     }
    // count--;
  //  printf("count=%d\n",count);
     long long ans = 1;
     long long xy =  aa%pp;
     for(int i = 0;i<count;i++)
     {
         if((1<<i)&bb)
           ans = (ans*xy)%pp;
         xy = (xy*xy)%pp;
     }
     return ans;
}
void div()  //��ʽ�ֽ⡣ͬʱ�ѷ��������Ľ���ͷ�ĸ�ĳ˻��������
{
    for(int i = 0 ; i<cnt; i++)
    {
        if(a==1)break;
        if(a%tab[i][0]==0)
        {
            while(a%tab[i][0]==0)
            {
                tab[i][1]++;
                a/=tab[i][0];
            }
            if(tab[i][0]%mod==1)p = (p*((((b%mod)*(tab[i][1]%mod))%mod+1)%mod))%mod;
            //ע��ai mod pΪ1�����Ρ�
            else
            {
             long long tmp=power(tab[i][0],tab[i][1]*b+1,mod);
             p = (p*((tmp-1+mod)%mod))%mod;
           //  printf("%lld\n",p);
             q = (q*((tab[i][0]-1)%mod))%mod;
            // printf("tab[0]=%lld q=%lld\n",tab[i][0],q);
            }
        }
    }
    if(a>1)   //�ر�ע�⣡�����ܻ�ʣ�����1�����ӡ��������ִ���sqrt(a)������һ����
    {
       if(a%mod==1)p = (p*((b%mod+1)%mod))%mod;
       else
       {
          long long tmp = power(a,b+1,mod);
          p =(p*((tmp-1+mod)%mod))%mod;
          q = (q*((a-1)%mod))%mod;
       }
    }
}
long long exd_gcd(long long aa,long long bb,long long & x,long long & y) //��չgcd�����Ԫ��
{
     if(bb==0)
     {
         x = 1;
         y = 0;
         return aa;
     }
     long long d = exd_gcd(bb,aa%bb,x,y);
     long long temp = y;
     y = x-(floor(aa/bb)*y);
     x = temp;
     return d;
}
void solve()
{
    memset(tab,0,sizeof(tab));
    cnt = 0;
    long long x,y;
    for(int i = 2; i<=maxn; i++)
        if(!prim[i])tab[cnt++][0] = (long long)i;
  /*  for(int i = 0;i<5;i++)
       printf("%d\n",tab[i][0]);*/
    p = 1;
    q = 1;
    div();
  //  printf("p=%lld q=%lld\n",p,q);
   // printf("p=%d q=%d\n",p,q);
    exd_gcd(q,mod,x,y);
    long long ans = (p*((x%mod+mod)%mod))%mod;
    printf("%lld\n",ans);
}
int main()
{
    int i,j;
    table();
    while(scanf("%lld%lld",&a,&b)!=EOF)
    {
        solve();
    }
    return 0;
}