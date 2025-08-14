import { NextResponse } from 'next/server'

const BACKEND_URL = process.env.BACKEND_URL || 'http://localhost:5000'

export async function GET(request) {
  try {
    const { searchParams } = new URL(request.url)
    const format = searchParams.get('format') || 'json'
    const days = searchParams.get('days') || '7'
    
    console.log(`[USAGE EXPORT] Proxying request to: ${BACKEND_URL}/api/usage/export?format=${format}&days=${days}`)
    
    const response = await fetch(`${BACKEND_URL}/api/usage/export?format=${format}&days=${days}`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      },
    })
    
    if (!response.ok) {
      console.error(`[USAGE EXPORT] Backend responded with ${response.status}`)
      throw new Error(`Backend responded with ${response.status}`)
    }
    
    if (format === 'csv') {
      const csvData = await response.text()
      return new NextResponse(csvData, {
        headers: {
          'Content-Type': 'text/csv',
          'Content-Disposition': `attachment; filename="usage-export-${new Date().toISOString().split('T')[0]}.csv"`,
        },
      })
    } else {
      const data = await response.json()
      return NextResponse.json(data)
    }
    
  } catch (error) {
    console.error('[USAGE EXPORT] Error:', error)
    return NextResponse.json(
      { error: 'Failed to export usage data', details: error.message },
      { status: 500 }
    )
  }
}
