# 🚀 **COPILOT INSTRUCTIONS: PROJECT DISCOVERY & INITIALIZATION**

## **📋 OBJECTIVE**
Implement intelligent project discovery and initialization system for COAI UI first launch experience. Transform generic dashboard into smart, context-aware project workspace that automatically detects user intent and project context.

## **🎯 SCOPE & GOALS**

### **Primary Goal:**
Create seamless first-launch experience that:
- **Detects projects** in C:\ai_projects automatically
- **Routes users intelligently** based on project count (0, 1, 2+)
- **Loads project context** without manual selection
- **Provides guided onboarding** for new users

### **Success Metrics:**
- ✅ **< 3 seconds** from UI launch to usable state
- ✅ **Zero clicks** required for returning single-project users
- ✅ **Complete project context** loaded before user interaction
- ✅ **Graceful fallbacks** for all error scenarios
- ✅ **Professional onboarding** for first-time users

---

## **🏗️ IMPLEMENTATION PHASES**

### **PHASE 1: CORE DISCOVERY ENGINE** ⚡ *Priority: CRITICAL*
**Estimated Time: 1.5 hours**

#### **1.1 Create Project Discovery Service**
**File:** `frontend/src/services/ProjectDiscoveryService.js`

**Requirements:**
- Scan C:\ai_projects directory
- Validate project structures
- Detect project types (Python, Node.js, etc.)
- Cache results for performance
- Handle permissions errors gracefully

**Implementation Logic:**
```
Discovery Flow:
1. API call to /api/projects/discover
2. Enhanced project validation (config.json, rules.txt, etc.)
3. Project type detection (package.json, requirements.txt, etc.)
4. Activity score calculation (recent files, chat history)
5. Return enriched project list with metadata
```

#### **1.2 Enhance Backend Projects API**
**File:** `backend/app/routes.py`

**New Endpoint:** `GET /api/projects/discover`

**Response Structure:**
```json
{
  "projects": [
    {
      "name": "coai",
      "path": "C:\\ai_projects\\coai",
      "type": "python", 
      "lastActivity": "2025-08-14T10:30:00Z",
      "hasConfig": true,
      "hasPlans": true,
      "chatHistory": 15,
      "activityScore": 85
    }
  ],
  "totalProjects": 1,
  "firstTimeUser": false,
  "recommendedProject": "coai"
}
```

#### **1.3 Create Session State Manager**
**File:** `frontend/src/hooks/useSessionManager.js`

**Responsibilities:**
- Track session state (loading, ready, error)
- Manage current project context
- Handle project switching
- Persist session data
- Coordinate component updates

---

### **PHASE 2: INTELLIGENT ROUTING SYSTEM** 🧠 *Priority: HIGH*
**Estimated Time: 2 hours**

#### **2.1 Create Decision Engine**
**File:** `frontend/src/utils/UserFlowDecisionEngine.js`

**Decision Matrix Logic:**
```
Input: { projectCount, hasHistory, systemReady }
Output: { flowType, targetComponent, preloadData }

Rules:
- projectCount === 0 → OnboardingFlow
- projectCount === 1 → AutoLoadProject  
- projectCount >= 2 && hasHistory → SmartProjectSelector
- projectCount >= 2 && !hasHistory → ProjectListView
- !systemReady → SystemCheckFlow
```

#### **2.2 Update Main Dashboard**
**File:** `frontend/src/app/page.js`

**Current State:** Generic welcome page
**Target State:** Intelligent routing hub

**New Structure:**
```jsx
export default function Dashboard() {
  const { sessionState, projects, currentProject } = useSessionManager()
  const { flowType, targetComponent } = useFlowDecision(sessionState)
  
  return (
    <DynamicRouter 
      flowType={flowType}
      projects={projects}
      currentProject={currentProject}
    />
  )
}
```

#### **2.3 Create Dynamic Router Component**
**File:** `frontend/src/components/DynamicRouter.js`

**Routing Logic:**
- `OnboardingFlow` → New user experience
- `AutoLoadProject` → Instant project activation  
- `SmartProjectSelector` → Intelligent project selection
- `ProjectListView` → Traditional project list
- `SystemCheckFlow` → Error recovery interface

---

### **PHASE 3: ONBOARDING FLOW** 🎓 *Priority: HIGH*
**Estimated Time: 2 hours**

