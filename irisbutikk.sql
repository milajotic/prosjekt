CREATE DATABASE irisbutikk;

USE irisbutikk;

--Opprett bruker med epost som primærnøkkel
CREATE TABLE bruker (
    id INT AUTO_INCREMENT PRIMARY KEY,
    epost VARCHAR(100) UNIQUE,
    fornavn VARCHAR(50) NOT NULL,
    etternavn VARCHAR(50) NOT NULL,
    telefonnummer VARCHAR(15),
    adresse VARCHAR(100),
    passord VARCHAR(100)
);

CREATE TABLE clothes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    navn VARCHAR(50) NOT NULL,
    pris DECIMAL(10,2) NOT NULL,
    beskrivelse TEXT
);

--Opprett bestilling med id nummer som primærnækkel
CREATE TABLE bestilling (
    id INT AUTO_INCREMENT PRIMARY KEY,
    bruker_id INT NOT NULL,
    clothes_id INT NOT NULL,
    bestillingsdato TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (bruker_id) REFERENCES bruker(id),
    FOREIGN KEY (clothes_id) REFERENCES clothes(id)
);