# Vasta-aineen CDR looppien sekvenssit

Ensimmäinen käytännön pythonprojekti :)
Koulutehtävää varten piti kerätä gevokizumab vasta-aineen (4G6K) CDR looppien aminohapposekvenssit tekstitiedostosta, joka näytti tältä:

![image](https://github.com/user-attachments/assets/b53c44b8-94b4-4b8c-83dd-1a2091020d7b)

Ensimmäisessä versiossa etsittiin Kabat numeroinnista H1-loopin sekvenssi ja output haluttiin auki kirjoitettuna (eli TSGMGVG). For loop suoritettiin etsimään rivit H31-H35B. Löydetyistä riveistä tehtiin lista, josta poistettiin kaikki muu tieto paitsi aminohapon nimi ja listan alkioiden väleistä poistettiin välilyönnit, jotta saatiin sekvenssi toivottuun ulkoasuun.

Päivitetyssä versiossa koodi hakee kolmen eri numeroinnin (Kabat, Martin ja Chothia) mukaiset raskasketjun CDR looppien aminohapposekvenssit.

## Käyttöohjeet

Tämä projekti lukee kolmen eri numerointijärjestelmän (Kabat, Martin, Chothia) mukaiset raskasketjun CDR loop sekvenssit tekstitiedostoista ja tulostaa ne.

### Tiedostot

- `kabat_input.txt`: Kabat numerointi
- `martin_input.txt`: Martin numerointi
- `chothia_input.txt`: Chothia numerointi

### Python-koodi

Koodi löytyy tiedostosta `CDR loop sequences.py`. Se sisältää funktiot, jotka lukevat sekvenssitiedostot ja tulostavat raskasketjun CDR loop sekvenssit.

### Suoritus

Voit suorittaa koodin seuraavasti:

```sh
python "CDR loop sequences.py"