#### **3.1 Create Welcome Wizard**
**File:** `frontend/src/components/onboarding/WelcomeWizard.js`

**Multi-Step Flow:**
1. **Welcome Screen** - System introduction
2. **Project Setup** - Create first project
3. **AI Configuration** - API key setup
4. **Feature Tour** - Guided navigation
5. **First Chat** - Immediate value demonstration

#### **3.2 Create Project Setup Wizard**
**File:** `frontend/src/components/onboarding/ProjectSetupWizard.js`

**Features:**
- Project name validation
- Directory structure creation
- Template selection (Python, Node.js, General)
- Initial configuration generation
- Git repository initialization option

#### **3.3 Create AI Setup Assistant**
**File:** `frontend/src/components/onboarding/AISetupAssistant.js`

**Capabilities:**
- API key validation
- Agent selection (OpenAI, GitHub Copilot)
- Connection testing
- Fallback configuration
- Usage guidelines

---

### **PHASE 4: AUTO-LOAD SYSTEM** ⚡ *Priority: HIGH*
**Estimated Time: 1.5 hours**

#### **4.1 Create Project Context Loader**
**File:** `frontend/src/services/ProjectContextLoader.js`

**Loading Sequence:**
1. Project configuration (config.json)
2. Rules and preferences (rules.txt)
3. Chat history (recent 50 messages)
4. Action plans (active plans only)
5. File structure cache (recent files)
6. Usage statistics (last 30 days)

#### **4.2 Enhance useProjectContext Hook**
**File:** `frontend/src/hooks/useProjectContext.js`

**Current State:** Basic project loading
**Enhanced Features:**
- Background context preloading
- Progressive data loading
- Error recovery mechanisms
- Cache management
- Real-time updates

#### **4.3 Create Context-Aware Dashboard**
**File:** `frontend/src/components/dashboard/ContextAwareDashboard.js`

**Smart Widgets:**
- **Recent Activity** - Last chat conversations
- **Active Plans** - Current action items
- **Quick Actions** - Context-based suggestions
- **Project Health** - Status indicators
- **Usage Summary** - Daily/weekly stats

---

### **PHASE 5: SMART PROJECT SELECTOR** 🎯 *Priority: MEDIUM*
**Estimated Time: 2 hours**

#### **5.1 Create Intelligent Project List**
**File:** `frontend/src/components/projects/SmartProjectSelector.js`

**Features:**
- **Smart Sorting** - Recent activity, importance score
- **Quick Preview** - Project cards with metadata
- **Search & Filter** - Real-time project filtering  
- **Favorites System** - Pin frequently used projects
- **Activity Indicators** - Visual activity metrics

#### **5.2 Create Project Preview Cards**
**File:** `frontend/src/components/projects/ProjectPreviewCard.js`

**Card Content:**
- Project name and type icon
- Last activity timestamp
- Active action plans count
- Recent chat preview
- Activity score visualization
- Quick action buttons

#### **5.3 Implement Smart Suggestions**
**File:** `frontend/src/utils/ProjectSuggestionEngine.js`

**Suggestion Logic:**
- **Most Recent** - Last accessed project
- **Most Active** - Highest activity score
- **Pending Tasks** - Projects with active plans
- **Time-based** - Morning/afternoon patterns
- **Work Context** - Related project groups

---

## **🔧 DETAILED IMPLEMENTATION STEPS**

### **STEP 1: Backend Discovery API Enhancement**

