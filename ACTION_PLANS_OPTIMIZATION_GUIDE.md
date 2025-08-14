# 🚀 **ACTION PLANS OPTIMIZACIJOS VEIKSMŲ PLANAS**

## **📋 PHASE 1: KRITINIAI PATAISYMAI (Prioritetas: AUKŠTAS)**

### **1. Backend Task Generation Enhancement**

#### **1.1 Atnaujinti `_generate_tasks` metodą**
```
Failas: backend/app/action_planner.py
Linijos: ~150-180 (dabartinis _generate_tasks metodas)
Tikslas: Pakeisti primityvų task generavimą į intelligent keyword-based sistemą
```

#### **1.2 Pridėti task templates sistemą**
```
Failas: backend/app/action_planner.py  
Vieta: Po TaskPriority enum definition
Tikslas: Sukurti task šablonus pagal kategorijas (performance, features, ui)
```

#### **1.3 Implementuoti smart task selection**
```
Failas: backend/app/action_planner.py
Metodas: _generate_tasks()
Tikslas: Analizuoti user request keywords ir generuoti relevant tasks
```

### **2. Backend DELETE Funkcionalumas**

#### **2.1 Pridėti DELETE endpoint**
```
Failas: backend/app/routes.py
Vieta: Po @bp.route('/api/plans/<plan_id>', methods=['GET'])
Tikslas: Sukurti DELETE /api/plans/<plan_id> endpoint
```

#### **2.2 Implementuoti delete_plan metodą**
```
Failas: backend/app/action_planner.py
Vieta: Po load_plan() metodo
Tikslas: Fiziškai ištrinti plan failą iš storage
```

### **3. Frontend Task Display Fix**

#### **3.1 Pataisyti fetchPlanDetails funkcijou**
```
Failas: frontend/src/app/plans/page.js
Linijos: ~82-90 (fetchPlanDetails funkcija)
Tikslas: Ensure consistent data structure su tasks array
```

#### **3.2 Pridėti delete plan funkcionalumą**
```
Failas: frontend/src/app/plans/page.js
Vieta: Po updateTaskStatus funkcijos
Tikslas: Sukurti deletePlan() funkciją su confirmation
```

#### **3.3 Atnaujinti UI su delete mygtukais**
```
Failas: frontend/src/app/plans/page.js
Linijos: ~220-250 (plans list rendering)
Tikslas: Pridėti delete mygtuką kiekvienam planui
```

---

## **📈 PHASE 2: FUNKCIONALUMO PLĖTRA (Prioritetas: VIDUTINIS)**

### **4. Real AI Integration**

#### **4.1 Sukurti AI analysis metodą**
```
Failas: backend/app/action_planner.py
Metodas: _analyze_with_ai()
Tikslas: Integruoti tikrą AI analizę su ai_agents_full.py
```

#### **4.2 Implementuoti AI response parsing**
```
Failas: backend/app/action_planner.py  
Metodas: _parse_ai_response()
Tikslas: Parse AI JSON response į Task objektus
```

#### **4.3 Sukurti fallback sistemą**
```
Failas: backend/app/action_planner.py
Metodas: _fallback_analysis()
Tikslas: Backup plan jei AI nepasiekiamas
```

### **5. Task Dependencies Sistema**

#### **5.1 Atnaujinti Task dataclass**
```
Failas: backend/app/action_planner.py
Linijos: ~25-40 (Task dataclass)
Tikslas: Pridėti dependencies field validation
```

#### **5.2 Dependencies logic backend**
```
Failas: backend/app/action_planner.py
Metodas: _calculate_dependencies()
Tikslas: Automatic dependency detection based on task types
```

#### **5.3 Frontend dependencies visualization**
```
Failas: frontend/src/app/plans/page.js
Komponentas: TaskCard component
Tikslas: Rodyti task dependencies su visual indicators
```

### **6. Enhanced UI Components**

#### **6.1 Sukurti TaskCard komponentą**
```
Naujas failas: frontend/src/components/plans/TaskCard.js
Tikslas: Dedicated task component su all functionality
```

