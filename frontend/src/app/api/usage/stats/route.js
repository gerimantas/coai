import { NextResponse } from 'next/server'

const BACKEND_URL = process.env.BACKEND_URL || 'http://localhost:5000'

export async function GET(request) {
  try {
    const { searchParams } = new URL(request.url)
    const days = searchParams.get('days') || '7'
    
    console.log(`[USAGE API] Proxying request to: ${BACKEND_URL}/api/usage/stats?days=${days}`)
    
    const response = await fetch(`${BACKEND_URL}/api/usage/stats?days=${days}`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      },
    })
    
    if (!response.ok) {
      console.error(`[USAGE API] Backend responded with ${response.status}`)
      throw new Error(`Backend responded with ${response.status}`)
    }
    
    const data = await response.json()
    console.log(`[USAGE API] Success - returning ${JSON.stringify(data).length} bytes`)
    
    return NextResponse.json(data)
    
  } catch (error) {
    console.error('[USAGE API] Error:', error)
    return NextResponse.json(
      { error: 'Failed to fetch usage data', details: error.message },
      { status: 500 }
    )
  }
}
