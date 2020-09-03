# Monitorando CVE's e enviando pelo Telegram
## Pré requisitos
Instale os pacotes Git e Python3.7 no servidor do Zabbix.

```bash
apt install git python3.7 python3-venv -y
```
## Baixando
```bash
cd /usr/lib/zabbix/externalscripts/
git clone https://github.com/lenoncorrea/check-cves.git
```
## VirtualEnv
Crie um venv na pasta do nosso script e instale os requerimentos, e por ultimo, dê permissão ao script para ser executado.
```python
python3 -m venv /usr/lib/zabbix/externalscripts/check-cves/venv
. /usr/lib/zabbix/externalscripts/check-cves/venv/bin/activate
pip install -r /usr/lib/zabbix/externalscripts/check-cves/requirements.txt
```
```bash
chmod 775 /usr/lib/zabbix/externalscripts/check-cves/cves.py
```
## Ajustes de envio para o Telegram
Copie o arquivo '.env.example' para '.env', e insira os valores corretos nas variaveis.
```bash
TOKEN="" --> TOKEN DO SEU BOT, QUE FARÁ O ENVIO
CHAT_ID="" --> USUÁRIO OU GRUPO QUE IRÁ RECEBER

```
## Colocando em funcionamento
Para o nosso script funcionar, é só colocar rodar, com o comando abaixo.
```bash
/usr/lib/zabbix/externalscripts/check-cves/venv/bin/python cves.py nohup
```
### Apóso comando acima, o terminal ficara rodando, aí vem a mágica, use um 'CTRL+Z' e o terminal vai fechar e parar o script. Em seguida digite 'bg' no terminal, e nosso script vai seguir rodando em background.

## Contribuição
Achou algum bug ou tem uma sugestão de melhoria? Envie-me!

## Licença
[MIT](https://github.com/lenoncorrea/check-cves/blob/master/LICENSE)