#### **1.1 Update routes.py**
```python
# Add new endpoint after existing /api/projects route

@bp.route('/api/projects/discover', methods=['GET'])
def discover_projects():
    """Enhanced project discovery with metadata"""
    try:
        projects_dir = "C:\\ai_projects"
        projects = []
        
        if not os.path.exists(projects_dir):
            return jsonify({
                "projects": [],
                "totalProjects": 0,
                "firstTimeUser": True,
                "error": "Projects directory not found"
            })
        
        for project_name in os.listdir(projects_dir):
            project_path = os.path.join(projects_dir, project_name)
            
            if os.path.isdir(project_path):
                # Gather project metadata
                project_info = analyze_project_structure(project_path, project_name)
                projects.append(project_info)
        
        # Sort by activity score
        projects.sort(key=lambda x: x.get('activityScore', 0), reverse=True)
        
        return jsonify({
            "projects": projects,
            "totalProjects": len(projects),
            "firstTimeUser": len(projects) == 0,
            "recommendedProject": projects[0]['name'] if projects else None
        })
        
    except Exception as e:
        logger.error(f"Error discovering projects: {str(e)}")
        return jsonify({"error": "Failed to discover projects"}), 500

def analyze_project_structure(project_path, project_name):
    """Analyze project structure and calculate metadata"""
    config_path = os.path.join(project_path, "config.json")
    rules_path = os.path.join(project_path, "rules.txt")
    plans_dir = os.path.join(project_path, ".coai", "plans")
    logs_dir = os.path.join(project_path, ".coai", "logs")
    
    # Basic project info
    project_info = {
        "name": project_name,
        "path": project_path,
        "type": detect_project_type(project_path),
        "hasConfig": os.path.exists(config_path),
        "hasRules": os.path.exists(rules_path),
        "hasPlans": os.path.exists(plans_dir),
        "activityScore": 0
    }
    
    # Calculate activity score
    activity_score = calculate_activity_score(project_path)
    project_info["activityScore"] = activity_score
    
    # Get last activity
    last_activity = get_last_activity(project_path)
    if last_activity:
        project_info["lastActivity"] = last_activity.isoformat()
    
    # Count chat history
    chat_history_path = os.path.join(logs_dir, "chat_history.json")
    if os.path.exists(chat_history_path):
        try:
            with open(chat_history_path, 'r', encoding='utf-8') as f:
                history = json.load(f)
                project_info["chatHistory"] = len(history.get('messages', []))
        except:
            project_info["chatHistory"] = 0
    else:
        project_info["chatHistory"] = 0
    
    return project_info

def detect_project_type(project_path):
    """Detect project type based on files present"""
    if os.path.exists(os.path.join(project_path, "package.json")):
        return "nodejs"
    elif os.path.exists(os.path.join(project_path, "requirements.txt")):
        return "python"
    elif os.path.exists(os.path.join(project_path, "Cargo.toml")):
        return "rust"
    elif os.path.exists(os.path.join(project_path, "go.mod")):
        return "go"
    else:
        return "general"

def calculate_activity_score(project_path):
    """Calculate project activity score based on various factors"""
    score = 0
    current_time = datetime.now()
    
    # Recent file modifications (last 7 days)
    for root, dirs, files in os.walk(project_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                mod_time = datetime.fromtimestamp(os.path.getmtime(file_path))
                days_old = (current_time - mod_time).days
                if days_old <= 7:
                    score += max(0, 10 - days_old)
            except:
                continue
    
    # Chat activity bonus
    logs_dir = os.path.join(project_path, ".coai", "logs")
    chat_history_path = os.path.join(logs_dir, "chat_history.json")
    if os.path.exists(chat_history_path):
        try:
            with open(chat_history_path, 'r', encoding='utf-8') as f:
                history = json.load(f)
                recent_messages = [
                    msg for msg in history.get('messages', [])
                    if 'timestamp' in msg and
                    (current_time - datetime.fromisoformat(msg['timestamp'])).days <= 7
                ]
                score += len(recent_messages) * 5
        except:
            pass
    
    # Configuration completeness bonus
    if os.path.exists(os.path.join(project_path, "config.json")):
        score += 20
    if os.path.exists(os.path.join(project_path, "rules.txt")):
        score += 15
    
    return min(score, 100)  # Cap at 100

def get_last_activity(project_path):
    """Get the most recent activity timestamp"""
    latest_time = None
    
    for root, dirs, files in os.walk(project_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                mod_time = datetime.fromtimestamp(os.path.getmtime(file_path))
                if latest_time is None or mod_time > latest_time:
                    latest_time = mod_time
            except:
                continue
    
    return latest_time
```

#### **1.2 Add Required Imports**
Add to top of routes.py:
```python
import json
from datetime import datetime
```

### **STEP 2: Frontend Session Manager**

#### **2.1 Create useSessionManager Hook**
**File:** `frontend/src/hooks/useSessionManager.js`

