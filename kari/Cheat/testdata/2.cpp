nclude <iostream>
#include <cmath>
#include <algorithm>
#include <iomanip>
 
 using namespace std;
  
  const double EPS = 1e-8;
  const int N = 10000 + 3;
   
    bool cmp(Point a, Point b)
    {
            if (fabs(a.y - b.y) <= EPS)
                        return a.x < b.x;
                            return a.y < b.y;
    }
   struct Point
   {
           double x;
               double y;
   };
     
       double Area(Point *p, int nv)
       {
               if (nv < 3) return 0;
                   int i;
                       double ret = 0;
                           for (i = 2; i < nv; i++)
                                   {
                                               ret += xmult(p[0], p[i - 1],
                                               p[i]) / 2.0;
                                                   }
                                                       return ret;
       }
      int Graham_Scan(Point *p, int nv, Point *res)  
      {
              int i, top;
               
                   sort(p, p + nv, cmp);
                       if (nv < 0) return 0;
                           res[0] = p[0];
                               if (nv == 1) return 1;
                                   res[1] = p[1];
                                       if (nv == 2) return 2;
                                          
                                              top = 1;
                                                  for (i = 2; i < nv; i++)   
                                                          {
                                                                      while
                                                                          (top
                                                                          >= 1
                                                                          >&&
                                                                          >xmult(res[top],
                                                                          >res[top
                                                                          >-
                                                                          >1],
                                                                          >p[i])
                                                                          >> 0)
                                                                          >> top--;
                                                                                  res[++top]
                                                                                  =
                                                                                  p[i];
                                                                                      }
                                                                                          for
                                                                                              (i
                                                                                              =
                                                                                              nv
                                                                                              - 2;
                                                                                                i
                                                                                                >=
                                                                                                >0;
                                                                                                >i--)
                                                                                                  {
                                                                                                              while
                                                                                                                  (top
                                                                                                                  >=
                                                                                                                  >1
                                                                                                                  >&&
                                                                                                                  >xmult(res[top],
                                                                                                                  >res[top
                                                                                                                  >-
                                                                                                                  >1],
                                                                                                                  >p[i])
                                                                                                                  >> 0)
                                                                                                                  >> top--;
                                                                                                                          res[++top]
                                                                                                                          =
                                                                                                                          p[i];
                                                                                                                              }
                                                                                                                               
                                                                                                                                   return
                                                                                                                                   top;
      }
     double xmult(Point a, Point b, Point c)   
     {
             return (((b.x - a.x) * (c.y - a.y)) - (c.x - a.x) * (b.y - a.y));
     }
       
        
        Point p[N], res[N];
         
         int main ()
         {
                 int j,N;
                     while (scanf("%d", &N) != EOF)
                             {
                                         for (j = 0; j < n; j++)
                                                         scanf("%lf%lf",
                                                         &p[j].x,&p[j].y);
                                                                 int T =
                                                                 Graham_Scan(p,
                                                                 N, res);
                                                                         double
                                                                         ans =
                                                                         Area(res,
                                                                         T);
                                                                         cout<<fixed<<setprecision(1)<<ans<<endl;
                                                                             }
         }