#### **6.2 Sukurti PlanAnalytics komponentą**
```
Naujas failas: frontend/src/components/plans/PlanAnalytics.js  
Tikslas: Progress tracking ir statistics
```

#### **6.3 Pridėti task status transitions**
```
Failas: frontend/src/app/plans/page.js
Funkcija: updateTaskStatus()
Tikslas: Smart status progression (pending -> in_progress -> completed)
```

---

## **🎯 PHASE 3: ADVANCED FEATURES (Prioritetas: ŽEMAS)**

### **7. Template System**

#### **7.1 Sukurti plan templates**
```
Naujas failas: backend/app/plan_templates.py
Tikslas: Predefined templates for common project types
```

#### **7.2 Template management API**
```
Failas: backend/app/routes.py
Endpoints: /api/templates, /api/templates/<id>
Tikslas: CRUD operations for templates
```

#### **7.3 Frontend template selector**
```
Failas: frontend/src/app/plans/page.js
Komponentas: TemplateSelector
Tikslas: Template selection UI in create form
```

### **8. Progress Tracking & Analytics**

#### **8.1 Time tracking sistema**
```
Failas: backend/app/action_planner.py
Metodas: track_time_spent()
Tikslas: Track actual time vs estimated
```

#### **8.2 Progress reporting**
```
Naujas failas: backend/app/plan_analytics.py
Tikslas: Generate progress reports ir statistics
```

#### **8.3 Charts ir visualizations**
```
Failas: frontend/src/components/plans/PlanCharts.js
Tikslas: Progress charts, time tracking graphs
```

---

## **🔧 DETALŪS IMPLEMENTACIJOS ŽINGSNIAI**

### **ŽINGSNIS 1-1: Backend Task Generation Enhancement**

```bash
# 1. Backup current file
cp backend/app/action_planner.py backend/app/action_planner.py.backup

# 2. Edit action_planner.py
# - Replace _generate_tasks method
# - Add task_templates dictionary  
# - Implement keyword analysis logic

# 3. Test changes
python backend/test_action_planner.py
```

**Implementacijos kodas:**
```python
def _generate_tasks(self, plan_analysis: Dict) -> List[Task]:
    """Generate intelligent tasks based on request analysis"""
    user_request = plan_analysis.get('user_request', '')
    
    # Keyword-based task templates
    task_templates = {
        'performance': [
            ('Performance Analysis', 'Analyze current system performance bottlenecks', 60, 'high'),
            ('Code Optimization', 'Optimize critical code paths and algorithms', 120, 'high'),
            ('Caching Implementation', 'Implement caching strategies', 90, 'medium'),
            ('Database Optimization', 'Optimize database queries and indexes', 90, 'medium')
        ],
        'features': [
            ('Requirements Analysis', 'Define and document new feature requirements', 45, 'high'),
            ('Architecture Design', 'Design system architecture for new features', 90, 'high'),
            ('Implementation Plan', 'Create detailed implementation roadmap', 60, 'medium'),
            ('Testing Strategy', 'Define testing approach and test cases', 45, 'medium')
        ],
        'ui': [
            ('UI/UX Analysis', 'Analyze current user experience', 60, 'high'),
            ('Design System', 'Create/update design system components', 120, 'medium'),
            ('Frontend Implementation', 'Implement new UI components', 180, 'high'),
            ('Responsive Testing', 'Test across different devices', 45, 'low')
        ]
    }
    
    # Intelligent task selection based on keywords
    selected_tasks = []
    request_lower = user_request.lower()
    
    for category, templates in task_templates.items():
        if category in request_lower:
            for title, desc, time, priority in templates:
                selected_tasks.append(Task(
                    id=f"task_{len(selected_tasks) + 1}",
                    title=title,
                    description=desc,
                    estimated_time=time,
                    priority=TaskPriority(priority),
                    tags=[category, 'generated']
                ))
    
    # Fallback if no keywords matched
    if not selected_tasks:
        selected_tasks = [Task(
            id="task_1",
            title="Project Analysis",
            description=f"Analyze requirements for: {user_request}",
            estimated_time=60,
            priority=TaskPriority.HIGH,
            tags=['analysis', 'planning']
        )]
    
    return selected_tasks[:5]  # Limit to 5 tasks max
```

