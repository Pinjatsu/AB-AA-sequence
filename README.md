# Vasta-aineiden CDR looppien sekvenssit

Ensimmäinen käytännön pythonprojekti :)
Koulutehtävää varten piti kerätä gevokizumab vasta-aineen CDR looppien aminohapposekvenssit tekstitiedostosta, joka näytti tältä:

![image](https://github.com/user-attachments/assets/b53c44b8-94b4-4b8c-83dd-1a2091020d7b)

Ensimmäisessä versiossa etsittiin Kabat numeroinnista H1-loopin sekvenssi ja output haluttiin auki kirjoitettuna (eli TSGMGVG). For loop suoritettiin etsimään rivit H31-H35B. Löydetyistä riveistä tehtiin lista, josta poistettiin kaikki muu tieto paitsi aminohapon nimi ja listan alkioiden väleistä poistettiin välilyönnit, jotta saatiin sekvenssi toivottuun ulkoasuun.
