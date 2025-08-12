# Puslapio išdėstymo problemos sprendimo veiksmų planas

1. Aiškiai atskirti atsakomybę: layout.js valdo globalų išdėstymą, PageContainer – tik modalų stilių.
2. Pašalinti max-width, centrinimą ir padding iš PageContainer komponento.
3. Pridėti `mx-auto`, `max-w-4xl`, `px-6`, `py-8`, `mt-8` į layout.js vidinį wrapper’į.
4. Patikrinti, kad visi puslapiai nenaudoja papildomų margin/padding ar wrapper’io sluoksnių.
5. Suderinti PageContainer antraštės (`title`) stilių, kad būtų nuoseklus margin-bottom, font-size, spalva.
6. Testuoti UI visuose puslapiuose, kad modalai būtų centre ir su vienodais tarpais nuo kraštų.
7. Vadovautis Next.js ir Tailwind CSS dokumentacija: layout komponentas valdo išdėstymą, PageContainer – modalų turinį.
8. Dokumentuoti architektūrinį sprendimą, kad ateityje būtų laikomasi šios struktūros.
