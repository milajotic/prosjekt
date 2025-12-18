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
<img width="376" height="174" alt="image" src="https://github.com/user-attachments/assets/89f8f8f0-f233-434e-80da-b434d6fd0e03" />

-   Brannmurregler
<img width="375" height="199" alt="image" src="https://github.com/user-attachments/assets/0ca9a786-8de7-45ef-ac13-bcb8c42b3a32" />

Eksempel:

    HTML → Flask → MariaDB → Flask → HTML-tabell

### Tjenestekonfigurasjon

-   systemctl / Supervisor



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

*irisbutikk:*

*Tabeller:*\

<img width="182" height="92" alt="image" src="https://github.com/user-attachments/assets/ca7f6b08-5b1e-4f06-ad72-5fdc4d502a6e" />

Tabell clothes:

<img width="508" height="114" alt="image" src="https://github.com/user-attachments/assets/0a957f84-2dd6-4fe8-bac8-0f8b16d61c7f" />

Tabell bruker:

<img width="512" height="151" alt="image" src="https://github.com/user-attachments/assets/c2394c94-cc13-4492-a8a8-c4a21ce1ab4b" />

Tabell bestilling:

<img width="584" height="108" alt="image" src="https://github.com/user-attachments/assets/4dbcd241-e30f-4739-9a64-211711a9985d" />

**SQL-eksempel:**

``` sql
CREATE TABLE clothes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    navn VARCHAR(50) NOT NULL,
    pris DECIMAL(10,2) NOT NULL,
    beskrivelse TEXT
);
```
Databasen består av tre tabeller: clothes, bruker og bestilling.

- clothes
Inneholder produkter som kan bestilles.
id er primærnøkkel.

- bruker
Inneholder registrerte brukere.
id er primærnøkkel.

- bestilling
Knytter brukere og produkter sammen.
bruker_id refererer til bruker.id
clothes_id refererer til clothes.id
bestillingsdato settes automatisk ved opprettelse.

## Hvordan det fungerer

- En rad i bestilling representerer én bestilling der én bruker bestiller ett produkt.
Dette gjør at én bruker kan ha flere bestillinger, og ett produkt kan bli bestilt av flere brukere.
------------------------------------------------------------------------

## 6. Programstruktur

    PROSJEKT/
     ├── app.py
     ├── templates/
     ├── static/
     └── .env

Databasestrøm:

    HTML → Flask → MariaDB → Flask → HTML-tabell

------------------------------------------------------------------------

## 7. Kodeforklaring

Dette prosjektet er en Flask-basert webapplikasjon som er koblet til en MySQL-database ved hjelp av `get_connection()`.

### Ruter

#### `/`
Viser forsiden (`index.html`).

#### `/clothes`
Henter alle produkter fra `clothes`-tabellen og viser dem på produktsiden.

#### `/add`
Brukes til å legge til nye produkter.
- **GET**: Viser skjema for nytt produkt  
- **POST**: Lagrer produktet i databasen og videresender til `/clothes`

#### `/bestill/<cid>`
Håndterer bestilling av et valgt produkt.
- Viser bestillingsskjema for valgt plagg
- Sjekker om en bruker med gitt e-post allerede finnes
- Oppretter ny bruker hvis ingen finnes
- Oppretter en bestilling som kobler bruker og produkt

#### `/bestill/<cid>/bekreftelse`
Viser en bekreftelsesside for bestillingen.
- Bruker `JOIN` for å hente data fra `bestilling`, `bruker` og `clothes`
- Viser informasjon om bruker, produkt og bestillingsdato

#### `/edit/<cid>`
Henter produktdata og viser skjema for redigering.

#### `/update`
Oppdaterer et eksisterende produkt i databasen.

#### `/delete/<cid>`
Sletter et produkt fra databasen.

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
