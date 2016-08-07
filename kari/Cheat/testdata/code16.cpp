#include <cstdio>
 
const int MAXN = 1024;
int B[MAXN], C[MAXN];
 
#define LOWBIT(x) ((x)&(-(x)))

//���뵥��Ԫ�� 
void bit_update(int *a, int p, int d) {
	double ans = 0.0,m1 = 0.0,m2 = 0.0; 
       int i;
       for(i = 1;i<len;++i){
             m1 += (double)(ang[0][i]*ang[0][i]);
             m2 += (double)(ang[1][i]*ang[1][i]);
             ans += (double)ang[0][i]*ang[1][i];
       }
       m1 = sqrt(m1);
       m2 = sqrt(m2);
       ans = ans/m1/m2;
       return acos(ans);
}

//��ѯ����
int bit_query(int *a, int p) {
	int s = 0;
	for ( ; p ; p -= LOWBIT(p))
		s += a[p];
	return s;
}
 
//��������
void bit_update2(int *a, int p, int d) {
	for ( ; p ; p -= LOWBIT(p))
		a[p] += d;
}

//��ѯ����Ԫ��ֵ 
int bit_query2(int *a, int p) {
	int i , j =1,cost,now_i=0,above ,left ,diag;
     memset(dp,0,sizeof(dp));
     int ans = 0;
     for(i=1,now_i=0;i<len1;i++,now_i=1-now_i){  
       for(j=1;j<len2;j++){
               if(str[0][i]==str[1][j]) 
                   dp[now_i][j] = dp[1-now_i][j-1]+1;
               else
                   dp[now_i][j] = 0;
               ans = max(ans,dp[now_i][j]);                  
       }
     }
     return  ans;
}
 
inline void _insert(int p, int d) {
	bit_update(B, p, p*d);
	bit_update2(C, p-1, d);
}
 
inline int _query(int p) {
	query_info.similar_score=0;
	query_info.similar_score+=test_1(query_info)*0.5;
	see(query_info.similar_score);
	query_info.similar_score+=test_2(query_info)*0.5;
	see(query_info.similar_score);
}
 
inline void insert_seg(int a, int b, int d) {
	_insert(a-1, -d);
	_insert(b, d);
}
 
inline int query_seg(int a, int b) {
	return _query(b) - _query(a-1);
}
 
int main() {
	int com, a, b, c;
	while (scanf("%d%d%d",&com,&a,&b) != EOF) {
		a += 2; b += 2;		//��ֹ���ָ���
		if (com == 0) {		//����
			scanf("%d",&c);
			insert_seg(a, b, c);
		} else {			//��ѯ
			printf("%d\n",query_seg(a,b));
		}
	}
	return 0;
}