### **ŽINGSNIS 1-2: Backend DELETE Functionality** 

```bash
# 1. Edit routes.py
# - Add DELETE /api/plans/<plan_id> endpoint
# - Add error handling

# 2. Edit action_planner.py  
# - Add delete_plan() method
# - Add file existence checks

# 3. Test with curl
curl -X DELETE http://localhost:5000/api/plans/plan_test_123
```

**Backend DELETE endpoint:**
```python
@bp.route('/api/plans/<plan_id>', methods=['DELETE'])
def delete_action_plan(plan_id):
    """Delete an action plan"""
    try:
        success = action_planner.delete_plan(plan_id)
        if success:
            return jsonify({"success": True, "message": "Plan deleted successfully"})
        else:
            return jsonify({"error": "Plan not found"}), 404
    except Exception as e:
        logger.error(f"Error deleting plan {plan_id}: {str(e)}")
        return jsonify({"error": "Failed to delete plan"}), 500
```

**ActionPlanner delete method:**
```python
def delete_plan(self, plan_id: str) -> bool:
    """Delete plan from storage"""
    file_path = os.path.join(self.storage_path, f"{plan_id}.json")
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            logger.info(f"Plan {plan_id} deleted successfully")
            return True
        else:
            logger.warning(f"Plan {plan_id} not found for deletion")
            return False
    except Exception as e:
        logger.error(f"Error deleting plan {plan_id}: {str(e)}")
        return False
```

### **ŽINGSNIS 1-3: Frontend Fixes**

```bash
# 1. Edit frontend/src/app/plans/page.js
# - Fix fetchPlanDetails data handling
# - Add deletePlan function  
# - Add delete buttons to UI

# 2. Test in browser
# - Create plan, verify tasks display
# - Test delete functionality
# - Check console for errors
```

**Frontend pataisymai:**
```javascript
// Fixed fetchPlanDetails
const fetchPlanDetails = async (planId) => {
    try {
        setSelectedPlan(null) // Clear current selection first
        const response = await fetch(`/api/plans/${planId}`)
        if (response.ok) {
            const data = await response.json()
            // Ensure tasks array always exists
            const planWithTasks = {
                ...data.plan,
                tasks: data.plan.tasks || []
            }
            setSelectedPlan(planWithTasks)
        } else {
            console.error('Failed to fetch plan details:', response.status)
        }
    } catch (error) {
        console.error('Error fetching plan details:', error)
        setSelectedPlan(null)
    }
}

// Delete plan functionality
const deletePlan = async (planId) => {
    if (!confirm('Are you sure you want to delete this plan? This action cannot be undone.')) {
        return
    }
    
    try {
        const response = await fetch(`/api/plans/${planId}`, {
            method: 'DELETE'
        })
        
        if (response.ok) {
            // Remove from plans list
            setPlans(plans.filter(p => p.id !== planId))
            // Clear selection if deleted plan was selected
            if (selectedPlan?.id === planId) {
                setSelectedPlan(null)
            }
            console.log('Plan deleted successfully')
        } else {
            console.error('Failed to delete plan:', response.status)
            alert('Failed to delete plan. Please try again.')
        }
    } catch (error) {
        console.error('Error deleting plan:', error)
        alert('Error occurred while deleting plan.')
    }
}

// UI with delete buttons
{plans.map((plan) => (
    <Card 
        key={plan.id} 
        className={`cursor-pointer transition-colors ${
            selectedPlan?.id === plan.id ? 'ring-2 ring-blue-500' : 'hover:bg-gray-50'
        }`}
    >
        <CardContent className="p-4">
            <div className="flex justify-between items-start mb-2">
                <h3 
                    className="font-medium cursor-pointer flex-1"
                    onClick={() => fetchPlanDetails(plan.id)}
                >
                    {plan.title}
                </h3>
                <Button
                    size="sm"
                    variant="outline"
                    onClick={(e) => {
                        e.stopPropagation()
                        deletePlan(plan.id)
                    }}
                    className="text-red-600 hover:text-red-800 hover:bg-red-50"
                >
                    🗑️
                </Button>
            </div>
            <p 
                className="text-sm text-gray-600 mb-3 line-clamp-2 cursor-pointer"
                onClick={() => fetchPlanDetails(plan.id)}
            >
                {plan.description}
            </p>
            <div className="flex justify-between items-center text-xs text-gray-500">
                <span>{plan.total_tasks} tasks</span>
                <span>{Math.round(plan.completion_percentage)}% complete</span>
            </div>
            <div className="mt-2 w-full bg-gray-200 rounded-full h-2">
                <div 
                    className="bg-blue-500 h-2 rounded-full transition-all duration-300" 
                    style={{ width: `${plan.completion_percentage}%` }}
                ></div>
            </div>
        </CardContent>
    </Card>
))}
```

