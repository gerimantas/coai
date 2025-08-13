# Copilot Instructions — SESSION_ACTION_PLAN Implementation

## Objective
Execute the SESSION_ACTION_PLAN.md to transform COAI from demo/stub to production-ready system with real AI integration. Follow the 6-stage approach systematically.

## Context
- Current state: COAI MVP completed, Stage II partially done
- Goal: Real AI integration, production-ready features
- Duration: 1 intensive session (3-4 hours)
- Focus: Practical implementation over theoretical planning

## Pre-Session Setup
1. **Environment Check:**
   ```bash
   cd C:\ai_projects\coai
   # Verify servers are running
   npm run dev  # Should start both frontend and backend
   ```

2. **Backup Current State:**
   ```bash
   git add .
   git commit -m "Pre-session backup - stable MVP state"
   git tag v1.0-mvp
   ```

3. **API Keys Preparation:**
   - Obtain OpenAI API key (test account sufficient)
   - Create `.env` file in backend directory
   - Verify GitHub token if using Copilot integration

## Stage-by-Stage Execution

### STAGE 1: AI Agents Activation (30 min)
**Priority: CRITICAL - Foundation for all other stages**

1. **Analyze existing AI implementation:**
   ```bash
   # Review what's already built
   code backend/app/ai_agents_full.py
   code backend/app/ai_agents.py
   code backend/app/routes.py  # Find OrchestratorStub usage
   ```

2. **Create environment configuration:**
   ```bash
   # Create .env file
   echo "OPENAI_API_KEY=your_key_here" > backend/.env
   echo "DEFAULT_AI_AGENT=openai" >> backend/.env
   ```

3. **Replace stub with real implementation:**
   - Edit `backend/app/routes.py`
   - Replace `OrchestratorStub` with real orchestrator
   - Import proper AI agents module

4. **Test basic AI integration:**
   ```bash
   # Start servers and test chat endpoint
   curl -X POST http://localhost:5000/api/chat \
     -H "Content-Type: application/json" \
     -d '{"message":"Hello, can you help me debug Python code?","project":"test","file":"main.py"}'
   ```

### STAGE 2: Practical Functionality Testing (45 min)
**Priority: HIGH - Real-world validation**

1. **Create test project structure:**
   ```bash
   mkdir C:\ai_projects\test-python-project
   # Create sample Python files with bugs/issues
   # Test code review, debugging assistance
   ```

2. **Test real scenarios:**
   - Code review requests
   - Bug fixing assistance  
   - Documentation generation
   - Multi-file context understanding

3. **Implement robust error handling:**
   - API failures gracefully handled
   - User-friendly error messages
   - Fallback to simulation if needed
   - Error logging to `.coai/logs/`

### STAGE 3: Usage Analytics Implementation (40 min)
**Priority: MEDIUM - Production readiness**

1. **Create UsageTracker class:**
   ```python
   # backend/app/usage_tracker.py
   class UsageTracker:
       def track_request(self, agent, tokens, cost, project):
           # Implement tracking logic
   ```

2. **Integrate with orchestrator:**
   - Track API calls in real-time
   - Store data in `.coai/usage/`
   - Calculate costs per request

3. **Build frontend usage dashboard:**
   - Create `/usage` page
   - Display charts and statistics
   - Export functionality

### STAGE 4: Advanced Features (45 min)
**Priority: MEDIUM - Enhancement**

1. **Production-ready rules system:**
   - Rules validation and versioning
   - Per-project rule overrides
   - Backup/restore functionality

2. **Action plan generation:**
   - AI-powered task breakdown
   - Step-by-step planning UI
   - Integration with progress tracking

### STAGE 5: Performance & Security (30 min)
**Priority: HIGH - Stability**

1. **Performance optimization:**
   - Request caching mechanism
   - Async processing where appropriate
   - Loading states in UI

2. **Security hardening:**
   - File access validation
   - Rate limiting implementation
   - API key encryption
   - Security audit logging

### STAGE 6: Integration Testing (30 min)
**Priority: CRITICAL - Validation**

1. **End-to-end testing:**
   - Complete chat workflow with real AI
   - Project switching functionality
   - Rules editing and application
   - Error scenario handling

2. **Documentation updates:**
   - README with real usage examples
   - API documentation
   - Configuration guide
   - Troubleshooting section

## Implementation Guidelines

### **Code Quality Standards:**
- Follow existing code patterns
- Add comprehensive error handling
- Include logging for debugging
- Write self-documenting code

### **Testing Approach:**
- Test after each major change
- Use real scenarios, not toy examples
- Validate both success and failure paths
- Keep fallback mechanisms working

### **Git Workflow:**
```bash
# After each stage:
git add .
git commit -m "Stage X: [Description of changes]"

# At session end:
git tag v1.1-production-ready
```

### **Rollback Strategy:**
- Keep backup commits at each stage
- Test changes incrementally
- Maintain stub fallback options
- Document any breaking changes

## Success Criteria

### **Minimum Viable Session (Must Have):**
- [ ] Real AI integration functional
- [ ] Chat produces meaningful responses
- [ ] Error handling prevents crashes
- [ ] Basic usage tracking works

### **Optimal Session Outcome (Should Have):**
- [ ] All 6 stages completed
- [ ] System production-ready
- [ ] Stage II >80% completed
- [ ] Ready for beta testing

### **Nice to Have (Could Have):**
- [ ] Advanced security features
- [ ] Performance optimizations
- [ ] Comprehensive documentation
- [ ] CI/CD preparation

## Post-Session Actions
1. **Update project status:**
   - Mark Stage II items as completed
   - Update progress tracking files
   - Document lessons learned

2. **Plan next iteration:**
   - Identify remaining Stage II items
   - Prioritize Stage III features
   - Set up beta testing program

## Troubleshooting Common Issues

### **AI API Connection Problems:**
- Verify API key validity
- Check network connectivity
- Implement proper error handling
- Test with different AI providers

### **Performance Issues:**
- Add request caching
- Optimize file reading operations
- Implement proper loading states
- Monitor response times

### **Security Concerns:**
- Validate all file paths
- Implement rate limiting
- Secure API key storage
- Add audit logging

## Notes
- Focus on working implementation over perfect code
- Document any deviations from the plan
- Keep the session momentum going
- Test frequently, commit often
