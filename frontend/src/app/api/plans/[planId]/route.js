import { NextResponse } from 'next/server'

const BACKEND_URL = process.env.BACKEND_URL || 'http://localhost:5000'

export async function GET(request, { params }) {
  try {
    const planId = params.planId
    
    const response = await fetch(`${BACKEND_URL}/api/plans/${planId}`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      },
    })
    
    if (!response.ok) {
      if (response.status === 404) {
        return NextResponse.json(
          { error: 'Plan not found' },
          { status: 404 }
        )
      }
      throw new Error(`Backend responded with ${response.status}`)
    }
    
    const data = await response.json()
    return NextResponse.json(data)
    
  } catch (error) {
    console.error('Plan detail API proxy error:', error)
    return NextResponse.json(
      { error: 'Failed to fetch plan details', details: error.message },
      { status: 500 }
    )
  }
}