### **ŽINGSNIS 2-1: AI Integration**

```bash
# 1. Test AI agents availability
python backend/test_ai_integration.py

# 2. Implement _analyze_with_ai method
# - Import ai_agents_full
# - Create analysis prompt
# - Handle AI response

# 3. Create test cases
python backend/test_ai_plans.py
```

**AI Integration kodas:**
```python
def _analyze_with_ai(self, user_request: str, project_context: Dict = None) -> Dict:
    """Use real AI to analyze request and generate intelligent tasks"""
    try:
        # Import AI orchestrator
        from app.ai_agents_full import COAIOrchestrator
        
        # Create analysis prompt
        analysis_prompt = f"""
        Analyze this project request and break it down into actionable tasks:
        
        Request: "{user_request}"
        
        Please provide a detailed analysis in JSON format:
        {{
            "title": "Short descriptive project title",
            "description": "Detailed project description",
            "estimated_complexity": "low|medium|high",
            "categories": ["performance", "features", "ui", "backend", "testing"],
            "tasks": [
                {{
                    "title": "Task title",
                    "description": "Detailed task description",
                    "estimated_time": 60,
                    "priority": "high|medium|low",
                    "category": "performance|features|ui|backend|testing",
                    "dependencies": []
                }}
            ]
        }}
        
        Generate 3-5 specific, actionable tasks with realistic time estimates.
        """
        
        # Get AI response
        ai_orchestrator = COAIOrchestrator()
        ai_response = ai_orchestrator.generate_response(
            analysis_prompt, 
            agent_name='project_planner',
            project=project_context.get('project', 'coai') if project_context else 'coai'
        )
        
        # Parse AI response
        return self._parse_ai_response(ai_response)
        
    except Exception as e:
        logger.warning(f"AI analysis failed: {str(e)}, using fallback")
        return self._fallback_analysis(user_request)

def _parse_ai_response(self, ai_response: str) -> Dict:
    """Parse AI JSON response into structured data"""
    try:
        import json
        import re
        
        # Extract JSON from response (AI might include extra text)
        json_match = re.search(r'\{.*\}', ai_response, re.DOTALL)
        if json_match:
            json_str = json_match.group()
            parsed = json.loads(json_str)
            
            # Validate required fields
            if 'tasks' in parsed and isinstance(parsed['tasks'], list):
                return parsed
        
        raise ValueError("Invalid AI response format")
        
    except Exception as e:
        logger.error(f"Failed to parse AI response: {str(e)}")
        # Return fallback structure
        return {
            "title": "AI-Generated Plan",
            "description": "AI analysis unavailable, using fallback",
            "tasks": []
        }

def _fallback_analysis(self, user_request: str) -> Dict:
    """Fallback analysis when AI is unavailable"""
    return {
        "title": "Custom Development Plan",
        "description": user_request,
        "user_request": user_request,
        "estimated_complexity": "medium",
        "categories": self._detect_categories(user_request)
    }

def _detect_categories(self, user_request: str) -> List[str]:
    """Detect project categories from user request"""
    request_lower = user_request.lower()
    categories = []
    
    category_keywords = {
        'performance': ['performance', 'optimize', 'speed', 'fast', 'cache'],
        'features': ['feature', 'add', 'new', 'implement', 'functionality'],
        'ui': ['ui', 'interface', 'design', 'frontend', 'user'],
        'backend': ['backend', 'api', 'server', 'database'],
        'testing': ['test', 'testing', 'quality', 'validation']
    }
    
    for category, keywords in category_keywords.items():
        if any(keyword in request_lower for keyword in keywords):
            categories.append(category)
    
    return categories if categories else ['general']
```

