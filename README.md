Cookie Extractor and Manipulator

Cookie Extractor and Manipulator è un tool scritto in Python che consente di estrarre, visualizzare e modificare i cookie per una pagina web specifica. È particolarmente utile per le analisi di sicurezza, la manipolazione di sessioni e i CTF (Capture The Flag).

Caratteristiche

- Estrazione dei Cookie: Visualizza i cookie ricevuti da una pagina web.
- Iniezione dei Cookie: Consente di impostare cookie personalizzati nelle richieste HTTP.
- Visualizzazione delle Intestazioni: Mostra le intestazioni HTTP di risposta.
- Supporto ai Redirect: Gestisce automaticamente i redirect.
- Ritenta le Richieste: Configurazione del retry per richieste fallite a causa di errori temporanei del server.
- Informazioni sui Crediti: Visualizza i crediti dell'autore.

Prerequisiti

Assicurati di avere Python 3 installato sul tuo sistema. Puoi verificare la versione di Python con il comando:

python3 --version

Installazione

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

Utilizzo

Esegui il tool dal terminale utilizzando i seguenti comandi:

python3 C00K13.py [opzioni]

Opzioni Disponibili

- -u, --url: L'URL della pagina web da analizzare.
- -c, --cookies: Cookie personalizzati da impostare (nome=valore).
- -inj, --inject: Inietta cookie personalizzati nella richiesta.
- -ext, --extract: Estrae e visualizza i cookie dalla risposta.
- --key: Intestazioni aggiuntive da impostare (nome=valore).
- -cc, --credits: Mostra i crediti dell'autore.

Esempi

- Estrai i Cookie da una Pagina Web:

  python3 C00K13.py -u http://example.com -ext

- Inietta Cookie Personalizzati:

  python3 C00K13.py -u http://example.com -inj -c "sessionid=12345" -ext

- Visualizza i Crediti:

  python3 C00K13.py -cc

Crediti

Author: ImOnF1r3
GitHub: ImOnF1r3

Questo strumento è destinato solo a scopi educativi e di ricerca. Utilizzalo responsabilmente e solo su siti web per i quali hai autorizzazione.
