# 3. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados
# da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
# e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades
# de latas de tinta a serem compradas e o preço total. 

metros = float(input('Tamanho de metros quadrados a ser pintado: '))
lata = 80
litros = 18
print(f'A sua pintura de {metros}m² vai usar {litros * 3 - metros} e vai pagar') 


cd /opt
wget https://www.sqlite.org/2019/sqlite-autoconf-3310100.tar.gz
tar -xzf sqlite-autoconf-3310100.tar.gz
cd sqlite-autoconf-3310100
./configure
make
sudo make install