# 🧪 COAI UI Testavimo Vadovas
**Serveriai:** Backend (http://localhost:5000) + Frontend (http://localhost:3000)

## 📋 **1. PRADINIS PATIKRINIMAS**

### **1.1 Atidaryti COAI sistemą:**
- Eiti į: **http://localhost:3000**
- Turėtumėte matyti COAI Dashboard su sidebar navigacija

### **1.2 Patikrinti navigacijos meniu:**
✅ **CREATE sekcija:**
- New Project
- Action Plans ← (naujas funkcionalumas!)

✅ **ANALYZE sekcija:**
- Chat Interface
- Usage Analytics ← (naujas!)

✅ **SETTINGS sekcija:**
- Project Settings
- Rules Management

---

## 💬 **2. CHAT INTERFACE TESTAVIMAS**

### **2.1 Eiti į Chat Interface:**
- Sidebar → Chat Interface
- Turėtumėte matyti chat langą su input lauku

### **2.2 Testuoti AI integracijos:**

**Test 1: Basic Chat**
```
Įrašyti: "Hello! Can you help me debug Python code?"
Tikėtinas rezultatas: AI atsako su helpful response
```

**Test 2: Code Review**
```
Įrašyti: "Please review this Python function: 
def calculate(a, b):
    return a + b"
Tikėtinas rezultatas: AI pateiks code review komentarus
```

**Test 3: Project Context**
```
Įrašyti: "What files are in this project?"
Tikėtinas rezultatas: AI nuskaito ir aprašo projekto failus
```

### **2.3 Patikrinti response metadata:**
- Žiūrėti ar atsako greitai (< 2s)
- Patikrinti ar nėra error pranešimų
- Matyti usage tracking informaciją

---

## 📊 **3. USAGE ANALYTICS TESTAVIMAS**

### **3.1 Eiti į Usage Analytics:**
- Sidebar → Usage Analytics
- Turėtumėte matyti analytics dashboard

### **3.2 Patikrinti duomenis:**
✅ **Statistics Cards:**
- Total Requests
- Total Cost
- Average Response Time
- Most Used Agent

✅ **Charts/Graphs:**
- Daily usage trends
- Cost breakdown
- Request distribution

✅ **Export funkcionalumas:**
- Export to JSON/CSV mygtukas
- Download functionality

### **3.3 Testuoti real-time tracking:**
- Grįžti į Chat
- Padaryti kelias užklausas
- Grįžti į Analytics
- Patikrinti ar statistikos atsinaujino

---

## 📋 **4. ACTION PLANS TESTAVIMAS**

### **4.1 Eiti į Action Plans:**
- Sidebar → Action Plans (CREATE sekcijoje)
- Turėtumėte matyti Action Plans puslapį

### **4.2 Sukurti naują Action Plan:**

**Test Input:**
```
Goal: "Optimize COAI performance and add new features"
```

**Tikėtinas rezultatas:**
- AI sugeneruoja structured action plan
- Matyti tasks su priorities
- Estimated time information
- Task dependencies

### **4.3 Patikrinti plan management:**
- View existing plans
- Task status updates
- Progress tracking

---

## ⚙️ **5. RULES MANAGEMENT TESTAVIMAS**

### **5.1 Eiti į Rules Management:**
- Sidebar → Rules Management
- Turėtumėte matyti rules editor

### **5.2 Testuoti rules funkcionalumą:**
- View current rules
- Edit rules content
- Save changes
- Reload rules

### **5.3 Patikrinti rule validation:**
- Bandyti įrašyti invalid rules
- Patikrinti validation messages
- Backup/restore funkcionalumą

---

## 🔒 **6. SECURITY & PERFORMANCE TESTAVIMAS**

### **6.1 Rate Limiting Test:**
- Greitai padaryti daug chat requests
- Patikrinti ar sistema blokuoja per dažnus requests
- Matyti rate limit warnings

### **6.2 Error Handling Test:**
- Bandyti ilgą message (>10000 characters)
- Bandyti empty message
- Patikrinti ar error messages aiškūs

### **6.3 Performance Test:**
- Matuoti response times
- Patikrinti caching (kartoti tas pačias užklausas)
- Monitoring memory usage

---

## 🎯 **7. END-TO-END WORKFLOW TEST**

### **Complete User Journey:**

**Step 1:** Sukurti Action Plan
```
Goal: "Build a Python calculator app"
```

**Step 2:** Naudoti Chat Interface
```
Message: "Help me implement the calculator from my action plan"
```

**Step 3:** Patikrinti Analytics
- Matyti naują usage data
- Export statistics

**Step 4:** Update Rules
- Pridėti specific coding guidelines
- Test ar AI laikosi naujų rules

**Step 5:** Verify Integration
- Viskas veikia sklandžiai
- No errors ar crashes

---

## ✅ **SUCCESS CRITERIA:**

### **Must Work:**
- [ ] Chat produces AI responses
- [ ] Analytics shows usage data
- [ ] Action Plans generated
- [ ] No critical errors

### **Should Work:**
- [ ] Real-time updates
- [ ] Export functionality
- [ ] Rule modifications
- [ ] Performance optimal

### **Nice to Have:**
- [ ] Advanced analytics
- [ ] Complex action plans
- [ ] Custom rules working
- [ ] Professional UI/UX

---

## 🚨 **COMMON ISSUES & SOLUTIONS:**

### **Problem: No AI Response**
- Patikrinti backend logs
- **CRITICAL: Verify real OpenAI API key configured**
- Check backend/.env: OPENAI_API_KEY=sk-proj-... (not demo key)
- **Ensure ENABLE_REAL_AI=true in .env file**
- Set FALLBACK_TO_MOCK=false
- Run: `python backend/test_openai_key.py` to validate
- Restart backend server after changes

### **Problem: Demo Responses Only**
- 🔑 **Replace demo key with real OpenAI key**
- Edit `backend/.env`:
  - Line 4: OPENAI_API_KEY=your-real-key
  - Line 9: ENABLE_REAL_AI=true  
  - Line 12: FALLBACK_TO_MOCK=false
- Restart backend server
- Verify with: `python backend/test_openai_key.py`

### **Problem: Analytics Empty**
- Padaryti chat requests
- Wait for tracking updates
- Check usage_tracker.py logs

### **Problem: Slow Performance**
- Check caching working
- Monitor network requests
- Verify backend not overloaded

### **Problem: UI Not Loading**
- Clear browser cache
- Check console errors
- Restart frontend server

---

## 🎉 **FINAL VALIDATION:**

Jei visi testai praeina ✅, tai **COAI sistema yra production-ready!**

Sistema sėkmingai transformuota iš demo į enterprise-grade AI development platform! 🚀
