# UI klaidų sąrašas po paskutinių atnaujinimų

1. **Dubliuotas Sidebar meniu**
   - Sidebar rodomas du kartus kairėje pusėje. Tikėtina, kad Sidebar komponentas yra renderinamas tiek layout.js, tiek ChatPage ar kitame wrapper komponente.

2. **Per siauras pagrindinis turinys**
   - Chat kortelė ir turinys yra per siauri, o šoninis meniu užima per daug vietos. Reikia padidinti max-width ir padding pagrindiniam turiniui.

3. **Per daug tamsus fonas ir kontrastingas tekstas**
   - Kortelės ir fonas labai tamsūs, tekstas ryškiai baltas. Reikia sušvelninti spalvas, kad UI būtų malonesnis akiai.

4. **Netinkamas komponentų išdėstymas**
   - Chat kortelė yra per arti šoninio meniu, trūksta „kvėpavimo“ (padding). Reikia padidinti atstumą tarp meniu ir turinio.

5. **Pertekliniai wrapper div arba layout komponentai**
   - Gali būti, kad ChatPage ar kiti puslapiai turi papildomus wrapper div, kurie dubliuoja išdėstymą ir sukelia UI klaidas.

6. **Netinkamas Layout naudojimas kituose puslapiuose**
   - Reikia patikrinti, ar visi puslapiai naudoja tik vieną Layout ir nėra perteklinių Sidebar ar kitų navigacijos komponentų.

---

Kiekviena klaida turi būti ištaisyta, kad UI būtų estetiškas ir tinkamas naudoti.
