# COAI AGENTŲ ROLIŲ SĄRAŠAS
## Reikalingi AI Agentai COAI Sistemai

*Sukurta: August 16, 2025*  
*Pagal COAI Development Plan v3*

---

## CORE AGENTS (Būtini)

### **1. Orchestrator**
**Paskirtis:** Centrinis koordinatorius
**Funkcijos:**
- Request analizė ir maršrutizavimas
- Agent selection logic
- Multi-agent workflow koordinavimas
- Context preservation tarp agent'ų
- Response synthesis
- Error handling ir fallback

**LLM:** GPT-4 Turbo (API) arba Local Mixtral 8x22B

---

### **2. CodeAssistAgent**
**Paskirtis:** Greita kodo pagalba
**Funkcijos:**
- Code completion suggestions
- Syntax error fixes
- Quick implementation help
- Basic debugging hints
- Common patterns suggestions
- Simple refactoring

**LLM:** GPT-3.5 Turbo (API) arba Local Code Llama 13B

---

### **3. DebugAgent**
**Paskirtis:** Klaidų analizė ir debugging
**Funkcijos:**
- Error message analysis
- Stack trace interpretation
- Bug identification
- Root cause analysis
- Debugging strategy recommendations
- Performance bottleneck detection

**LLM:** Claude-3 Sonnet (API) arba Local Mixtral 8x7B

---

## SPECIALIZED AGENTS (Pažengę)

### **4. ReviewAgent**
**Paskirtis:** Kodo kokybės vertinimas
**Funkcijos:**
- Code quality assessment
- Security vulnerability scanning
- Best practices validation
- Performance optimization suggestions
- Architecture compliance check
- Testing adequacy evaluation

**LLM:** GPT-4o (API) arba Local DeepSeek Coder 33B

---

### **5. ArchitectAgent**
**Paskirtis:** Sistemos architektūros konsultavimas
**Funkcijos:**
- System architecture design
- Technology stack recommendations
- Scalability planning
- Integration patterns advice
- Design patterns guidance
- Architectural refactoring

**LLM:** Claude-3 Opus (API) arba Local Mixtral 8x22B

---

### **6. DocumentAgent**
**Paskirtis:** Dokumentacijos generavimas
**Funkcijos:**
- API documentation generation
- User guide creation
- Code commenting
- Technical specifications
- Tutorial creation
- README generation

**LLM:** GPT-4 Turbo (API) arba Local Mixtral 8x7B

---

## ADVANCED AGENTS (Perspektyviai)

### **7. TestAgent**
**Paskirtis:** Testų kūrimas ir strategija
**Funkcijos:**
- Unit test generation
- Integration test scenarios
- Test strategy planning
- Mock data creation
- Test coverage analysis
- Testing best practices

**LLM:** GPT-4 (API) arba Local Code Llama 34B

---

### **8. SecurityAgent**
**Paskirtis:** Saugumo analizė
**Funkcijos:**
- Security vulnerability detection
- Penetration testing guidance
- Secure coding practices
- Authentication/authorization review
- Data protection compliance
- Security architecture review

**LLM:** Claude-3 Sonnet (API) arba Local Mixtral 8x7B

---

### **9. PerformanceAgent**
**Paskirtis:** Performance optimization
**Funkcijos:**
- Performance bottleneck identification
- Code optimization suggestions
- Database query optimization
- Memory usage analysis
- Caching strategies
- Load testing guidance

**LLM:** GPT-4 (API) arba Local DeepSeek Coder

---

### **10. RefactorAgent**
**Paskirtis:** Kodo refaktoringas
**Funkcijos:**
- Code structure improvement
- Design pattern implementation
- Legacy code modernization
- Code duplication elimination
- Naming convention fixes
- Architecture migration

**LLM:** Claude-3 Opus (API) arba Local Code Llama 34B

---

## DOMAIN-SPECIFIC AGENTS (Specializuoti)

### **11. WebDevAgent**
**Paskirtis:** Web development specialistas
**Funkcijos:**
- Frontend framework guidance
- Backend API design
- Database schema design
- Web security best practices
- Performance optimization
- Deployment strategies

**LLM:** GPT-4 (API) arba Local Mixtral

---

### **12. DataAgent**
**Paskirtis:** Data science ir analytics
**Funkcijos:**
- Data analysis strategies
- Machine learning guidance
- Data visualization recommendations
- ETL pipeline design
- Statistical analysis
- Data quality assessment

**LLM:** Claude-3 Sonnet (API) arba Local Code Llama

---

### **13. DevOpsAgent**
**Paskirtis:** DevOps ir deployment
**Funkcijos:**
- CI/CD pipeline design
- Infrastructure as Code
- Container orchestration
- Monitoring and logging
- Deployment strategies
- Cloud platform guidance

**LLM:** GPT-4 (API) arba Local Mixtral

---

## PRIORITY IMPLEMENTATION ORDER

### **PHASE 1 - MVP (Būtini agentai)**
1. **Orchestrator** - centrinis koordinatorius
2. **CodeAssistAgent** - basic kodo pagalba
3. **DebugAgent** - error analysis

### **PHASE 2 - Core Functionality**
4. **ReviewAgent** - code quality
5. **ArchitectAgent** - system design
6. **DocumentAgent** - documentation

### **PHASE 3 - Advanced Features**
7. **TestAgent** - testing support
8. **SecurityAgent** - security analysis
9. **PerformanceAgent** - optimization

### **PHASE 4 - Specialization**
10. **RefactorAgent** - code improvement
11. **WebDevAgent** - web development
12. **DataAgent** - data science
13. **DevOpsAgent** - deployment

---

## AGENT INTERACTION PATTERNS

### **Single Agent Tasks**
- Simple code questions → CodeAssistAgent
- Bug reports → DebugAgent
- Documentation requests → DocumentAgent

### **Multi-Agent Workflows**
```
Complex Performance Issue:
1. DebugAgent → identify bottlenecks
2. PerformanceAgent → optimization strategies  
3. ReviewAgent → validate improvements
4. TestAgent → create performance tests
```

### **Collaborative Scenarios**
```
New Feature Development:
1. ArchitectAgent → design approach
2. CodeAssistAgent → implementation help
3. TestAgent → test strategy
4. SecurityAgent → security review
5. DocumentAgent → documentation
```

---

## CONFIGURATION FLEXIBILITY

### **Deployment Options**
- **Cloud-only:** Visi agentai naudoja API keys
- **Hybrid:** Core agents cloud, specialized local
- **Local-only:** Visi agentai local LLM

### **Cost Optimization**
- **Tier 1:** GPT-3.5 / Local Code Llama (cheap, fast)
- **Tier 2:** GPT-4 / Claude Sonnet (balanced)
- **Tier 3:** GPT-4o / Claude Opus (premium, complex)

### **Privacy Levels**
- **Public:** Cloud LLM, bet kuris kodas
- **Sensitive:** Local LLM tik, cloud basic tasks
- **Confidential:** Tik local LLM

---

## MINIMALI AGENT KONFIGŪRACIJA (MVP)

Pradžiai užtenka **3 core agents**:

1. **Orchestrator** - request routing
2. **CodeAssistAgent** - basic help  
3. **DebugAgent** - error analysis

Šie 3 agentai gali padengti 80% basic developer needs ir leisti sistemai veikti production environment.

---

*Šis sąrašas yra scalable - galima pridėti specialistus pagal poreikį, nepažeidžiant core sistemos.*
