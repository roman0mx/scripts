#!/bin/bash

cat /etc/openvpn/clientes/machote1 >> $1.ovpn

echo "<ca>"  >> $1.ovpn
cat /etc/openvpn/rsa/keys/ca.crt >> $1.ovpn
echo "</ca>"  >> $1.ovpn

echo "<cert>"  >> $1.ovpn
cat /etc/openvpn/rsa/keys/$1.crt >> $1.ovpn
echo "</cert>"  >> $1.ovpn

echo "<key>"  >> $1.ovpn
cat /etc/openvpn/rsa/keys/$1.key >> $1.ovpn
echo "</key>"  >> $1.ovpn

echo "Finalizado... $1 "

