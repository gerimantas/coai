# COAI Kūrimo Planas — v4 (Dogfooding Gidas su Copilot)

## Įžanga Vartotojui

Sveiki! Tai yra ketvirtoji COAI projekto kūrimo plano versija, sukurta pagal visiškai naują strategiją. Mes nebekursime COAI tiesiogiai. Vietoj to, mes **naudosime COAI, kad kurtume kitą, testinį projektą**. Kai COAI nesugebės atlikti mūsų komandos, mes sustosime ir patobulinsime patį COAI.

**Kaip mes dirbsime:**

1.  **Jūs esate Klientas ir Programuotojas:** Jūs duosite užduotis COAI sistemai, lyg būtumėte jos klientas. Kai sistema "nemokės" kažko padaryti, jūs tapsite programuotoju ir ją patobulinsite.
2.  **COAI UI yra mūsų Pagrindinis Įrankis:** Visas darbas su testiniu projektu vyks per COAI sąsają.
3.  **VS Code Copilot yra jūsų Meta-Asistentas:** Kai reikės tobulinti patį COAI, mes naudosime Copilot tiesiogiai redaktoriuje, kad pakeistume COAI kodą.

Šis metodas vadinamas "Dogfooding" (valgyti savo paties šunų maistą) – mes patys naudosimės savo produktu, kad rastume jo trūkumus ir jį pagerintume. Tai pats efektyviausias būdas sukurti tikrai naudingą įrankį.

---

## 1 Etapas (Sesija): Testuojame Esamą "Action Plans" Sistemą ir Atskleidžiame Jos Trūkumus

### Etapo Užduotis:

Mūsų tikslas – pabandyti sukurti paprastą komponentą `test-python-project` projekte, naudojant dabartinę COAI "Action Plans" funkciją. Mes tikimės, kad ji sugeneruos labai paprastą ir neefektyvų planą. Tai mums suteiks motyvaciją ir aiškų pagrindą, kodėl reikia ją tobulinti pagal `ACTION_PLANS_OPTIMIZATION_GUIDE.md`.

### Bendra Instrukcija Copilot Agentui (šiai sesijai):

"Veik kaip mano vyresnysis programuotojas-mentorius. Aš bandysiu naudoti COAI aplikaciją, kad sukurčiau komponentą testiniame projekte. Tavo užduotis – padėti man analizuoti COAI atsakymus ir, kai COAI nesusitvarkys, padėti man suformuluoti planą, kaip patobulinti patį COAI kodą."

---

### **Veiksmas 1.1: Užduoties Formulavimas Testiniam Projektui**

*   **Veiksmo Užduotis:** Suformuluoti aiškią, realistišką užduotį, kurią bandysime įvykdyti testiniame projekte.
*   **Komentaras Vartotojui:** Pradėsime kaip tikri COAI vartotojai. Turime projektą (`test-python-project`) ir norime jame sukurti naują funkcionalumą.
*   **Detali Vykdymo Instrukcija:**
    1.  **Pasiruošimas (COAI UI):** Paleiskite COAI. Pagrindiniame lange pasirinkite `test-python-project` kaip aktyvų projektą.
    2.  **Užduoties pateikimas (COAI UI):** Pokalbių lange pateikite AI agentui aiškią užduotį.
*   **Instrukcija COAI Agentui (Promptas):**
    ```
    Sukurk naują "calculator" komponentą `test-python-project` projekte. Komponentas turi būti realizuotas `calculator.py` faile ir turėti tris funkcijas: `add(a, b)`, `subtract(a, b)`, ir `multiply(a, b)`. Taip pat sukurk testavimo failą `test_calculator.py` su `pytest` testais, kurie patikrintų visas tris funkcijas. Sugeneruok veiksmų planą šiai užduočiai įvykdyti.
    ```

### **Veiksmas 1.2: Rezultato Analizė ir Problemos Identifikavimas**

*   **Veiksmo Užduotis:** Kritiškai įvertinti planą, kurį sugeneravo dabartinė COAI versija.
*   **Komentaras Vartotojui:** Tikėtina, kad dabartinė, paprasta sistema sugeneruos vieną bendrą žingsnį, pvz., "1. Create calculator component and tests". Tai yra neefektyvu. Mums reikia detalaus plano. Čia ir slypi galimybė tobulėjimui.
*   **Detali Vykdymo Instrukcija:**
    1.  **Analizė:** Atidžiai išnagrinėkite COAI sugeneruotą veiksmų planą.
    2.  **Problemos fiksavimas (Pokalbis su VS Code Copilot):** Dabar pereikite į VS Code redaktorių. Atidarykite Copilot Chat ir aprašykite jam situaciją.
