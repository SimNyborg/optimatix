# 🎨 Farvevejledning - Datara

## Hurtig Farveændring

For at ændre farverne på hele hjemmesiden, åbn `static/style.css` og find sektionen øverst med CSS-variabler.

### Nuværende Farver (Standard)
```css
:root {
    --primary-color: #4a5cff;           /* Blå hovedfarve */
    --primary-dark: #222831;            /* Mørkere blå */
    --primary-light: #f8f9ff;           /* Lysere blå */
    --secondary-color: #f39c12;         /* Orange sekundærfarve */
    --accent-color: #222;               /* Mørk accentfarve */
    --text-primary: #222;               /* Hovedtekst */
    --text-secondary: #444;             /* Sekundær tekst */
    --text-light: #666;                 /* Lys tekst */
    --text-white: #fff;                 /* Hvid tekst */
    --bg-primary: #fff;                 /* Hovedbaggrund */
    --bg-secondary: #fafbfc;            /* Sekundær baggrund */
    --bg-light: #f8f9ff;                /* Lys baggrund */
    --border-color: #e0e0e0;            /* Border farve */
    --shadow-color: rgba(0,0,0,0.07);   /* Skygge farve */
    --shadow-hover: rgba(0,0,0,0.13);   /* Hover skygge farve */
    --gradient-start: #4a5cff;          /* Gradient start */
    --gradient-end: #222831;            /* Gradient slut */
}
```

## 🚀 Foruddefinerede Farveteamer

### Blå Tema
Fjern `/*` og `*/` fra denne sektion for at aktivere blåt tema:
```css
:root {
    --primary-color: #2563eb;
    --primary-dark: #1e40af;
    --primary-light: #eff6ff;
    --secondary-color: #3b82f6;
    --accent-color: #1f2937;
    --text-primary: #1f2937;
    --text-secondary: #374151;
    --text-light: #6b7280;
    --text-white: #ffffff;
    --bg-primary: #ffffff;
    --bg-secondary: #f9fafb;
    --bg-light: #eff6ff;
    --border-color: #e5e7eb;
    --shadow-color: rgba(0,0,0,0.07);
    --shadow-hover: rgba(0,0,0,0.13);
    --gradient-start: #2563eb;
    --gradient-end: #1e40af;
}
```

### Grøn Tema
Fjern `/*` og `*/` fra denne sektion for at aktivere grønt tema:
```css
:root {
    --primary-color: #059669;
    --primary-dark: #047857;
    --primary-light: #ecfdf5;
    --secondary-color: #10b981;
    --accent-color: #064e3b;
    --text-primary: #064e3b;
    --text-secondary: #065f46;
    --text-light: #6b7280;
    --text-white: #ffffff;
    --bg-primary: #ffffff;
    --bg-secondary: #f9fafb;
    --bg-light: #ecfdf5;
    --border-color: #e5e7eb;
    --shadow-color: rgba(0,0,0,0.07);
    --shadow-hover: rgba(0,0,0,0.13);
    --gradient-start: #059669;
    --gradient-end: #047857;
}
```

### Lilla Tema
Fjern `/*` og `*/` fra denne sektion for at aktivere lilla tema:
```css
:root {
    --primary-color: #7c3aed;
    --primary-dark: #5b21b6;
    --primary-light: #f3f4f6;
    --secondary-color: #8b5cf6;
    --accent-color: #2e1065;
    --text-primary: #2e1065;
    --text-secondary: #4c1d95;
    --text-light: #6b7280;
    --text-white: #ffffff;
    --bg-primary: #ffffff;
    --bg-secondary: #f9fafb;
    --bg-light: #f3f4f6;
    --border-color: #e5e7eb;
    --shadow-color: rgba(0,0,0,0.07);
    --shadow-hover: rgba(0,0,0,0.13);
    --gradient-start: #7c3aed;
    --gradient-end: #5b21b6;
}
```

### Rød Tema
Fjern `/*` og `*/` fra denne sektion for at aktivere rødt tema:
```css
:root {
    --primary-color: #dc2626;
    --primary-dark: #991b1b;
    --primary-light: #fef2f2;
    --secondary-color: #ef4444;
    --accent-color: #450a0a;
    --text-primary: #450a0a;
    --text-secondary: #7f1d1d;
    --text-light: #6b7280;
    --text-white: #ffffff;
    --bg-primary: #ffffff;
    --bg-secondary: #f9fafb;
    --bg-light: #fef2f2;
    --border-color: #e5e7eb;
    --shadow-color: rgba(0,0,0,0.07);
    --shadow-hover: rgba(0,0,0,0.13);
    --gradient-start: #dc2626;
    --gradient-end: #991b1b;
}
```

## 🎯 Sådan Skifter Du Farver

1. **Åbn** `static/style.css`
2. **Find** sektionen øverst med `:root {`
3. **Kommenter ud** det ønskede tema ved at fjerne `/*` og `*/`
4. **Kommenter ind** det nuværende tema ved at tilføje `/*` og `*/`
5. **Gem** filen og genindlæs siden

## 🎨 Skræddersyede Farver

Du kan også oprette dit eget farveteam ved at ændre værdierne i `:root` sektionen:

```css
:root {
    --primary-color: #din-farve;        /* Din hovedfarve */
    --primary-dark: #din-mørke-farve;   /* Mørkere version */
    --primary-light: #din-lys-farve;    /* Lysere version */
    /* ... osv. */
}
```

## 📱 Hvad Ændres

Disse farver påvirker:
- ✅ Knapper og links
- ✅ Baggrunde og kort
- ✅ Tekstfarver
- ✅ Hover-effekter
- ✅ Gradienter
- ✅ Skygger og borders
- ✅ Alle servicesider
- ✅ Footer og navigation

## 🔄 Eksempel på Hurtig Skift

For at skifte til blåt tema:
1. Find `/* Blå tema */` sektionen
2. Fjern `/*` fra start og `*/` fra slut
3. Tilføj `/*` og `*/` omkring den nuværende `:root` sektion
4. Gem og genindlæs

**Resultat:** Hele hjemmesiden skifter til blåt tema med ét klik! 🚀 