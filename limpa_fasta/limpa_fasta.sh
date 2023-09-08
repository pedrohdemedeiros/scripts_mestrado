#!/bin/bash

# Verifica se os argumentos foram fornecidos
if [ "$#" -ne 2 ]; then
  echo "Uso: $0 <diretório_dos_fastas> <nome_do_fasta_final>"
  exit 1
fi

# Argumentos
dir_fastas=$1
fasta_final_name=$2

# Concatena todos os arquivos FASTA no diretório especificado
cat "${dir_fastas}"/*.fasta > "$fasta_final_name"

# Criando arquivo com cabeçalhos brutos
echo "Criando arquivos com cabeçalhos brutos..."
grep ">" "$fasta_final_name" > cabecalhos_brutos.list
echo "cabecalhos_brutos.list criado"

# Limpando o fasta
echo "Limpando fasta..."
sed -i -e 's/-//g' -e 's/)//g' -e 's/(//g' -e 's/;//g' \
      -e 's/://g' -e 's/|//g' -e 's/\.//g' -e 's/]//g' \
      -e 's/\[//g' -e 's/ //g' -e 's/_//g' -e "s/'//g" \
      -e 's/"//g' -e 's/=//g' -e 's/,//g' -e 's/\///g' \
      -e 's/>9/9/g' -e 's/>8/8/g' -e 's/>7/7/g' -e 's/>6/6/g' \
      -e 's/>5/5/g' -e 's/>4/4/g' -e 's/>3/3/g' -e 's/>2/2/g' \
      -e 's/>1/1/g' -e 's/>0/0/g' "$fasta_final_name"
echo "Fasta limpo"

# Criando arquivo com cabeçalhos limpos
echo "Criando arquivo de cabeçalhos limpos"
grep ">" "$fasta_final_name" > cabecalhos_limpos.list
sed -i 's/>//g' cabecalhos_limpos.list
echo "cabecalhos_limpos.list criado"

# Criando script para renomeação
echo "Criando arquivo de renomeação de fasta"
touch renomeia.sh
chmod +x renomeia.sh
n=0

for m in $(cat cabecalhos_limpos.list)
do 
	n=$((n+1))

	if [ "$n" -le 9 ]
	then
		echo "sed -i 's/$m/xxxx$n/g' $fasta_final_name" >> renomeia.sh
	elif [ "$n" -le 99 ]
	then
		echo "sed -i 's/$m/xxx$n/g' $fasta_final_name" >> renomeia.sh
	elif [ "$n" -le 999 ]
	then
		echo "sed -i 's/$m/xx$n/g' $fasta_final_name" >> renomeia.sh
	else
		echo "sed -i 's/$m/x$n/g' $fasta_final_name" >> renomeia.sh
	fi
done
echo "renomeia.sh criado"

# Renomeando fasta
echo "renomeando fasta..."
./renomeia.sh
echo "Fasta renomeado"

echo "Para fazer um arquivo utilizado para renomear a árvore resultante posteriormente, digite SIM. Para sair, digite qualquer outra coisa"
read resp
if [ $resp != 'SIM' ]; then
    exit 0
fi

# Recuperando siglas para renomear a árvore
echo "Criando arquivo de siglas..."
awk '{print $1}' cabecalhos_brutos.list > siglas
sed -i -e 's/_cds_/\*/g' -e 's/>//g' -e 's/lcl|//g' -e 's/.1_1//g' -e 's/.2_1//g' siglas
sed -i 's/^.*\*//g' siglas
echo "siglas criado"
echo "Confira o arquivo de siglas e digite SIM para continuar"
read resp
if [ $resp != 'SIM' ]; then
    exit 0
fi

# Criando script de renomeação inversa para a árvore
echo "Criando arquivo de renomeacao de arvore..."
n=0

for m in $(cat siglas)
do 
	n=$((n+1))

	if [ "$n" -le 9 ]
	then
		echo "sed -i 's/xxxx$n/$m/g' exemplo.fasta" >> renomeia_inverso.sh
	elif [ "$n" -le 99 ]
	then
		echo "sed -i 's/xxx$n/$m/g' exemplo.fasta" >> renomeia_inverso.sh
	elif [ "$n" -le 999 ]
	then
		echo "sed -i 's/xx$n/$m/g' exemplo.fasta" >> renomeia_inverso.sh
	else
		echo "sed -i 's/x$n/$m/g' exemplo.fasta" >> renomeia_inverso.sh
	fi
done
echo "renomeia_inverso.sh criado"
chmod +x renomeia_inverso.sh
echo "Finalizado"