```javascript
'use client'
import { useState, useEffect, useCallback } from 'react'

export default function useSessionManager() {
  const [sessionState, setSessionState] = useState('initializing')
  const [projects, setProjects] = useState([])
  const [currentProject, setCurrentProject] = useState(null)
  const [systemReady, setSystemReady] = useState(false)
  const [error, setError] = useState(null)

  // Initialize session on mount
  useEffect(() => {
    initializeSession()
  }, [])

  const initializeSession = async () => {
    try {
      setSessionState('discovering')
      
      // Step 1: Check system readiness
      const systemCheck = await checkSystemReadiness()
      setSystemReady(systemCheck.ready)
      
      if (!systemCheck.ready) {
        setSessionState('system_error')
        setError(systemCheck.error)
        return
      }
      
      // Step 2: Discover projects
      const discovery = await discoverProjects()
      setProjects(discovery.projects)
      
      // Step 3: Determine flow based on project count
      if (discovery.firstTimeUser) {
        setSessionState('onboarding')
      } else if (discovery.totalProjects === 1) {
        setSessionState('auto_loading')
        await autoLoadProject(discovery.projects[0])
      } else {
        setSessionState('project_selection')
      }
      
    } catch (err) {
      console.error('Session initialization failed:', err)
      setSessionState('error')
      setError(err.message)
    }
  }

  const checkSystemReadiness = async () => {
    try {
      // Check backend connectivity
      const response = await fetch('/api/health', {
        timeout: 5000
      })
      
      if (!response.ok) {
        throw new Error('Backend unavailable')
      }
      
      return { ready: true }
    } catch (error) {
      return { 
        ready: false, 
        error: 'Backend service unavailable. Please ensure servers are running.' 
      }
    }
  }

  const discoverProjects = async () => {
    const response = await fetch('/api/projects/discover')
    if (!response.ok) {
      throw new Error('Failed to discover projects')
    }
    return await response.json()
  }

  const autoLoadProject = async (project) => {
    try {
      setSessionState('loading_context')
      
      // Load project context
      const context = await loadProjectContext(project.name)
      setCurrentProject({ ...project, context })
      
      setSessionState('ready')
    } catch (err) {
      console.error('Auto-load failed:', err)
      setSessionState('project_selection') // Fallback to manual selection
    }
  }

  const loadProjectContext = async (projectName) => {
    // Load project-specific data
    const [config, details, plans] = await Promise.all([
      fetchProjectConfig(projectName),
      fetchProjectDetails(projectName),
      fetchProjectPlans(projectName)
    ])
    
    return { config, details, plans }
  }

  const fetchProjectConfig = async (projectName) => {
    try {
      const response = await fetch(`/api/project-details?name=${encodeURIComponent(projectName)}`)
      return response.ok ? await response.json() : null
    } catch {
      return null
    }
  }

  const fetchProjectDetails = async (projectName) => {
    try {
      const response = await fetch(`/api/projects/${encodeURIComponent(projectName)}/details`)
      return response.ok ? await response.json() : null
    } catch {
      return null
    }
  }

  const fetchProjectPlans = async (projectName) => {
    try {
      const response = await fetch(`/api/plans?project=${encodeURIComponent(projectName)}`)
      return response.ok ? await response.json() : { plans: [] }
    } catch {
      return { plans: [] }
    }
  }

  const selectProject = async (project) => {
    setSessionState('loading_context')
    await autoLoadProject(project)
  }

  const createNewProject = useCallback(async (projectData) => {
    try {
      setSessionState('creating_project')
      
      const response = await fetch('/api/projects/create', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(projectData)
      })
      
      if (!response.ok) {
        throw new Error('Project creation failed')
      }
      
      const newProject = await response.json()
      
      // Refresh projects list
      const discovery = await discoverProjects()
      setProjects(discovery.projects)
      
      // Auto-load new project
      await autoLoadProject(newProject)
      
    } catch (err) {
      setError(err.message)
      setSessionState('onboarding') // Stay in onboarding on error
    }
  }, [])

  return {
    sessionState,
    projects,
    currentProject,
    systemReady,
    error,
    selectProject,
    createNewProject,
    refreshProjects: initializeSession
  }
}
```

### **STEP 3: Flow Decision Engine**

#### **3.1 Create UserFlowDecisionEngine**
**File:** `frontend/src/utils/UserFlowDecisionEngine.js`

