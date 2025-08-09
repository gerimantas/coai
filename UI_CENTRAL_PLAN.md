# COAI UI Centralizuoto Dizaino ir Funkcionalumo Planas

## Tikslas
Sukurti modernų, centralizuotai valdomą UI, kad dizaino ir funkcionalumo pakeitimai būtų lengvai pritaikomi visiems puslapiams.

---

## 1. Spalvų ir stilių valdymas
- Sukurti globalų CSS/Tailwind konfigūraciją (`globals.css`, `tailwind.config.js`).
- Apibrėžti pagrindines spalvas, šriftus, border radius, shadow ir kt.
- Naudoti CSS kintamuosius arba Tailwind custom themes.

## 2. UI komponentų biblioteka
- Sukurti bendrų komponentų katalogą: `Button`, `Card`, `Tab`, `StatusBar`, `Loader`, `Alert`, `Sidebar`, `Toolbar`.
- Visi puslapiai naudoja tik šiuos komponentus.
- Komponentai turi aiškias props (pvz., spalva, dydis, variantas).

## 3. Layout ir struktūra
- Sukurti pagrindinį „Layout“ komponentą (`layout.js`).
- Apibrėžti bendrą struktūrą: sidebar, toolbar, statusbar, pagrindinis turinys.
- Visi puslapiai naudoja šį layout.

## 4. Navigacija
- Sukurti `Tab` arba `NavBar` komponentą su aktyvaus tab išskyrimu.
- Navigacijos stilius ir funkcionalumas valdomi per vieną komponentą.

## 5. Dark/Light režimas
- Palaikyti dark/light režimą per Tailwind arba CSS kintamuosius.
- Režimo keitimas paveikia visus komponentus.

## 6. Responsyvumas
- Visi komponentai turi būti responsyvūs.
- Layout automatiškai prisitaiko prie ekrano dydžio.

## 7. Funkcionalumo centralizavimas
- Statuso, pranešimų, loaderių, klaidų rodymas – per bendrus komponentus.
- API užklausos, vartotojo duomenys, projekto informacija – per bendrą kontekstą (`React Context` arba `zustand` store).

## 8. Ikonų ir vizualų naudojimas
- Naudoti bendrą ikonų biblioteką (pvz., Heroicons, FontAwesome).
- Ikonos ir vizualai integruoti į komponentus per props.

## 9. Dokumentacija
- Aprašyti UI komponentų naudojimą, props ir stilių keitimo principus README arba atskirame UI guideline faile.

---

## Veiksmai
1. Sukurti ir sukonfigūruoti globalų stilių failą ir Tailwind temą.
2. Refaktoruoti esamus puslapius, kad naudotų bendrus UI komponentus.
3. Sukurti pagrindinį layout komponentą ir pritaikyti visiems puslapiams.
4. Sukurti ir naudoti bendrus navigacijos, statuso, pranešimų komponentus.
5. Aprašyti ir dokumentuoti UI keitimo principus.

---

## Rezultatas
Bet kokie dizaino ar funkcionalumo pakeitimai bus pritaikomi visam UI centralizuotai ir greitai.
