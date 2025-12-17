# Flask-prosjekt -- Dokumentasjon

## 1. Forside

**Prosjekttittel: Klesbutikk**\
**Navn: Mila**\
**Klasse: 2IMI**\
**Dato: 11/13/2025**

**Kort beskrivelse av prosjektet:**\
*Applikasjonen er en nettbutikk for klær der brukere kan se gjennom produkter, legge varer i handlekurven og bestille klær på nett. Brukerne kan også opprette en konto og logge inn for å administrere bestillingene sine. Temaet bygger på netthandel og brukervennlig design for en moderne klesbutikk.*

------------------------------------------------------------------------

## 2. Systembeskrivelse

**Formål med applikasjonen:**\
Formålet med applikasjonen Irisbutikk er å utvikle en enkel og brukervennlig nettbutikk for klær. Løsningen gjør det mulig for brukere å bla gjennom produkter, opprette en brukerprofil og gjennomføre bestillinger på en effektiv måte. Applikasjonen ble utviklet for å lære og demonstrere bruk av webteknologi koblet mot en relasjonsdatabase (MariaDB) ved hjelp av Python.

Prosjektet har som mål å vise hvordan man kan implementere grunnleggende funksjonalitet for en nettbutikk, inkludert lagring av produkter, brukerdata og bestillinger. Samtidig skal applikasjonen være lett å navigere, gir oversiktlig informasjon og støtte trygg lagring av data i en strukturert database.

**Brukerflyt:**\
Brukeren starter på forsiden av applikasjonen, hvor det vises en velkomstmelding med teksten «Velkommen til butikken» samt en knapp for å kjøpe varer. Når brukeren trykker på Buy-knappen, blir de sendt videre til en side som viser en liste over tilgjengelige klær.

På produktsiden kan brukeren velge et plagg og trykke på Bestill. Dette fører brukeren til et bestillingsskjema der nødvendig informasjon fylles inn, som navn, kontaktinformasjon og bestillingsdetaljer. Når skjemaet er sendt inn, lagres informasjonen i databasen.

Etter at bestillingen er fullført, blir brukeren sendt til en bekreftelsesside som viser en takk for bestillingen. På denne siden har brukeren mulighet til å gå tilbake til forsiden.

**Teknologier brukt:**

-   Python / Flask\
-   MariaDB\
-   HTML / CSS /

------------------------------------------------------------------------

## 3. Server-, infrastruktur- og nettverksoppsett

### Servermiljø

*Ubuntu v.25, Mariadb, Rasberry pi*

### Nettverksoppsett

-   Nettverksdiagram
-   IP-adresser\
  ip-adresser for server (rasberry pi): 10.200.14.21, ip-adresse for klient(windows): 10.2.0.231
-   Porter\
  To                         Action      From
--                         ------      ----
22/tcp                     ALLOW       Anywhere
80                         ALLOW       Anywhere
Samba                      ALLOW       Anywhere
3306                       ALLOW       Anywhere
3306/tcp                   ALLOW       Anywhere
22/tcp (v6)                ALLOW       Anywhere (v6)
80 (v6)                    ALLOW       Anywhere (v6)
Samba (v6)                 ALLOW       Anywhere (v6)
3306 (v6)                  ALLOW       Anywhere (v6)
3306/tcp (v6)              ALLOW       Anywhere (v6)
-   Brannmurregler
  To                         Action      From
--                         ------      ----
22/tcp                     ALLOW IN    Anywhere
80                         ALLOW IN    Anywhere
137,138/udp (Samba)        ALLOW IN    Anywhere
139,445/tcp (Samba)        ALLOW IN    Anywhere
3306                       ALLOW IN    Anywhere
3306/tcp                   ALLOW IN    Anywhere
22/tcp (v6)                ALLOW IN    Anywhere (v6)
80 (v6)                    ALLOW IN    Anywhere (v6)
137,138/udp (Samba (v6))   ALLOW IN    Anywhere (v6)
139,445/tcp (Samba (v6))   ALLOW IN    Anywhere (v6)
3306 (v6)                  ALLOW IN    Anywhere (v6)
3306/tcp (v6)              ALLOW IN    Anywhere (v6)