```javascript
export class UserFlowDecisionEngine {
  static determineFlow(sessionData) {
    const { sessionState, projects, systemReady, error } = sessionData
    
    // System health check
    if (!systemReady || error) {
      return {
        flowType: 'system_error',
        component: 'SystemErrorFlow',
        props: { error }
      }
    }
    
    // Route based on session state
    switch (sessionState) {
      case 'initializing':
      case 'discovering':
      case 'loading_context':
        return {
          flowType: 'loading',
          component: 'LoadingFlow',
          props: { stage: sessionState }
        }
      
      case 'onboarding':
        return {
          flowType: 'onboarding',
          component: 'OnboardingFlow',
          props: { }
        }
      
      case 'auto_loading':
        return {
          flowType: 'auto_loading',
          component: 'AutoLoadingFlow',
          props: { project: projects[0] }
        }
      
      case 'project_selection':
        return {
          flowType: 'project_selection',
          component: 'ProjectSelectionFlow',
          props: { projects, hasHistory: this.hasSessionHistory() }
        }
      
      case 'ready':
        return {
          flowType: 'ready',
          component: 'ContextAwareDashboard',
          props: { }
        }
      
      default:
        return {
          flowType: 'error',
          component: 'ErrorFlow',
          props: { error: 'Unknown session state' }
        }
    }
  }
  
  static hasSessionHistory() {
    // Check localStorage for previous sessions
    try {
      const history = localStorage.getItem('coai_session_history')
      return history ? JSON.parse(history).length > 0 : false
    } catch {
      return false
    }
  }
  
  static shouldShowQuickStart(projects) {
    // Show quick start if user has projects but limited activity
    return projects.length > 0 && 
           projects.every(p => (p.activityScore || 0) < 30)
  }
  
  static getRecommendedProject(projects) {
    if (!projects.length) return null
    
    // Sort by activity score and return top project
    return projects.sort((a, b) => (b.activityScore || 0) - (a.activityScore || 0))[0]
  }
}

export function useFlowDecision(sessionData) {
  return UserFlowDecisionEngine.determineFlow(sessionData)
}
```

### **STEP 4: Dynamic Router Implementation**

#### **4.1 Update Main Dashboard**
**File:** `frontend/src/app/page.js`

```javascript
'use client'
import { Suspense } from 'react'
import useSessionManager from '@/hooks/useSessionManager'
import { useFlowDecision } from '@/utils/UserFlowDecisionEngine'
import DynamicRouter from '@/components/DynamicRouter'
import LoadingScreen from '@/components/ui/LoadingScreen'

export default function Dashboard() {
  const sessionData = useSessionManager()
  const flowDecision = useFlowDecision(sessionData)
  
  return (
    <div className="min-h-screen bg-[var(--background)]">
      <Suspense fallback={<LoadingScreen message="Initializing COAI..." />}>
        <DynamicRouter 
          flowDecision={flowDecision}
          sessionData={sessionData}
        />
      </Suspense>
    </div>
  )
}
```

#### **4.2 Create Dynamic Router**
**File:** `frontend/src/components/DynamicRouter.js`

```javascript
'use client'
import { lazy, Suspense } from 'react'
import LoadingScreen from '@/components/ui/LoadingScreen'

// Lazy load components for better performance
const OnboardingFlow = lazy(() => import('@/components/onboarding/OnboardingFlow'))
const ProjectSelectionFlow = lazy(() => import('@/components/projects/ProjectSelectionFlow'))
const ContextAwareDashboard = lazy(() => import('@/components/dashboard/ContextAwareDashboard'))
const SystemErrorFlow = lazy(() => import('@/components/error/SystemErrorFlow'))
const AutoLoadingFlow = lazy(() => import('@/components/loading/AutoLoadingFlow'))

export default function DynamicRouter({ flowDecision, sessionData }) {
  const { flowType, component, props } = flowDecision
  
  const renderComponent = () => {
    switch (component) {
      case 'OnboardingFlow':
        return <OnboardingFlow {...props} sessionData={sessionData} />
      
      case 'ProjectSelectionFlow':
        return <ProjectSelectionFlow {...props} sessionData={sessionData} />
      
      case 'ContextAwareDashboard':
        return <ContextAwareDashboard {...props} sessionData={sessionData} />
      
      case 'SystemErrorFlow':
        return <SystemErrorFlow {...props} sessionData={sessionData} />
      
      case 'AutoLoadingFlow':
        return <AutoLoadingFlow {...props} sessionData={sessionData} />
      
      case 'LoadingFlow':
        return (
          <LoadingScreen 
            message={getLoadingMessage(props.stage)} 
            stage={props.stage}
          />
        )
      
      default:
        return (
          <SystemErrorFlow 
            error="Unknown component type" 
            sessionData={sessionData} 
          />
        )
    }
  }
  
  return (
    <Suspense fallback={<LoadingScreen message="Loading interface..." />}>
      <div className="dynamic-router" data-flow-type={flowType}>
        {renderComponent()}
      </div>
    </Suspense>
  )
}

function getLoadingMessage(stage) {
  const messages = {
    'initializing': 'Starting COAI system...',
    'discovering': 'Scanning for projects...',
    'auto_loading': 'Loading project context...',
    'loading_context': 'Preparing workspace...',
    'creating_project': 'Creating new project...'
  }
  
  return messages[stage] || 'Loading...'
}
```

