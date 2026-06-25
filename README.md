# Event Management System
**Studente:** Fabio Pieroni  
**Tipo di Progetto:** Full-Stack Web Application  
**Framework utilizzato:** Django  

## Descrizione del progetto
Applicazione web modulare per la pianificazione e la gestione di eventi, con distinzione dei flussi di lavoro in base al ruolo dell'utente.

## Funzionalità implementate per Ruolo
* **Anonymous User:** Consultazione dell'elenco degli eventi pubblici.
* **Attendee (Partecipante):** Registrazione al portale, iscrizione agli eventi e gestione delle proprie prenotazioni.
* **Organizer (Organizzatore):** Creazione, modifica e cancellazione dei propri eventi; monitoraggio della lista dei partecipanti iscritti.

## Installazione Locale
1. Clonare la repository: `git clone <url-repository>`
2. Creare l'ambiente virtuale: `python -m venv venv`
3. Attivare l'ambiente virtuale: `venv\Scripts\activate`
4. Installare le dipendenze: `pip install -r requirements.txt`
5. Eseguire le migrazioni: `python manage.py migrate`
6. Avviare il server: `python manage.py runserver`

## Database Demo (SQLite)
Il file `db.sqlite3` è incluso e pre-popolato con account fittizi e record di test.

## Account Demo per la Valutazione
* **Administrator / Superuser:** `admin_demo` / `admin12345`
* **Organizer (Organizzatore):** `organizer_demo` / `organizer12345`
* **Attendee (Partecipante):** `attendee_demo` / `attendee12345`

## Link di Deployment (PythonAnywhere)
url ancora da caricare.