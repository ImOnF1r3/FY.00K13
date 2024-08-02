Cookie Extractor and Manipulator

Il Cookie Extractor and Manipulator è uno strumento scritto in Python che permette di estrarre, visualizzare e modificare i cookie di una pagina web specifica. Questo tool è particolarmente utile per l'analisi della sicurezza, la manipolazione delle sessioni e i CTF (Capture The Flag) semplici o per scopi di sperimentazione.

Caratteristiche:

- Estrazione dei Cookie: Visualizza i cookie ricevuti da una pagina web.
- Iniezione dei Cookie: Permette di impostare cookie personalizzati nelle richieste HTTP.
- Visualizzazione delle Intestazioni: Mostra le intestazioni HTTP della risposta.
- Supporto ai Redirect: Gestisce automaticamente i redirect.
- Ritenta le Richieste: Configura il retry per le richieste fallite a causa di errori temporanei del server.
- Informazioni sui Crediti: Visualizza i crediti dell'autore.

Prerequisiti:

Assicurati di avere Python 3 installato sul tuo sistema. Puoi verificare la versione di Python con il comando:

python3 --version

Installazione:

1. Clona il repository:

   git clone https://github.com/ImOnF1r3/cookie-extractor.git
   cd cookie-extractor

2. Installa i requisiti:

   Utilizza pip per installare le librerie richieste. È consigliato usare un ambiente virtuale:

   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt

   Includi nel file requirements.txt le seguenti dipendenze:

   requests
   beautifulsoup4
   colorama

Utilizzo:

Esegui il tool dal terminale utilizzando i seguenti comandi:

python3 C00K13.py [opzioni]

Opzioni Disponibili:

- -u, --url: L'URL della pagina web da analizzare.
- -c, --cookies: Cookie personalizzati da impostare (nome=valore).
- -inj, --inject: Inietta cookie personalizzati nella richiesta.
- -ext, --extract: Estrae e visualizza i cookie dalla risposta.
- --key: Intestazioni aggiuntive da impostare (nome=valore).
- -cc, --credits: Mostra i crediti dell'autore.

Esempi di Utilizzo con PicoCTF (http://mercury.picoctf.net:17781/):

- Estrai i Cookie da una Pagina Web:

```
python edit_C00K13.py -u http://mercury.picoctf.net:17781/ -ext

Esempio di Output:

Fetched http://mercury.picoctf.net:17781/ with status code 200.
Response Headers:
Content-Type: text/html; charset=utf-8
Content-Length: 2048
----------------------------------------
Cookies:
Name: name
Value: -1
Domain: mercury.picoctf.net
Path: /
Expires: None
Secure: False
HttpOnly: False
----------------------------------------
Page Title: Cookies
Page Snippet:

Cookies

Home

Cookies

Welcome to my cookie search page. See how much I like different kinds of cookies!

© PicoCTF
----------------------------------------
```

- Inietta Cookie Personalizzati:

```
python edit_C00K13.py -u http://mercury.picoctf.net:17781/ -inj -c "name=18"

Esempio di Output:

Fetched http://mercury.picoctf.net:17781/check with status code 200.
Response Headers:
Content-Type: text/html; charset=utf-8
Content-Length: 1184
----------------------------------------
Page Title: Cookies
Page Snippet:

Cookies

Home

Cookies

Flag: picoCTF{Check The CTF on PicoCTF}

© PicoCTF
----------------------------------------
```

Crediti:

Author: ImOnF1r3
GitHub: https://github.com/ImOnF1r3

Questo strumento è destinato solo a scopi educativi e di ricerca. Utilizzalo responsabilmente e solo su siti web per i quali hai autorizzazione.