### **STEP 5: Create Loading Components**

#### **5.1 Enhanced Loading Screen**
**File:** `frontend/src/components/ui/LoadingScreen.js`

```javascript
'use client'
import { useState, useEffect } from 'react'

export default function LoadingScreen({ message = "Loading...", stage = null }) {
  const [dots, setDots] = useState('')
  
  useEffect(() => {
    const interval = setInterval(() => {
      setDots(prev => prev.length >= 3 ? '' : prev + '.')
    }, 500)
    
    return () => clearInterval(interval)
  }, [])
  
  const getProgressPercentage = () => {
    const stageProgress = {
      'initializing': 10,
      'discovering': 30,
      'auto_loading': 60,
      'loading_context': 80,
      'creating_project': 70
    }
    
    return stageProgress[stage] || 50
  }
  
  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-[var(--background)] text-[var(--foreground)]">
      <div className="text-center max-w-md">
        {/* COAI Logo/Icon */}
        <div className="mb-8">
          <div className="w-16 h-16 mx-auto bg-blue-600 rounded-lg flex items-center justify-center text-white text-2xl font-bold">
            AI
          </div>
        </div>
        
        {/* Loading Message */}
        <h2 className="text-xl font-medium mb-4">
          {message}{dots}
        </h2>
        
        {/* Progress Bar */}
        <div className="w-64 bg-gray-200 rounded-full h-2 mb-4">
          <div 
            className="bg-blue-600 h-2 rounded-full transition-all duration-500"
            style={{ width: `${getProgressPercentage()}%` }}
          />
        </div>
        
        {/* Stage Information */}
        {stage && (
          <p className="text-sm text-[var(--foreground-muted)]">
            {getStageDescription(stage)}
          </p>
        )}
        
        {/* Animated Indicator */}
        <div className="mt-6 flex justify-center space-x-1">
          {[0, 1, 2].map((i) => (
            <div
              key={i}
              className="w-2 h-2 bg-blue-600 rounded-full animate-pulse"
              style={{ animationDelay: `${i * 0.3}s` }}
            />
          ))}
        </div>
      </div>
    </div>
  )
}

function getStageDescription(stage) {
  const descriptions = {
    'initializing': 'Checking system components...',
    'discovering': 'Finding your projects in C:\\ai_projects\\',
    'auto_loading': 'Preparing your workspace environment...',
    'loading_context': 'Loading project configuration and history...',
    'creating_project': 'Setting up project structure and files...'
  }
  
  return descriptions[stage] || 'Processing request...'
}
```

---

## **🔄 TESTING & VALIDATION PLAN**

### **Testing Scenarios Matrix**

#### **Scenario 1: First-Time User (New Installation)**
```
Given: Empty C:\ai_projects directory
When: User opens COAI UI
Then: 
  ✅ Shows onboarding flow
  ✅ Guides through project creation
  ✅ Sets up AI configuration
  ✅ Creates first project successfully
  ✅ Loads dashboard with new project context
```

#### **Scenario 2: Single Project User (Returning)**
```
Given: One project in C:\ai_projects\my-project
When: User opens COAI UI  
Then:
  ✅ Auto-detects single project
  ✅ Loads project context < 3 seconds
  ✅ Shows dashboard with project data
  ✅ No manual project selection required
  ✅ Chat interface ready with context
```

