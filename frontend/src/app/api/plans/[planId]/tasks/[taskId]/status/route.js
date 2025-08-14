import { NextResponse } from 'next/server'

const BACKEND_URL = process.env.BACKEND_URL || 'http://localhost:5000'

export async function PUT(request, { params }) {
  try {
    const { planId, taskId } = params
    const body = await request.json()
    
    const response = await fetch(`${BACKEND_URL}/api/plans/${planId}/tasks/${taskId}/status`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(body),
    })
    
    if (!response.ok) {
      if (response.status === 404) {
        return NextResponse.json(
          { error: 'Plan or task not found' },
          { status: 404 }
        )
      }
      throw new Error(`Backend responded with ${response.status}`)
    }
    
    const data = await response.json()
    return NextResponse.json(data)
    
  } catch (error) {
    console.error('Task status update API proxy error:', error)
    return NextResponse.json(
      { error: 'Failed to update task status', details: error.message },
      { status: 500 }
    )
  }
}