---

## **✅ TESTING & VALIDATION PLAN**

### **Unit Tests**
```bash
# Backend tests
python -m pytest backend/tests/test_action_planner.py
python -m pytest backend/tests/test_routes_plans.py

# Frontend tests  
cd frontend && npm test -- plans.test.js
```

### **Integration Tests**
```bash
# End-to-end API testing
python backend/test_plans_e2e.py

# Frontend integration
cd frontend && npm run test:integration
```

### **Manual Testing Checklist**
- [ ] Create plan with "Optimize COAI performance and add new features"
- [ ] Verify multiple tasks generated with different priorities
- [ ] Test task status updates
- [ ] Test plan deletion with confirmation
- [ ] Verify UI responsiveness and error handling
- [ ] Check console for JavaScript errors
- [ ] Test with different request types (performance, features, UI)

### **Test Cases för "Optimize COAI performance and add new features"**

**Expected Results:**
```json
{
  "title": "COAI Performance & Feature Enhancement",
  "tasks": [
    {
      "title": "Performance Analysis",
      "priority": "high",
      "estimated_time": 60,
      "category": "performance"
    },
    {
      "title": "Code Optimization", 
      "priority": "high",
      "estimated_time": 120,
      "category": "performance"
    },
    {
      "title": "Requirements Analysis",
      "priority": "high", 
      "estimated_time": 45,
      "category": "features"
    },
    {
      "title": "Architecture Design",
      "priority": "high",
      "estimated_time": 90,
      "category": "features"
    }
  ]
}
```

---

## **📊 SUCCESS METRICS**

### **Phase 1 Goals:**
- ✅ Plans generate 3-5 relevant tasks instead of 1 generic task
- ✅ Tasks have appropriate priorities (high/medium/low)
- ✅ Estimated times are realistic (30-180 minutes)
- ✅ All tasks display correctly in UI without errors
- ✅ Delete functionality works with proper confirmation
- ✅ No console errors or application crashes

### **Phase 2 Goals:**
- ✅ AI-generated tasks are contextually relevant
- ✅ Task categories match request content
- ✅ Dependencies are logically structured
- ✅ Progress tracking shows accurate completion
- ✅ Enhanced UI components are responsive

### **Phase 3 Goals:**
- ✅ Template system reduces plan creation time
- ✅ Analytics provide actionable insights
- ✅ Time tracking improves estimation accuracy
- ✅ Professional-grade user experience

---

## **⏰ TIMELINE ESTIMATE**

### **Phase 1 (Critical Fixes):** 1-2 dienos
- **Day 1:** Backend task generation + DELETE functionality
- **Day 2:** Frontend fixes + testing + validation

### **Phase 2 (Enhancement):** 3-5 dienos  
- **Day 3-4:** AI integration + response parsing
- **Day 5:** Dependencies system + enhanced UI
- **Day 6:** Testing + bug fixes

### **Phase 3 (Advanced):** 1-2 savaitės
- **Week 2:** Template system + progress analytics
- **Week 3:** Polish + performance optimization

**Total Project Duration:** 2-3 savaitės

---

## **🎯 NEXT STEPS**

1. **Start with Phase 1, Step 1-1** - Backend task generation enhancement
2. **Test each change incrementally** - Don't implement everything at once
3. **Validate with real usage** - Test with the example "Optimize COAI performance and add new features"
4. **Document any issues** - Keep track of problems and solutions
5. **Get user feedback** - Test with actual users before moving to next phase

**Ready to begin implementation? Recommend starting with Phase 1, Step 1-1 (Backend Task Generation Enhancement).**
