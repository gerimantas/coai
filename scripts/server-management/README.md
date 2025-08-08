# COAI Server Management Scripts

Šiame aplanke yra visi reikalingi COAI serverių valdymo skriptai.

## 📋 Failų sąrašas

### 🚀 Serverių paleidimas
- **`start-servers.bat`** - Paleidžia abu serverius (frontend + backend)
  - Tikrina dependencies
  - Diegia trūkstamas priklausomybes
  - Paleidžia atskiruose languose
  - Laukia kol serveriai pasileis
  - Rodo statusą

### 🔄 Serverių perkrovimas  
- **`restart-servers.bat`** - Perkrauna serverius (stop + start)
  - Pirmiau švelniai sustabdo
  - Jei nepavyksta - priverstinai
  - Laukia 3 sekundes
  - Paleidžia iš naujo

### ⏹️ Serverių sustabdymas
- **`graceful-stop.bat`** - Švelniai sustabdo serverius
  - Bando API shutdown (jei palaikoma)
  - Švelniai sustabdo procesus
  - Jei nepavyksta - informuoja
  
- **`kill-servers.bat`** - Priverstinai sustabdo visus serverius
  - Sustabdo visus Node.js procesus
  - Sustabdo visus Python procesus
  - Nenaudoti tik kraštutiniais atvejais

### 📊 Serverių stebėjimas
- **`check-servers.bat`** - Tikrina serverių būseną
  - HTTP endpoint tikrinimas
  - Port tikrinimas
  - Proceso tikrinimas
  
- **`ps-check.bat`** - Rodo aktyvius procesus
  - Node.js procesų sąrašas
  - Python procesų sąrašas
  - Port listening būsena

## 🔧 Naudojimo instrukcijos

### Pirmas paleidimas
```bash
# 1. Paleisti serverius
start-servers.bat

# 2. Patikrinti ar veikia
check-servers.bat
```

### Kasdieninis naudojimas
```bash
# Paleidimas
start-servers.bat

# Tikrinimas
check-servers.bat

# Perkrovimas (jei reikia)
restart-servers.bat

# Sustabdymas (darbo pabaigoje)
graceful-stop.bat
```

### Problemos sprendimas
```bash
# Jei serveriai neklauso
ps-check.bat

# Jei reikia priverstinai sustabdyti
kill-servers.bat

# Perkrovimas po problemų
restart-servers.bat
```

## 🌐 Serverių adresai

- **Frontend**: http://localhost:3000
- **Backend**: http://localhost:5000

## ⚠️ Pastabos

1. **Dependencies**: Skriptai automatiškai diegs trūkstamas priklausomybes
2. **Windows**: Skriptai optimizuoti Windows aplinkai
3. **Portai**: Jei portai užimti - skriptai perspės
4. **Languose**: Serveriai paleidžiami atskiruose cmd languose
5. **UTF-8**: Palaikomi lietuviški simboliai

## 🔍 Troubleshooting

### Port jau užimtas
```bash
# Patikrinti kas naudoja portą
netstat -ano | findstr :3000
netstat -ano | findstr :5000

# Sustabdyti procesą pagal PID
taskkill /pid <PID> /f
```

### Dependencies trūksta
```bash
# Root level
npm install

# Frontend
cd frontend && npm install

# Backend  
cd backend && pip install -r requirements.txt
```

### Serveriai neatsako
```bash
# Pilnas restart
kill-servers.bat
start-servers.bat
```
