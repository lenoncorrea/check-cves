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
Para o nosso script funcionar, é só colocar rodar lincando o service.
```bash
ln -s /usr/lib/zabbix/externalscripts/check-cves/check-cves.service /etc/systemd/system/
systemctl enable check-cves.service
systemctl start check-cves.service
```
### Após isso, nosso script fara o envio das CVE's

## Contribuição
Achou algum bug ou tem uma sugestão de melhoria? Envie-me!

## Licença
[MIT](https://github.com/lenoncorrea/check-cves/blob/master/LICENSE)