Eksempel:

    Klient → Waitress → MariaDB

### Tjenestekonfigurasjon

-   systemctl / Supervisor

Applikasjonen er utviklet for å kunne kjøres som en tjeneste ved hjelp av systemverktøy som systemctl eller Supervisor. Dette gjør det mulig å starte og stoppe applikasjonen på en kontrollert måte. I dette prosjektet kjøres applikasjonen lokalt under utvikling.

-   Filrettigheter

Filrettigheter er konfigurert slik at applikasjonens filer er beskyttet mot uautorisert tilgang. Kun nødvendige brukere har tilgang til å lese og endre filer, noe som bidrar til økt sikkerhet i løsningen.

-   Miljøvariabler

Konfigurasjonsverdier som databaseinformasjon og andre innstillinger håndteres ved hjelp av miljøvariabler. Dette gjør løsningen mer fleksibel og hindrer at sensitiv informasjon lagres direkte i kildekoden.

------------------------------------------------------------------------

## 4. Prosjektstyring -- GitHub Projects (Kanban)

<img width="823" height="341" alt="image" src="https://github.com/user-attachments/assets/b6ec8320-9a6d-42d1-808a-54beb1e036e0" />


Refleksjon: Hvordan hjalp Kanban arbeidet?
-   Kanban hjalp arbeidet ved å gi god oversikt over oppgavene i prosjektet. Ved å dele arbeidet inn i kolonner som «To do», «Doing» og «Done» ble det lettere å se hva som måtte gjøres, hva som var under arbeid, og hva som allerede var ferdig. Dette gjorde planleggingen mer strukturert og bidro til bedre fremdrift.

Kanban gjorde det også enklere å prioritere oppgaver og jobbe steg for steg i stedet for å gjøre alt samtidig. Når en oppgave var fullført, kunne den flyttes til «Done», noe som ga motivasjon og en tydelig følelse av progresjon. Samlet sett bidro Kanban til bedre organisering, mindre stress og mer effektivt arbeid gjennom hele prosjektet.

------------------------------------------------------------------------

## 5. Databasebeskrivelse

**Databasenavn:**

**Tabeller:**\
\| Tabell \| Felt \| Datatype \| Beskrivelse \|
\|--------\|-------\|-----------\|--------------\| \| customers \| id \|
INT \| Primærnøkkel \| \| customers \| name \| VARCHAR(255) \| Navn \|
\| customers \| address \| VARCHAR(255) \| Adresse \|

**SQL-eksempel:**

``` sql
CREATE TABLE customers (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255),
  address VARCHAR(255)
);
```

------------------------------------------------------------------------

## 6. Programstruktur

    projectnavn/
     ├── app.py
     ├── templates/
     ├── static/
     └── .env

Databasestrøm:

    HTML → Flask → MariaDB → Flask → HTML-tabell

------------------------------------------------------------------------

## 7. Kodeforklaring

Forklar ruter og funksjoner (kort).

------------------------------------------------------------------------

## 8. Sikkerhet og pålitelighet

-   .env\
-   Miljøvariabler\
-   Parameteriserte spørringer\
-   Validering\
-   Feilhåndtering

------------------------------------------------------------------------

## 9. Feilsøking og testing

-   Typiske feil\
-   Hvordan du løste dem\
-   Testmetoder

------------------------------------------------------------------------

## 10. Konklusjon og refleksjon

-   Hva lærte du?\
-   Hva fungerte bra?\
-   Hva ville du gjort annerledes?\
-   Hva var utfordrende?

------------------------------------------------------------------------

## 11. Kildeliste

-   w3schools\
-   flask.palletsprojects.com
