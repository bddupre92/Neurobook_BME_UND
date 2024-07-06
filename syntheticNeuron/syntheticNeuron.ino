//Synthetic Arduino neuron
double n1=0.0003;
double m1=0.0011;
double h1=0.9998;
double V1=-10;
double C=1;
double g_k_max=36;
double g_Na_max=120;
double g_L=0.3;
double E_K= -12; 
double E_Na=115; 
double E_L= 10.613; 
double d_t=0.04;
double I_inj=10;
double n,m,h,V;
double n_new,m_new,h_new,V_new;

void setup() {
  // put your setup code here, to run once:
  pinMode(3, OUTPUT);
  Serial.begin(9600);
  n=n1;
  m=m1;
  h=h1;
  V=V1;
}

void loop() {

    double dn=n_prime(n, -V);
    double dm=m_prime(m, -V);
    double dh=h_prime(h, -V);
    n_new=n+dn*d_t;
    m_new=m+dm*d_t;
    h_new=h+dh*d_t;
    //Serial.println("n="+ String(n_new)+" "+"m="+String(m_new)+" "+"h="+String(h_new));
    double dV=1/C*(-1*g_k_max*pow(n,4)*(V-E_K) -g_Na_max*pow(m,3)*h*(V-E_Na) -g_L*(V-E_L)+I_inj);
    V_new=V+dV*d_t;

    //Serial.println(V_new+20);
    analogWrite(3, V_new+20);

    n=n_new;
    m=m_new;
    h=h_new;
    V=V_new;
}

double n_prime(double n, double V){
  double k_1=(0.01*(V+10))/(exp((V+10)/10)-1);
  double k_2=0.125*exp(V/80);
  double dn=k_1-(k_1+k_2)*n;
  return dn;
}

double m_prime(double m, double V){
  double k_1=0.1*(V+25)/(exp((V+25)/10)-1);
  double k_2=4*exp(V/18);
  double dm=k_1 - (k_1+k_2)*m;
  return dm;
}

double h_prime(double h, double V){
  double k_1=0.07*exp(V/20);
  double k_2=1/(exp((V+30)/10)+1);
  double dh=k_1 - (k_1+k_2)*h;
  return dh;
}
