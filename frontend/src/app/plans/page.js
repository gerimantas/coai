"use client"

import { useState, useEffect } from 'react'
import PageContainer from "@/components/ui/PageContainer"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/Card"
import { Badge } from "@/components/ui/Badge"
import { Button } from "@/components/ui/Button"

const PlansPage = () => {
  const [plans, setPlans] = useState([])
  const [selectedPlan, setSelectedPlan] = useState(null)
  const [showCreateForm, setShowCreateForm] = useState(false)
  const [newPlanRequest, setNewPlanRequest] = useState('')
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    fetchPlans()
  }, [])

  const fetchPlans = async () => {
    try {
      setLoading(true)
      const response = await fetch('/api/plans')
      if (response.ok) {
        const data = await response.json()
        setPlans(data.plans || [])
      }
    } catch (error) {
      console.error('Error fetching plans:', error)
    } finally {
      setLoading(false)
    }
  }

  const createPlan = async () => {
    if (!newPlanRequest.trim()) return

    try {
      const response = await fetch('/api/plans', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          request: newPlanRequest,
          project_context: {
            path: window.location.pathname
          }
        })
      })

      if (response.ok) {
        const data = await response.json()
        setPlans([...plans, {
          id: data.plan.id,
          title: data.plan.title,
          description: data.plan.description,
          completion_percentage: 0,
          total_tasks: data.plan.total_tasks,
          created_at: new Date().toISOString(),
          updated_at: new Date().toISOString()
        }])
        setNewPlanRequest('')
        setShowCreateForm(false)
      }
    } catch (error) {
      console.error('Error creating plan:', error)
    }
  }

  const fetchPlanDetails = async (planId) => {
    try {
      const response = await fetch(`/api/plans/${planId}`)
      if (response.ok) {
        const data = await response.json()
        setSelectedPlan(data.plan)
      }
    } catch (error) {
      console.error('Error fetching plan details:', error)
    }
  }

  const updateTaskStatus = async (planId, taskId, newStatus) => {
    try {
      const response = await fetch(`/api/plans/${planId}/tasks/${taskId}/status`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ status: newStatus })
      })

      if (response.ok) {
        // Refresh plan details
        fetchPlanDetails(planId)
        // Refresh plans list
        fetchPlans()
      }
    } catch (error) {
      console.error('Error updating task status:', error)
    }
  }

  const getStatusColor = (status) => {
    const colors = {
      pending: 'secondary',
      in_progress: 'default',
      completed: 'success',
      blocked: 'warning',
      cancelled: 'error'
    }
    return colors[status] || 'secondary'
  }

  const getPriorityColor = (priority) => {
    const colors = {
      low: 'secondary',
      medium: 'default',
      high: 'warning',
      critical: 'error'
    }
    return colors[priority] || 'secondary'
  }

  if (loading && plans.length === 0) {
    return (
      <PageContainer title="Action Plans" subtitle="Manage your project action plans and tasks">
        <div className="text-center">Loading action plans...</div>
      </PageContainer>
    )
  }

  return (
    <PageContainer title="Action Plans" subtitle="Manage your project action plans and tasks">
      <div className="space-y-6">
        
        {/* Header with Create Button */}
        <div className="flex justify-between items-center">
          <div>
            <h2 className="text-xl font-semibold">Your Action Plans</h2>
            <p className="text-sm text-gray-600">Create and manage step-by-step project plans</p>
          </div>
          <Button onClick={() => setShowCreateForm(true)}>
            Create New Plan
          </Button>
        </div>

        {/* Create Plan Form */}
        {showCreateForm && (
          <Card>
            <CardHeader>
              <CardTitle>Create New Action Plan</CardTitle>
              <CardDescription>Describe what you want to accomplish</CardDescription>
            </CardHeader>
            <CardContent>
              <div className="space-y-4">
                <textarea
                  value={newPlanRequest}
                  onChange={(e) => setNewPlanRequest(e.target.value)}
                  placeholder="Describe your project or goal in detail..."
                  className="w-full h-32 p-3 border rounded-md resize-none"
                />
                <div className="flex gap-2">
                  <Button onClick={createPlan} disabled={!newPlanRequest.trim()}>
                    Generate Plan
                  </Button>
                  <Button variant="outline" onClick={() => setShowCreateForm(false)}>
                    Cancel
                  </Button>
                </div>
              </div>
            </CardContent>
          </Card>
        )}

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          
          {/* Plans List */}
          <div className="lg:col-span-1 space-y-4">
            {plans.length === 0 ? (
              <Card>
                <CardContent className="text-center py-8">
                  <p className="text-gray-600">No action plans yet</p>
                  <p className="text-sm text-gray-400 mt-2">Create your first plan to get started</p>
                </CardContent>
              </Card>
            ) : (
              plans.map((plan) => (
                <Card 
                  key={plan.id} 
                  className={`cursor-pointer transition-colors ${
                    selectedPlan?.id === plan.id ? 'ring-2 ring-blue-500' : 'hover:bg-gray-50'
                  }`}
                  onClick={() => fetchPlanDetails(plan.id)}
                >
                  <CardContent className="p-4">
                    <h3 className="font-medium mb-2">{plan.title}</h3>
                    <p className="text-sm text-gray-600 mb-3 line-clamp-2">{plan.description}</p>
                    <div className="flex justify-between items-center text-xs text-gray-500">
                      <span>{plan.total_tasks} tasks</span>
                      <span>{Math.round(plan.completion_percentage)}% complete</span>
                    </div>
                    <div className="mt-2 w-full bg-gray-200 rounded-full h-2">
                      <div 
                        className="bg-blue-500 h-2 rounded-full" 
                        style={{ width: `${plan.completion_percentage}%` }}
                      ></div>
                    </div>
                  </CardContent>
                </Card>
              ))
            )}
          </div>

          {/* Plan Details */}
          <div className="lg:col-span-2">
            {selectedPlan ? (
              <Card>
                <CardHeader>
                  <CardTitle>{selectedPlan.title}</CardTitle>
                  <CardDescription>{selectedPlan.description}</CardDescription>
                  <div className="flex gap-4 text-sm text-gray-600">
                    <span>Created: {new Date(selectedPlan.created_at).toLocaleDateString()}</span>
                    <span>Updated: {new Date(selectedPlan.updated_at).toLocaleDateString()}</span>
                    <span>{Math.round(selectedPlan.completion_percentage)}% Complete</span>
                  </div>
                </CardHeader>
                <CardContent>
                  <div className="space-y-4">
                    {selectedPlan.tasks.map((task) => (
                      <div key={task.id} className="border rounded-lg p-4">
                        <div className="flex justify-between items-start mb-2">
                          <h4 className="font-medium">{task.title}</h4>
                          <div className="flex gap-2">
                            <Badge variant={getPriorityColor(task.priority)}>
                              {task.priority}
                            </Badge>
                            <Badge variant={getStatusColor(task.status)}>
                              {task.status.replace('_', ' ')}
                            </Badge>
                          </div>
                        </div>
                        <p className="text-sm text-gray-600 mb-3">{task.description}</p>
                        <div className="flex justify-between items-center">
                          <div className="flex gap-2 text-xs text-gray-500">
                            <span>{task.estimated_time} min</span>
                            {task.tags.map(tag => (
                              <span key={tag} className="bg-gray-100 px-2 py-1 rounded">
                                {tag}
                              </span>
                            ))}
                          </div>
                          <div className="flex gap-1">
                            {task.status === 'pending' && (
                              <Button 
                                size="sm" 
                                onClick={() => updateTaskStatus(selectedPlan.id, task.id, 'in_progress')}
                              >
                                Start
                              </Button>
                            )}
                            {task.status === 'in_progress' && (
                              <Button 
                                size="sm" 
                                onClick={() => updateTaskStatus(selectedPlan.id, task.id, 'completed')}
                              >
                                Complete
                              </Button>
                            )}
                            {task.status !== 'completed' && (
                              <Button 
                                size="sm" 
                                variant="outline"
                                onClick={() => updateTaskStatus(selectedPlan.id, task.id, 'blocked')}
                              >
                                Block
                              </Button>
                            )}
                          </div>
                        </div>
                      </div>
                    ))}
                  </div>
                </CardContent>
              </Card>
            ) : (
              <Card>
                <CardContent className="text-center py-12">
                  <p className="text-gray-600">Select a plan to view details</p>
                </CardContent>
              </Card>
            )}
          </div>
        </div>
      </div>
    </PageContainer>
  )
}

export default PlansPage
