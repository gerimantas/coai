import { NextResponse } from 'next/server'

const BACKEND_URL = process.env.BACKEND_URL || 'http://localhost:5000'

export async function GET(request) {
  try {
    const { searchParams } = new URL(request.url)
    const project_path = searchParams.get('project_path')
    
    let url = `${BACKEND_URL}/api/plans`
    if (project_path) {
      url += `?project_path=${encodeURIComponent(project_path)}`
    }
    
    const response = await fetch(url, {
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
    console.error('Plans API proxy error:', error)
    return NextResponse.json(
      { error: 'Failed to fetch plans', details: error.message },
      { status: 500 }
    )
  }
}

export async function POST(request) {
  try {
    const body = await request.json()
    
    const response = await fetch(`${BACKEND_URL}/api/plans`, {
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
    console.error('Plans create API proxy error:', error)
    return NextResponse.json(
      { error: 'Failed to create plan', details: error.message },
      { status: 500 }
    )
  }
}
