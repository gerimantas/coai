import { NextResponse } from 'next/server'

const BACKEND_URL = process.env.BACKEND_URL || 'http://localhost:5000'

export async function GET(request) {
  try {
    const { searchParams } = new URL(request.url)
    const days = searchParams.get('days') || '7'
    
    const response = await fetch(`${BACKEND_URL}/api/usage/stats?days=${days}`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      },
    })
    
    if (!response.ok) {
      throw new Error(`Backend responded with ${response.status}`)
    }
    
    const data = await response.json()
    return NextResponse.json(data)
    
  } catch (error) {
    console.error('Usage API proxy error:', error)
    return NextResponse.json(
      { error: 'Failed to fetch usage data', details: error.message },
      { status: 500 }
    )
  }
}

export async function POST(request) {
  try {
    const body = await request.json()
    
    const response = await fetch(`${BACKEND_URL}/api/usage/export`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(body),
    })
    
    if (!response.ok) {
      throw new Error(`Backend responded with ${response.status}`)
    }
    
    const data = await response.json()
    return NextResponse.json(data)
    
  } catch (error) {
    console.error('Usage export API proxy error:', error)
    return NextResponse.json(
      { error: 'Failed to export usage data', details: error.message },
      { status: 500 }
    )
  }
}