#### **Scenario 3: Multi-Project User (Power User)**
```
Given: Multiple projects (coai, project-alpha, project-beta)
When: User opens COAI UI
Then:
  ✅ Shows intelligent project selector
  ✅ Projects sorted by activity score
  ✅ Highlights most recently used project
  ✅ Shows project metadata and previews
  ✅ One-click project switching
```

#### **Scenario 4: System Error Recovery**
```
Given: Backend service offline
When: User opens COAI UI
Then:
  ✅ Detects backend unavailability
  ✅ Shows clear error message
  ✅ Provides recovery instructions
  ✅ Offers offline mode option
  ✅ Retry mechanism available
```

### **Performance Benchmarks**
- **Initial Load Time:** < 2 seconds to first paint
- **Project Discovery:** < 1 second for 10 projects
- **Context Loading:** < 3 seconds for full project context
- **Memory Usage:** < 100MB for project cache
- **API Response Time:** < 500ms for discovery endpoint

---

## **📋 IMPLEMENTATION CHECKLIST**

### **Phase 1: Discovery Engine ⚡**
- [ ] Create ProjectDiscoveryService.js
- [ ] Add /api/projects/discover endpoint
- [ ] Implement project metadata analysis
- [ ] Add activity score calculation
- [ ] Create useSessionManager hook
- [ ] Add error handling and fallbacks

### **Phase 2: Routing System 🧠**
- [ ] Create UserFlowDecisionEngine.js
- [ ] Update main Dashboard component
- [ ] Create DynamicRouter component
- [ ] Implement component lazy loading
- [ ] Add flow type detection logic

### **Phase 3: Onboarding Flow 🎓**
- [ ] Create WelcomeWizard component
- [ ] Create ProjectSetupWizard component
- [ ] Create AISetupAssistant component
- [ ] Add project creation API endpoint
- [ ] Implement guided tour system

### **Phase 4: Auto-Load System ⚡**
- [ ] Create ProjectContextLoader service
- [ ] Enhance useProjectContext hook
- [ ] Create ContextAwareDashboard component
- [ ] Add background data preloading
- [ ] Implement progressive loading

### **Phase 5: Smart Selector 🎯**
- [ ] Create SmartProjectSelector component
- [ ] Create ProjectPreviewCard component
- [ ] Implement ProjectSuggestionEngine
- [ ] Add search and filter functionality
- [ ] Create favorites system

### **Testing & Quality Assurance**
- [ ] Unit tests for all services
- [ ] Integration tests for user flows
- [ ] Performance testing
- [ ] Error scenario testing
- [ ] Cross-browser compatibility testing

---

## **🚀 DEPLOYMENT INSTRUCTIONS**

### **Pre-Deployment Checklist**
1. **Backend Dependencies:**
   - Verify Python imports are available
   - Test /api/projects/discover endpoint
   - Validate project structure analysis
   - Check error handling

2. **Frontend Dependencies:**
   - Install any new npm packages
   - Verify hook implementations
   - Test lazy loading components
   - Check routing logic

3. **System Integration:**
   - Test with real project structures
   - Verify C:\ai_projects access
   - Check file permission handling
   - Test API connectivity

### **Rollback Strategy**
- Keep current dashboard as fallback
- Implement feature flags for gradual rollout
- Maintain backward compatibility
- Monitor error rates and performance

### **Success Metrics Monitoring**
- Track user flow completion rates
- Monitor load times and performance
- Measure user satisfaction scores
- Analyze project discovery accuracy

---

## **📚 ADDITIONAL RESOURCES**

### **Code Examples Repository**
All implementation examples and templates available in:
`frontend/src/examples/project-discovery/`

### **API Documentation**
Enhanced API documentation with new endpoints:
`backend/docs/api-discovery.md`

### **Testing Scenarios**
Comprehensive test cases and mock data:
`frontend/src/tests/project-discovery/`

### **Performance Monitoring**
Analytics and monitoring setup:
`frontend/src/utils/analytics/ProjectDiscoveryMetrics.js`

---

**🎯 IMPLEMENTATION SUCCESS = Seamless, intelligent, context-aware project discovery that makes COAI immediately useful without configuration overhead!**