*   **Instrukcija VS Code Copilot (Promptas):**
    ```
    Aš daviau COAI agentui užduotį sukurti kalkuliatoriaus komponentą ir testus. Jis sugeneravo labai bendrą, vieno žingsnio planą. Tai neefektyvu. Remiantis `ACTION_PLANS_OPTIMIZATION_GUIDE.md`, ką turėtume pakeisti COAI `backend` sistemoje, kad ji galėtų išskaidyti tokią užduotį į detalius žingsnius (pvz., "1. Create `calculator.py` file", "2. Add `add` function", "3. Create `test_calculator.py` file", etc.)? Pateik aukšto lygio pakeitimų planą.
    ```

### **Veiksmas 1.3: Perėjimas į Meta-Lygį: COAI Kodo Tobulinimo Planavimas**

*   **Veiksmo Užduotis:** Remiantis Copilot atsakymu, suformuoti konkretų techninį planą, kaip patobulinsime patį COAI.
*   **Komentaras Vartotojui:** Dabar mes oficialiai "sustabdome" darbą su testiniu projektu ir tampame COAI programuotojais. Mūsų tikslas – įgyvendinti funkcionalumą, kurio mums prireikė 1.2 žingsnyje.
*   **Detali Vykdymo Instrukcija:**
    1.  **Plano detalizavimas (Pokalbis su VS Code Copilot):** Tęskite pokalbį su Copilot.
*   **Instrukcija VS Code Copilot (Promptas):**
    ```
    Gerai, tavo pasiūlytas planas tinka. Dabar išskaidykime pirmąją dalį – "Backend task generation with keyword analysis" – į konkrečius, nuoseklius techninius veiksmus. Kiekvienam veiksmui nurodyk, kokį failą reikia sukurti ar modifikuoti. Pradėkime nuo modulio, kuris analizuos vartotojo užklausą.
    ```

### **Veiksmas 1.4: Techninės Užduoties Įgyvendinimas (Pagal ankstesnį planą)**

*   **Veiksmo Užduotis:** Įgyvendinti techninį planą, kurį sugeneravo Copilot (sukurti `RequestAnalyzer`, `TemplateLoader`, atnaujinti `Orchestrator` ir parašyti testus).
*   **Komentaras Vartotojui:** Ši dalis atitinka ankstesnio plano (v3) techninius žingsnius. Jūs, kartu su Copilot, kuriate naujus modulius, rašote testus ir atnaujinate Orkestratorių tiesiogiai VS Code redaktoriuje.
*   **Detali Vykdymo Instrukcija:**
    1.  Sistemingai vykdykite Copilot sugeneruotą techninį planą, nuolat testuodami pakeitimus su `pytest backend/`.

### **Veiksmas 1.5: Grįžimas prie Pradinės Užduoties ir Patvirtinimas**

*   **Veiksmo Užduotis:** Pakartoti 1.1 žingsnį ir patikrinti, ar dabar COAI sugeneruoja geresnį planą.
*   **Komentaras Vartotojui:** Tai yra "sėkmės ratas". Patobulinę įrankį, grįžtame prie pradinės problemos ir žiūrime, ar ją išsprendėme.
*   **Detali Vykdymo Instrukcija:**
    1.  **Git dokumentacija (Jūsų veiksmas):** Įtvirtinkite atliktus COAI pakeitimus su `git commit`.
    2.  **Serverio perkrovimas (Jūsų veiksmas):** Perkraukite COAI backend serverį, kad pakeitimai įsigaliotų.
    3.  **Pakartotinis testas (COAI UI):** Grįžkite į COAI sąsają, vėl pasirinkite `test-python-project` ir pateikite lygiai tą pačią užduotį iš 1.1 veiksmo.
    4.  **Analizė:** Palyginkite naujai sugeneruotą planą su pirmuoju. Dabar jis turėtų būti detalus, išskaidytas į loginius žingsnius pagal jūsų sukurtus šablonus. Jei taip, jūs sėkmingai užbaigėte pirmąjį etapą!

---
**Pirmojo Etapo Apibendrinimas:** Jūs ne tik patobulinote COAI, bet ir išmokote patį svarbiausią produkto vystymo principą: realūs vartotojo poreikiai turi diktuoti kūrimo procesą. Jūs susidūrėte su problema, identifikavote jos priežastį ir sistemingai ją pašalinote.

**Kitame etape mes imsimės šio detalaus plano vykdymo per COAI UI ir žiūrėsime, su kokiais naujais iššūkiais susidursime.**